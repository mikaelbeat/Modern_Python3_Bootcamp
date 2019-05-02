import csv
from csv import reader, writer
 
# def delete_users(first_name, last_name):
#     with open("users.csv") as csvfile:
#         csv_reader = csv.reader(csvfile)
#         rows = list(csv_reader)
#  
#     count = 0
#     with open("users.csv", "w") as csvfile:
#         csv_writer = csv.writer(csvfile)
#         for row in rows:
#             if row[0] == first_name and row[1] == last_name:
#                 count += 1
#             else:
#                 csv_writer.writerow(row)
#  
#     return "Users deleted: {}.".format(count)


# print(delete_users("Colt", "Steele"))




def delete_user(first, last):
    with open("users.csv", "r") as file:
        csv_reader = reader(file)
        next(csv_reader)     
        for row in csv_reader:
            if first and last in row:
                with open("users.csv", "w+") as file:
                    csv_writer = writer(file)
                    csv_writer.writerow(row)
                return f"\nUser {first} {last} deleted from database."
        return f"\nUser {first} {last} is not in the database."
        
            
            
print(delete_user("Grace", "Hopper"))