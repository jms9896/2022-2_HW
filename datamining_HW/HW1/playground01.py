import csv

f = open('Seoul.csv', 'r', encoding="cp949")
reader = csv.reader(f)
for line in reader:
    print(line)
f.close



# with open('Seoul.csv', 'r', encoding='cp949') as file:
#     for line in file:
#         data = line.strip().split(',')
#         print(data)