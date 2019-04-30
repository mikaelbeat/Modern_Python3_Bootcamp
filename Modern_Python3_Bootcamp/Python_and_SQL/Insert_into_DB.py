
import sqlite3

connection = sqlite3.connect("my_friends.db")

# Create cursor object
c = connection.cursor()

# Execute some SQL
insert_query = "INSERT INTO friends VALUES ('Merriwether', 'Lewis', 7)"
c.execute(insert_query)


form_first = "Dana"
query = f"INSERT INTO friends (first_name) VALUES (?)"
c.execute(query, (form_first,))


data = ("Steve", "Irwin", 9)
query = f"INSERT INTO friends VALUES (?, ?, ?)"
c.execute(query, data)




# Commit changes
connection.commit()
connection.close()
print("\nAdded new friend to database.")