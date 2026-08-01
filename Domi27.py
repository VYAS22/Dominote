import csv
my_list = '0' * 128
print(my_list)
with open('data02.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        rose = row[0]
        jaz = row[1]
        my_list.insert(my_list[rose], rose)
        my_list.insert((my_list[rose])+1, row[1])

print(my_list)
