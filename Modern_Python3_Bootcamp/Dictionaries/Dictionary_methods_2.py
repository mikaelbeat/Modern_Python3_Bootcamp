
instructor = {
    "name" : "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favourite_lanquage": "Python",
    "is_hilarious": False,
    44: "my_favourite_number"}


print("\n********** pop() removes given item from dictionary **********\n")
instructor.pop("name")

for values in instructor:
    print(values)


print("\n********** popitem() removes random item from dictionary **********\n")
print(instructor.popitem())
print(instructor.popitem())


print("\n********** update() updates given item in dictionary **********\n")

instructor2 = {
    "name" : "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favourite_lanquage": "Python",
    "is_hilarious": False,
    44: "my_favourite_number"}

instructor2["name"] = "Steel"

print(instructor2.get("name"))