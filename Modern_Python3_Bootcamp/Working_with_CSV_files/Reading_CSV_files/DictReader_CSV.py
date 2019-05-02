
from csv import DictReader
import csv

# Each row is OrderedDict
    
print("\n************ Reading using ordereddict ************\n")  
# Using DictReader
with open("fighters.csv", "r") as csv_file:
    csv_reader = DictReader(csv_file)
    for row in csv_reader:
        print(row)


print("\n************ Another approach 1 ************\n")

with open("fighters.csv", "r") as csv_file:
    csv_reader = DictReader(csv_file)
    for row in csv_reader:
        print(row["Name"])
        

print("\n************ Another approach 2 ************\n")       
        
def print_fighters():
    with open("fighters.csv") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            print("{} - {}".format(row["Name"], row["Country"]))
            
print_fighters()