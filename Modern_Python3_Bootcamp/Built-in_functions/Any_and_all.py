
# All returns true if all values are truthy or values are empty

true_list = [1, 2, 3, 4]
false_list = [0, 1, 2]
empty_list = []
people = ["Charlie", "Casey", "Cody", "Carly", "Cristina"]


print("\n********** All true list **********\n")
print(all(true_list))


print("\n********** All false list **********\n")
print(all(false_list))


print("\n********** All empty list **********\n")
print(all(empty_list))


print("\n********** Returns true is all names starts with C **********\n")
print(all(name[0] == "C" for name in people))



# Any returns true if all values are not empty -> BUT RETURNS FALSE IS VALUE IS EMPTY

print("\n********** Any true list **********\n")
print(any(true_list))


print("\n********** Any false list, true is returned because none of the values are empty **********\n")
print(any(false_list))


print("\n********** Any empty list **********\n")
print(any(empty_list))