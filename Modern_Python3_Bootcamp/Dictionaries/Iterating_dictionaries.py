
instructor = {
    "name" : "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favourite_lanquage": "Python",
    "is_hilarious": False,
    44: "my_favourite_number"}


print("\n********** keys() **********\n")
# Using for loop for accessing instructor dictionary key
for value in instructor.keys():
    print(value)


print("\n********** values() **********\n")
# Using for loop for accessing instructor dictionary values
for value in instructor.values():
    print(value)
    
    
print("\n********** items() **********\n")    
# Using for loop for accessing instructor dictionary values using items()
for value in instructor.items():
    print(value)
    
    
print("\n********** items() looping using key and value variables **********\n")    
# Using for loop for accessing instructor dictionary values using items()
for key, value in instructor.items():
    print(f"Key is {key} and value is {value}")