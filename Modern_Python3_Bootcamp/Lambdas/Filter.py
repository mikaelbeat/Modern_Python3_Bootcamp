

# When using filter function needs to have boolean expression


names = ["Austin", "Penny", "Anthony", "Angel", "Billy"]


print("\n*** Filter names starting with A ***\n")
a_names = filter(lambda data: data[0] == "A", names)
print(list(a_names))


print("\n*** Filter inactive users ***\n")

users = [
    {"username": "Samuel", "tweets": ["I love cats and cake"]},
    {"username": "Stone", "tweets": []},
    {"username": "Katie", "tweets": ["I hate cats and cake"]},
    {"username": "Matt", "tweets": []}
    ]

inactive_users = list(filter(lambda user: not user["tweets"], users))
print(inactive_users)


print("\n*** Filter inactive usernames is uppercase ***\n")

usernames = list(map(lambda user: user["username"].upper(),
    filter(lambda user: not user["tweets"], users)))

print(usernames)




print("\n*** Combine map and filter ***\n")

names = ["Lassie", "Colt", "Rusty"]

instructor = list(map(lambda name: f"Your instructor is {name}",
         filter(lambda value: len(value) < 5, names)))

print(instructor)