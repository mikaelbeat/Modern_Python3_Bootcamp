

# When using filter function needs to have boolean expression


names = ["Austin", "Penny", "Anthony", "Angel", "Billy"]


print("\n*** Filter names starting with A ***\n")
a_names = filter(lambda data: data[0] == "A", names)
print(list(a_names))



users = [
    {"username": "Samuel", "tweets": ["I love cats and cake"]},
    {"username": "Stone", "tweets": []},
    {"username": "Katie", "tweets": ["I hate cats and cake"]},
    {"username": "Matt", "tweets": []}
    ]

inactive_users = filter()

# 188 6:39