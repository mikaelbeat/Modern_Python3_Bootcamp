
print("\n********** Demo 1 **********\n")

numbers = [1, 2, 3, 4, 5]
doubled_numbers = []

for num in numbers:
    doubled_number = num * 2
    doubled_numbers.append(doubled_number)
    
print(doubled_numbers)


print("\n********** Demo 2 **********\n")

name = "Colt"

print([char.upper() for char in name])


print("\n********** Demo 3 **********\n")

print([bool(value) for value in [0, [], ""]])


print("\n********** Demo 4 **********\n")

string_list = [str(value) for value in numbers]

print(string_list)