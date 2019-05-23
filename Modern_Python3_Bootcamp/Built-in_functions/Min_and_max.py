
# Max returns largest value
# Min returns smallers value


values = [10, 20, 40, 39, 9]

value = "Morning"

names = ["Samson", "Arya", "Dora", "Tim", "Ollivander"]

songs = [
    {"title": "Happy Bithday", "playcount": 1},
    {"title": "Survive", "playcount": 6},
    {"title": "YMCA", "playcount": 99},  
    {"title": "Toxic", "playcount": 31}, 
    ]


print("\n*** Max returns largest value ***\n")
print(max(values))
print(max(value))
print(max(names, key=lambda name: len(name)))
print(max(songs, key=lambda song: song["playcount"]))
print(max(songs, key=lambda song: song["playcount"])["title"])


print("\n*** Min returns smallest value ***\n")
print(min(values))
print(min(value))
print(min(names, key=lambda name: len(name)))
print(min(songs, key=lambda song: song["playcount"]))
print(min(songs, key=lambda song: song["playcount"])["title"])