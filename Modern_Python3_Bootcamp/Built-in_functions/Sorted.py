
# Sorted returns sorted list from the given items

numbers = [5, 3, 2, 4, 1]

users = [
    {"username": "Samuel", "tweets": ["I love cats and cake", "Sunny beaches", "Alligators"]},
    {"username": "Stone", "tweets": []},
    {"username": "Katie", "tweets": ["I hate cats and cake"]},
    {"username": "Matt", "tweets": []},
    {"username": "Abel", "tweets": ["Tequila"]}
    ]

songs = [
    {"title": "Happy Bithday", "playcount": 1},
    {"title": "Survive", "playcount": 6},
    {"title": "YMCA", "playcount": 99},  
    {"title": "Toxic", "playcount": 31}, 
    ]


print("\n***** Sorting the data ******\n")
print(sorted(numbers))


print("\n***** Sorting the data in reverse ******\n")
print(sorted(numbers, reverse=True))


print("\n***** Sorting the data ******\n")
print(sorted(users, key=lambda user: user["username"]))


print("\n***** Sorting the data for most tweets ******\n")
print(sorted(users, key=lambda user: len(user["tweets"])))


print("\n***** Sorting the data for most playcount ******\n")
print(sorted(songs, key=lambda song: song["playcount"], reverse=True))