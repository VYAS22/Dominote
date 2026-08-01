import pandas as pd
from pandas import isna

pd.set_option('display.max_rows', 200)

# Reading midicsv output file to dataframe
df2 = pd.read_csv('data.dat')
df2 = df2.drop([0, 1, 2, 3])
print(df2)

# printing the data frame
# print('DataFrame1')
# print(df1)
# print('DateFrame2')
# print(df2)

# df2.drop(5)
type(df2)
df2.shape
df2.info()

df2.columns = ['IDX', 'col2', 'NoteStatus', 'col4', 'NoteNr', 'NoteValo']   # adding lables to the data-frame
col1 = df2['IDX']
col2 = df2['col2']
NoteStatus = df2['NoteStatus']
col4 = df2['col4']
NoteNr = df2['NoteNr']
NoteValo = df2['NoteValo']
##
gd = int('0' * 127)
print("test24")
gd  = df2.groupby('NoteNr').size()
gn = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(gn)
for i in range(0, 127):
      if ( isna(gd[i]) == False ):
            k = i%12
            gn.set_value[k] = gn[k] + gd[i]
      else:
            gd.set_value[i] = 0
print(gn)
#
Dominote = df3.idxmax()
print(Dominote)
Note_Number = (int)((Dominote % 12))
Scale = (int)(Dominote/12)
print(Note_Number)
df4.item = (['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B'])
EndP = df3.item[Note_Number]
EndQ = (str)(Scale-1)
print(EndP+"("+EndQ+")")
