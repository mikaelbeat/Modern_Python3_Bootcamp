
import sqlite3

connection = sqlite3.connect("my_friends2.db")

c = connection.cursor()

c.execute("SELECT * FROM friends")

# Returns data in tuple
# for result in c:
#     print(result)

# Returns data in list
print(c.fetchall())

connection.commit()
connection.close()