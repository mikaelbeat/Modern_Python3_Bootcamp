

# Formal mathematical sets
# Do not have duplicate values
# Elements aren't ordered
# Cannot access items by index

set1 = {1, 2, 3, 4, 5}
set2 = set({7, 8, 9, 10})

print("\n********** Printing set **********\n")
print(set1)


print("\n********** Check is given value in set **********\n")
print(1 in set1)
print(6 in set1)


print("\n********** Looping throught set **********\n")
for value in set1:
    print(value)
    
    
print("\n********** Set can only contain unique values **********\n")
cities = ["Tokyo", "Oslo", "Los Angeles", "Tokyo", "Oslo", "Los Angeles"]
print(set(cities))
# Print how many unique values are in set
print(len(set(cities)))