import pandas as pd
import numpy as np
import array
df = pd.read_csv('data.dat', index_col=None)
print(df)  
df.info()
df.columns = ['col1', 'col2', 'NoteStatus', 'col4', 'NoteNr', 'NoteValo']
print(df)
type(df)
df.shape
df.info()
## col1 = df['col1']
## col2 = df['col2']
## NoteStatus = df['NoteStatus']
## col4 = df['col4']
## NoteNr = df['NoteNr']
## NoteValo = df['NoteValo']
gd = df.groupby('NoteNr').size()
print(gd)
df = gd
Max = max(df)
print(Max)
Dominote = df.idxmax()
print(Dominote)
Note_Number = (int)((Dominote % 12))
Scale = (int)(Dominote/12)
print(Note_Number)
df.item = (['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B'])
EndP = df.item[Note_Number]
EndQ = (str)(Scale-1)
print(EndP+EndQ)
