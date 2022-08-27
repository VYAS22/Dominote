import csv

global Note_Number
Note_Number = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

with open('data03.csv', 'r') as data03:
    csv_reader = csv.reader(data03)
##    next(csv_reader)

    for row in csv_reader:
        x: int = int(row[0]) % 12
        Note_Number[x] += int(row[1])

print(Note_Number)

    # Note_Number.to_csv("c:\\users\\ruchi\\onedrive\\midiraga\\code\\data03.csv",inxed=True)
