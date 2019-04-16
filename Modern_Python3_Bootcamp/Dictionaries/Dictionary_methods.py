
instructor = {
    "name" : "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favourite_lanquage": "Python",
    "is_hilarious": False,
    44: "my_favourite_number"}


print("\n********** Clearing dictionary **********\n")
# instructor.clear()
# for values in instructor.items():
#     print(values)


print("\n********** Copy dictionary **********\n") 
instructor2 = instructor.copy()  

for values in instructor2.items():
    print(values)
    
    
print("\n********** From keys **********\n")
# Used to create dictionaty with initial values
# Creates new dictionary with default values unknown 
new_user = {}.fromkeys(["name", "score", "email", "profile bio"], "unknown")


print("\n********** Get **********\n")
# Fetch given key value from dictionary
print(instructor2.get("name"))
print(instructor2.get("owns_dog"))



