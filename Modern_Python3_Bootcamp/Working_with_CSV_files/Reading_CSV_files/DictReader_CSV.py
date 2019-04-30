
from csv import DictReader

# Each row is OrderedDict
    
print("\n************ Reading using ordereddict ************\n")  
# Using DictReader
with open("fighters.csv", "r") as csv_file:
    csv_reader = DictReader(csv_file)
    for row in csv_reader:
        print(row)


print("\n************ Anoter approach ************\n")

with open("fighters.csv", "r") as csv_file:
    csv_reader = DictReader(csv_file)
    for row in csv_reader:
        print(row["Name"])