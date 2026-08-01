import pandas as pd
import numpy as np
import array
pd.set_option('display.max_rows', 200)

# Reading midicsv output file to dataframe
df = pd.read_csv('data.dat', Index=True)
df1 = df.iloc[0:3, :]
df2 = df.iloc[3: , :]

# printing the data frame
print('DataFrame1')
print(df1)
print('DateFrame2')
print(df2)
   
type(df2)
df2.shape
df2.info()
df2.drop(5)
df2.columns = ['col1', 'col2', 'NoteStatus', 'col4', 'NoteNr', 'NoteValo']   # adding lables to the data-frame
col1 = df2['col1']
col2 = df2['col2']
NoteStatus = df2['NoteStatus']
col4 = df2['col4']
NoteNr = df2['NoteNr']
NoteValo = df2['NoteValo']
pd.set_option('display.max_rows', 200)
gd = df2.groupby(NoteNr).size()
print(gd)
dn = max(df2)
print(dn)

for L in range(128):
      Note_Number = df2.items[int(dn%12)]
      Scale =(dn//12)
      print(Note_Number, Scale)
      L += 1
      
df2.items = (['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B'])
EndP = df2.items['Note_Number']
EndQ = (str)(Scale-1)
print(EndP+"("+EndQ+")")
