
numbers = [1, 2, 3, 4, 5,6, 7, 8, 9, 10]
text = "This is fun!"
numbers_text = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
names = ["James", "Michelle"]

print("\n********** Slice from given index **********\n")

# Slices list from given index, returns values after sliced index
print(numbers[1:])

# Sliced from counting given value from end of the list
print(numbers[-2:])


print("\n********** Slice from given index range **********\n")

# Slices up to given index value
print(numbers[:2])

# Slices list from given range
print(numbers[1:3])


print("\n********** Slice with using step **********\n")

# Slice from index 1 with step of 2
print(numbers[1::2])

# Slice from index 6 with step of 2 going backwards
print(numbers[6::-2])

# Reverse list
print(text[::-1])

# Reverse list
print(numbers_text[::-1])


print("\n********** Swapping values **********\n")

names[0], names[1] = names[1], names[0]
print(names)