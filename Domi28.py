import csv

global Note_Number
Note_Number = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

with open('data02.csv', 'r') as data02:
    csv_reader = csv.reader(data02)
    next(csv_reader)

    for row in csv_reader:
        x: int = int(row[0]) % 12
        Note_Number[x] += int(row[1])

print(Note_Number)

    # Note_Number.to_csv("c:\\users\\ruchi\\onedrive\\midiraga\\code\\data03.csv",inxed=True)
