from _operator import le

list = ["One", "Two", 3]

# List length
print("\n********** Length of list **********\n")
print(len(list))

# Prints all values in list
print("\n********** ALl values in list **********\n")
print(list)

# Print all values in list using for loop
print("\n********** For looping list **********\n")
for item in list:
    print(item)
    
# While looping list
print("\n********** While looping list **********\n")
i = 0

while i < len(list):
    print(list[i])
    i += 1

# Check is given value in list
print("\n********** Check is value in list **********\n")
print("One" in list)

# Change value in index 0 to 1
print("\n********** Change value in list **********\n")
list[0] = 1





