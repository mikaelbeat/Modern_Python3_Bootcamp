
# Data is stored to dictionary in key value pairs

instructor = {
    "name" : "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favourite_lanquage": "Python",
    "is_hilarious": False,
    44: "my_favourite_number"}


print(instructor)


print("\n********** Check is value in dictionary **********\n")
print("\nCheck is phone string in dictionary")
print("phone" in instructor)
print("\nCheck is 'Python' string in dictionary values")
print("Python" in instructor.values())