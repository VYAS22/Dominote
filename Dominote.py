import pandas as pd
import numpy as np
import array
pd.set_option('display.max_rows', 200)
df = pd.read_csv('data.dat')  # Reading midicsv output file to dataframe
df1 = df.iloc[:, :5]
df2 = df.iloc[:, 5:]
print(df)  # printing the data frame
type(df)
df.shape
df.info()
df.drop(5)
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
NoteValo = df['NoteValo']
pd.set_option('display.max_rows', 200)
gd = df.groupby(NoteNr).size()
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
print(EndP+"("+EndQ+")")