import pandas as pd
import numpy as np
import array
NoteNr = range(128)
NoteVelo = range(128)
pd.set_option('display.max_rows', 200)
df = pd.read_csv('Data.dat')
print(df)  
type(df)
df.shape
df.info()
df.columns = ['col1', 'col2', 'NoteStatus', 'col4', 'NoteNr', 'NoteVelo']
print(df)
type(df)
df.shape
df.info()
df.fillna(0)
col1 = df['col1']
col2 = df['col2']
NoteStatus = df['NoteStatus']
col4 = df['col4']
new_notenr = df.NoteNr.astype(int)
## new_notevelo = df.NoteVelo.astype(int)
## pd.set_option('display.max_rows', 200)

# Grouping the events by corresponding note numbers
df = df.groupby(new_notenr).size()
print(df)
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