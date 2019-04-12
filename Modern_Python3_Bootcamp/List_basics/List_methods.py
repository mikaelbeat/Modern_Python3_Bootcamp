
numbers = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Nine", "Ten"]
numbers2 = [5, 2, 1, 3, 4]
words = ["Coding", "is", "fun"]

print("\n********** Search value from list **********\n")

# Return index where given value is located
print("\nNumber four is located at index " + str(numbers.index("Four")))

# Starting point for search can also be defined
# This will seach string "Five" from list starting at index position 3
numbers.index("Five", 3)

# Starting and ending point for search can also be defined
# This will seach string "Five" from list between indexes fo 3 and 7
numbers.index("Five", 3, 7)


print("\n********** Count values in list **********\n")

# Counts hpw many times given value is in list
print("\nNumber Nine is in numbers list " + str(numbers.count("Nine")) + " times.")


print("\n********** Reverse list **********\n")

numbers.reverse()

print(numbers)


print("\n********** Sort list **********\n")

numbers2.sort()

print(numbers2)


print("\n********** Join list **********\n")

# Joins values in list to one value
# " " adds space between values
print(" ".join(words) + "\n")

# Adds comma between values
print(".".join(words) + "\n")



