

import sqlite3

connection = sqlite3.connect("users.db")

c = connection.cursor()

# Create table
#c.execute("CREATE TABLE users (username TEXT, password TEXT);")


# Create table data
data = [
    ("Blue", "Meow"),
    ("Rosa", "12345"),
    ("Henry", "Monkey"),
    ("Neil", "password1"),
    ("Daniel", "4334343443434")
]

#c.executemany("INSERT INTO users VALUES (?, ?)", data)


# Print table data
# result = c.execute("SELECT * FROM users")
# 
# for result in result:
#     print(result)

# Logging in demo
username = input("\nPlease enter your username: ")
password = input("\nPlease enter your password: ")

query = f"SELECT * FROM users WHERE username=? AND password=? "

c.execute(query,(username, password))
result = c.fetchone()
if result:
    print("\nWelcome back!")
else:
    print("\nFailed login!")

    

connection.commit()
connection.close()