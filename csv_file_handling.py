import csv

with open("covid.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
print("****************************************************************************************************************************************")
# ['Albania', '1521', '36', '1044', '441', '57', '0', '5', '2.37', '68.64', '3.45', '1246', '275', '22.07', 'Europe']
with open("covid.csv","r") as file:
    reader = csv.reader(file, delimiter = '\t')
    for row in reader:
        print(row)
# ['Andorra,853,51,781,21,0,0,0,5.98,91.56,6.53,852,1,0.12,Europe']
print("****************************************************************************************************************************************")
with open("covid.csv","r") as file:
    reader = csv.reader(file, delimiter = '|')
    for row in reader:
        print(row)
# ['Vietnam,334,0,323,11,0,0,0,0.0,96.71,0.0,331,3,0.91,Western Pacific']
print("****************************************************************************************************************************************")
with open('covid.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    for row in reader:
        print(row)
# ['Vietnam', '334', '0', '323', '11', '0', '0', '0', '0.0', '96.71', '0.0', '331', '3', '0.91', 'Western Pacific']
print("****************************************************************************************************************************************")
with open("covid.csv",'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
# {'Country/Region': 'Zambia', 'Confirmed': '1358', 'Deaths': '11', 'Recovered': '1122', 'Active': '225', 'New cases': '1', 
# 'New deaths': '1', 'New recovered': '18', 'Deaths / 100 Cases': '0.81', 'Recovered / 100 Cases': '82.62', 'Deaths / 100 Recovered': '0.98',
#  'Confirmed last week': '1089', '1 week change': '269', '1 week % increase': '24.7', 'WHO Region': 'Africa'}
print("****************************************************************************************************************************************")
with open("covid.csv","r") as file:
    reader = list(csv.DictReader(file))
    data = reader[:10]
print(data[1])
