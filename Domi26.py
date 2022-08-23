import pandas as pd
import numpy

pd.set_option('display.max_rows', 200)
df = pd.read_csv('data.dat')  # Reading midicsv output file to dataframe
df1 = df.iloc[:, :5]
df2 = df.iloc[:, 5:]

print(df)  # printing the data frame
type(df)
#df.shape
df.info()
df.drop(5)
df.columns = ['col1', 'col2', 'NoteStatus', 'col4', 'NoteNr', 'NoteValo']
print(df)
type(df)
##df.shape
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
gd.to_csv("c:\\users\\ruchi\\onedrive\\midiraga\\code\\data02.csv",)
