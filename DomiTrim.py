# For Trimming the csv header and footer

import pandas as pd
import numpy

# Sets limit of maximum rows to display on screen 

pd.set_option('display.max_rows', 200)

# Reading midicsv output file to dataframe
df = pd.read_csv('data.dat')  

# Splits data into df1 and df2
df1 = df.iloc[:5, :]
df2 = df.iloc[5:-2, :]

# Assigns collumn names to collumns 
col1 = df2['col1']
col2 = df2['col2']
NoteStatus = df2['NoteStatus']
col4 = df2['col4']
NoteNr = df2['NoteNr']
NoteValo = df2['NoteValo']

# Groups df2 data by individual note frequency
gd = df2.groupby(NoteNr).size()
print(gd)
gd.to_csv("c:\\users\\ruchi\\onedrive\\midiraga\\code\\PythonCode\\data02.csv",)
