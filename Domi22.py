import pandas as pd
import numpy as np
import array
pd.set_option('display.max_rows', 200)
tnotes  = ([0,0,0,0,0,0,0,0,0,0,0,0])
df = pd.read_csv('data.dat')  # Reading midicsv output file to dataframe
df = df.iloc[5:-2]
#df1 = df.iloc[:, :5]
#df2 = df.iloc[:, 5:]
print(df)  # printing the data frame
type(df)
df.shape
df.info()
#df.drop(5)
df.columns = ['col1', 'col2', 'NoteStatus', 'col4', 'NoteNr', 'NoteValo']
print(df)
#type(df)
#df.shape()
#df.info()
col1 = df['col1']
col2 = df['col2']
NoteStatus = df['NoteStatus']
col4 = df['col4']
NoteNr = df['NoteNr']
NoteValo = df['NoteValo']
#pd.set_option('display.max_rows', 200)
pn  =  df.groupby('NoteNr').size()
pn.columns = ['NoteNr', 'FSize']
print(pn)
# variables to be figured out in place of 37 and 103 (min, max) of pn
TNotes = [0,0,0,0,0,0,0,0,0,0,0,0]
c = NoteNr.min()
d = NoteNr.max()
print(c,d)
for k in range (c+1,d-1):    
      j = (k%12)
      TNotes[j] = TNotes[j] + pn.iloc[k]
      k += 1
print(TNotes)
pmax = max(TNotes)
dominote = pn.idxmax(pmax)
print(dominote%12)
pn.item = (['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B'])
print(pn.item[int(dominote%12)])

#Note_Number = (int)((Dominote % 12))
#Scale = (int)(Dominote/12)
#print(Note_Number)
#df.item = (['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B'])
#EndP = df.item[Note_Number]
#EndQ = (str)(Scale-1)
#print(EndP+"("+EndQ+")")