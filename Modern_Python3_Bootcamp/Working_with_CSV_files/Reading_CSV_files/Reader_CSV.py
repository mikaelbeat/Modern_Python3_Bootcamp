
from csv import reader

# Each row is list

print("\n************ Basic print ************\n")

# Using reader
with open("fighters.csv", "r") as csv_file:
    csv_reader = reader(csv_file)
    for row in csv_reader:
        print(row)
        
        
print("\n************ Anoter approach 1 ************\n")
        
        
with open("fighters.csv", "r") as csv_file:
    csv_reader = reader(csv_file)
    # Using next jumps over headers and everything after it is printed
    next(csv_reader)
    for fighter in csv_reader:
        print(f"{fighter[0]} is from {fighter[1]}")
        
        
print("\n************ Anoter approach 2 ************\n")
        
        
with open("fighters.csv", "r") as csv_file:
    csv_reader = reader(csv_file)
    # Reads data from file to list data
    data = list(csv_reader)
    #next(csv_reader)
    print(data)
    
    
print("\n************ Anoter approach 3 ************\n")
        
        
with open("fighters.csv", "r") as csv_file:
    csv_reader = reader(csv_file, delimiter="|")
    for row in csv_reader:
        print(data)