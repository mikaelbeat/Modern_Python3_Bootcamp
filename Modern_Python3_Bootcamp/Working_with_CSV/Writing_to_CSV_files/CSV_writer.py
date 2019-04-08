from csv import writer, reader

with open("fighters.csv", 'w') as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Character", "Move"])
    csv_writer.writerow(["Ryu", "Hadouken"])
    
with open("fighters.csv", 'r') as file:
    csv_reader = reader(file)
    for row in csv_reader:
        print(row)
        
        
print("\n ********** Creating new csv file with uppercase data **********\n")
        

# Reading all fighters file and saving it to variable
with open("fightersAll.csv", 'r') as file:
    csv_reader = reader(file)
    fighters = [[s.upper() for s in row] for row in csv_reader]
    for row in fighters:
        print(row)
        
with open("UPPERCASE_FIGHTERS.csv", 'w') as file:
    csv_writer = writer(file)
    for fighter in fighters:
        csv_writer.writerow(fighter)