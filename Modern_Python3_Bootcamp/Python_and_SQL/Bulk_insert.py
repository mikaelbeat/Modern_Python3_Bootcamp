import sqlite3

connection = sqlite3.connect("my_friends.db")

c = connection.cursor()

people = [
    ("Ronald", "Amudsen", 5),
    ("Rosa", "Parks", 8),
    ("Henry", "Hudson", 7),
    ("Neil", "Armstrong", 7),
    ("Daniel", "Boone", 3)
]

c.executemany("INSERT INTO friends VALUES (?, ?, ?)", people)

# Another approach
# for person in people:
#     c.execute("INSERT INTO friends VALUES (?, ?, ?)", person)
#     print("Inserting now")


connection.commit()
connection.close()

print("\nAdded bulk of friends to database.")