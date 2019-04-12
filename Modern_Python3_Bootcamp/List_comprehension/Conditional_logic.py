
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

evens = [num for num in numbers if num % 2 == 0]

odds = [num for num in numbers if num % 2 != 0]

print("\nEven numbers " + str(evens))
print("\nOdd numbers " + str(odds))


print("\n********** Joining values **********\n")

data = ["cool", "cat"]

print(" ".join(data))