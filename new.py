import pandas as pd
import numpy as np
import array
pd.set_option('display.max_rows', 200)
df = pd.read_csv('RagaJhinjhoti22.csv')
print(df)  
type(df)
df.shape
df.info()
df.columns = ['col1', 'col2', 'NoteStatus', 'col4', 'NoteNr', 'NoteValo']
print(df)
type(df)
df.shape
df.info()
col1 = df['col1']
col2 = df['col2']
NoteStatus = df['NoteStatus']
col4 = df['col4']
NoteNr = df['NoteNr']
df.NoteNr = df.NoteNr.astype(float)
NoteValo = df['NoteValo']
pd.set_option('display.max_rows', 200)
gd = df.groupby(NoteNr).size()
print(gd)
df = gd
df.fillna(0)
for j in range(128):
      for i in range(12):
            Flag = pd.isnull(j)
            if((i) == (j % 12) & ((i != 0) | (j != 0))):
                  df[i] += df[j]
                  continue
            elif(Flag):
                  df.fillna()
                  continue
            else:
                  continue
for k in range(12):
      print('/n')
      print(df.item[k])
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