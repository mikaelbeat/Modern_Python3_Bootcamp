
import sqlite3

connection = sqlite3.connect("my_friends2.db")

# Create cursor object
c = connection.cursor()
 
# Execute some SQL
c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")
 
# Commit changes
connection.commit()
connection.close()
print("\nCreated database friends with friends table.")