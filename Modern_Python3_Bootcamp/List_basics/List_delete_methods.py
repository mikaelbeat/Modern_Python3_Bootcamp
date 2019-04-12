print("\n********** Clear **********\n")

list1 = [1, 2, 3, 4, 5]

# Deletes everything in the list
list1.clear()

print(list1)


print("\n********** Pop **********\n")

list2 = [1, 2, 3, 4, 5]

# Without givin any index, it just removes last value
list2.pop()

# Revoving value in given index
list2.pop(0)

print("\n" + str(list2))

list3 = ["One", "Two", "Three"]

last_item = list3.pop()
print("\n" + last_item)


print("\n********** Remove **********\n")

list4 = ["One", "Two", "Three", "Four"]

# Removes given value from the list
# If list has multiple same values, first matching value is removed
list4.remove("Two")

print("\n" + str(list4))