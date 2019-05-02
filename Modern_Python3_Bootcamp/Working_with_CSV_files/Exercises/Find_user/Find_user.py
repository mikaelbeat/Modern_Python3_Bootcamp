
from csv import reader


def find_user(first, last):
    with open("users.csv", "r") as file:
        csv_reader = reader(file)
        next(csv_reader)
        for row in csv_reader:
            if first and last in row:
                return f"\nUser {first} {last} is in the list."
    return f"\nUser {first} {last} is not in the list."
            

result = find_user("Dwayne", "Johnson")
print(result)

result = find_user("Kevin", "Sorbo")
print(result)

result = find_user("Demo", "Person")
print(result)