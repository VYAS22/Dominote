#!/usr/bin/env python3

"""
summarize_code.py

Usage:
  python summarize_code.py "C:/Users/ruchi/PythonCode/" --output "local_summary.xlsx" --existing "Dominote_summary.csv"

Dependencies:
  pip install pandas openpyxl

"""
import os
import argparse
import ast
import tokenize
import io
import hashlib
from collections import OrderedDict
import pandas as pd

PY_EXTENSIONS = {'.py'}

def file_sha256_text(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()

def first_comment_block(source):
    # Return first group of leading comments (if any)
    try:
        g = tokenize.generate_tokens(io.StringIO(source).readline)
    except Exception:
        return ''
    comments = []
    last_line = -1
    for toknum, tokval, start, end, line in g:
        if toknum == tokenize.COMMENT:
            if last_line + 1 == start[0] or last_line == -1:
                comments.append(tokval.lstrip('#').strip())
                last_line = start[0]
            else:
                break
        elif toknum == tokenize.NL or toknum == tokenize.NEWLINE:
            # continue scanning
            continue
        elif toknum == tokenize.STRING and last_line == -1:
            # a module docstring would be token.STRING at top; we will let ast.get_docstring handle it
            break
        else:
            break
        if len(comments) >= 10:
            break
    return '\n'.join(comments).strip()

def analyze_py_file(path):
    info = {
        'FileName': os.path.relpath(path),
        'Executable': False,
        'Logic': '',
        'Function': '',
        'sha256': file_sha256_text(path),
    }
    try:
        with open(path, 'r', encoding='utf-8', errors='replace') as f:
            source = f.read()
    except Exception as e:
        info['Logic'] = f'Could not read file: {e}'
        return info

    # shebang
    lines = source.splitlines()
    has_shebang = len(lines) > 0 and lines[0].startswith('#!')

    # docstring via AST
    try:
        module = ast.parse(source, filename=path)
        doc = ast.get_docstring(module) or ''
    except Exception:
        module = None
        doc = ''

    # detect main guard
    has_main_guard = '__name__' in source and '__main__' in source and 'if __name__' in source

    # top-level statements (beyond docstring, imports, defs)
    top_level_non_def = False
    funcs = []
    classes = []
    imports = set()
    if module:
        for node in module.body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                funcs.append(node.name)
            elif isinstance(node, ast.ClassDef):
                classes.append(node.name)
            elif isinstance(node, (ast.Import, ast.ImportFrom)):
                if isinstance(node, ast.Import):
                    for n in node.names:
                        imports.add(n.name.split('.')[0])
                else:
                    if node.module:
                        imports.add(node.module.split('.')[0])
            else:
                # Exclude simple module docstring as top-level (it's represented as Expr(Constant(str)))
                if not (isinstance(node, ast.Expr) and isinstance(getattr(node, 'value', None), ast.Constant) and isinstance(node.value.value, str)):
                    top_level_non_def = True

    # first comment block
    comment_block = first_comment_block(source)

    # decide executable
    info['Executable'] = has_shebang or has_main_guard or top_level_non_def

    # Build Logic summary heuristically
    logic_parts = []
    if doc:
        logic_parts.append(doc.strip().splitlines()[0])
    elif comment_block:
        logic_parts.append(comment_block.splitlines()[0])
    if imports:
        logic_parts.append("imports: " + ", ".join(sorted(list(imports))[:6]))
    if funcs:
        logic_parts.append(f"defines {len(funcs)} function(s)")
    if classes:
        logic_parts.append(f"defines {len(classes)} class(es)")
    if top_level_non_def and not has_main_guard:
        logic_parts.append("contains top-level executable statements")

    info['Logic'] = " | ".join(logic_parts) if logic_parts else "No docstring or notable top-level structure found"

    # Short Function description heuristics (one-liner)
    lower_text = (doc + "\n" + comment_block + "\n" + source[:400]).lower()
    if any(k in lower_text for k in ('dominote', 'dominant', 'dominote', 'dominote', 'dominant key', 'dominant note')):
        info['Function'] = "Detect dominant MIDI note / compute pitch-class dominance"
    elif any(k in lower_text for k in ('midi', 'midicsv', 'data.dat')):
        info['Function'] = "Process midicsv-style data (data.dat) to analyze notes or durations"
    elif 'librosa' in imports or 'librosa' in lower_text or 'cqt' in lower_text:
        info['Function'] = "Analyze audio (CQT) and visualize spectrum (librosa)"
    elif 'csv' in imports and 'note' in lower_text:
        info['Function'] = "Aggregate note counts from CSV"
    elif funcs and not info['Executable']:
        info['Function'] = f"Library module providing {len(funcs)} function(s)"
    elif info['Executable']:
        info['Function'] = "Script that can be run (contains top-level code or main guard)"
    else:
        # fallback: summarize imports
        if imports:
            info['Function'] = "Script using " + ", ".join(sorted(list(imports))[:3])
        else:
            info['Function'] = "General Python file (no clear one-line purpose found)"

    return info

def collect_files(root_dir=r"C:\", extensions=PY_EXTENSIONS):
    results = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for fn in filenames:
            _, ext = os.path.splitext(fn)
            if ext.lower() in extensions:
                full = os.path.join(dirpath, fn)
                results.append(full)
    return sorted(results)

def load_existing_summary(path):
    if not path:
        return None
    if not os.path.exists(path):
        raise FileNotFoundError(f"Existing summary not found: {path}")
    df = pd.read_csv(path, dtype=str)
    # Normalize FileName column
    if 'FileName' not in df.columns:
        raise KeyError("Existing summary must have a 'FileName' column")
    return df

def merge_with_existing(generated_df, existing_df, prefer_existing=True, match_by='filename'):
    """
    - match_by: 'filename' or 'sha'
    - If prefer_existing True, rows in existing_df replace generated rows on match
    """
    if existing_df is None:
        return generated_df
    gen = generated_df.copy()
    ex = existing_df.copy()

    # Ensure columns exist in existing
    for col in ['Index', 'FileName', 'Executable', 'Logic', 'Function']:
        if col not in ex.columns:
            ex[col] = None

    # Build index by matching key
    merged_rows = OrderedDict()

    if match_by == 'sha' and 'sha256' not in ex.columns:
        # cannot match by sha if existing doesn't have it
        match_by = 'filename'

    # map existing keys
    existing_map = {}
    for _, row in ex.iterrows():
        key = row['FileName']
        existing_map[key] = row

    # iterate gen rows; if filename in existing_map prefer existing
    final_rows = []
    used_existing_keys = set()
    for _, g in gen.iterrows():
        fname = g['FileName']
        if fname in existing_map and prefer_existing:
            final_rows.append(existing_map[fname].to_dict())
            used_existing_keys.add(fname)
        else:
            final_rows.append(g.to_dict())

    # add any existing rows that didn't match (unique ones)
    for key, row in existing_map.items():
        if key not in used_existing_keys:
            final_rows.append(row.to_dict())

    # produce dataframe
    final_df = pd.DataFrame(final_rows)
    # reindex and set Index column numeric
    final_df = final_df.reset_index(drop=True)
    final_df.insert(0, 'Index', range(1, len(final_df) + 1))
    # ensure columns order
    cols = ['Index', 'FileName', 'Executable', 'Logic', 'Function']
    for c in cols:
        if c not in final_df.columns:
            final_df[c] = ''
    final_df = final_df[cols]
    return final_df

def main():
    parser = argparse.ArgumentParser(description="Scan a directory of Python files and produce a summary CSV/XLSX.")
    parser.add_argument('dir', dir='Directory to scan (e.g. C:\\Users\\ruchi\\PythonCode)')
    parser.add_argument('--output', '-o', default='local_summary.xlsx', help='Output Excel filename (.xlsx)')
    parser.add_argument('--csv', default=None, help='Also write CSV output (optional)')
    parser.add_argument('--existing', '-e', default=None, help='Path to existing summary CSV to merge/replace duplicates')
    parser.add_argument('--match-by', choices=['filename', 'sha'], default='filename', help='How to detect duplicates when merging with existing summary')
    parser.add_argument('--extensions', default='.py', help='Comma-separated file extensions to include (default .py)')
    parser.add_argument('--write-csv', action='store_true', help='Also write summary.csv beside Excel')
    args = parser.parse_args()

    exts = set([e if e.startswith('.') else '.'+e for e in args.extensions.split(',')])

    files = collect_files(args.dir, extensions=exts)
    if not files:
        print("No files found in directory with extensions:", exts)
        return

    rows = []
    for path in files:
        info = analyze_py_file(path)
        # canonicalize filename relative to scan dir
        info['FileName'] = os.path.relpath(path, start=args.dir)
        rows.append(info)

    gen_df = pd.DataFrame(rows)
    gen_df = gen_df.reset_index(drop=True)
    gen_df.insert(0, 'Index', range(1, len(gen_df) + 1))
    # Keep only relevant columns for output (but preserve sha256 internally if needed)
    # For merging, we supply FileName, Executable, Logic, Function (sha256 stays if needed)
    summary_df = gen_df[['Index', 'FileName', 'Executable', 'Logic', 'Function', 'sha256']].copy()

    existing_df = None
    if args.existing:
        try:
            existing_df = load_existing_summary(args.existing)
        except Exception as e:
            print("Warning: could not load existing summary:", e)
            existing_df = None

    final_df = merge_with_existing(summary_df, existing_df, prefer_existing=True, match_by=args.match_by)

    # Save to Excel
    out_xlsx = args.output
    if not out_xlsx.lower().endswith('.xlsx'):
        out_xlsx += '.xlsx'
    csv_out = args.csv or (os.path.splitext(out_xlsx)[0] + '.csv')
    try:
        # drop sha256 column before final output if present
        if 'sha256' in final_df.columns:
            final_df_to_write = final_df.drop(columns=['sha256'])
        else:
            final_df_to_write = final_df
        final_df_to_write.to_excel(out_xlsx, index=False, engine='openpyxl')
        print("Wrote Excel:", out_xlsx)
        final_df_to_write.to_csv(csv_out, index=False)
        print("Wrote CSV:", csv_out)
    except Exception as e:
        print("Error writing output files:", e)

if __name__ == '__main__':
    main()