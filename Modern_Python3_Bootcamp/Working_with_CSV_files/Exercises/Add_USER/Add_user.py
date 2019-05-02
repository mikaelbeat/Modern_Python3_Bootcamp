
from csv import writer, reader
import csv


def add_user(first, last):
    with open("users.csv", "a") as file:
        csv_writer = writer(file)
        csv_writer.writerow(["Firstname", "Lastname"])
        csv_writer.writerow([first, last])
        
        
def read_file(file):
    with open(file, "r") as file:
        csv_reader = reader(file)
        for row in csv_reader:
            print(row)
            

def print_users():
    with open("users.csv") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            print("{} {}".format(row["Firstname"], row["Lastname"]))
            
            
            
#add_user("Dwayne", "Johnson")

read_file("users.csv")

print_users()
    