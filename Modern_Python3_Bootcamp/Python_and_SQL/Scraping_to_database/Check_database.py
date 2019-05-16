
import sqlite3

connection = sqlite3.connect("books.db")

c = connection.cursor()

print("\n ***** All books in database *****\n")
c.execute("SELECT * FROM books")


# Returns data in tuple
# for result in c:
#     print(result)

# Returns data in list
print(c.fetchall())


print("\n ***** 4 or more rated books *****\n")
c.execute("SELECT * FROM books WHERE rating >= 4")
print(c.fetchall())


connection.commit()
connection.close()