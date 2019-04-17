
set1 = {1, 2, 3, 4, 5}
set2 = set({7, 8, 9, 10})
set3 = {"Moscow", "Tokyo", "Kioto"}
set5 = {"Vietnam", "Nepal", "China"}

print("\n********** Add to set **********\n")
set1.add(6)
print(set1)


print("\n********** Remove from set **********\n")
set2.remove(10)
print(set2)


print("\n********** Discard from set **********\n")
# Will not give error if trying to remove value which is not in set
set3.discard("Moscow")
print(set3)


print("\n********** Copy set **********\n")
set4 = set3.copy()
print(set4)


print("\n********** clear, removes all contents from the set **********\n")
set5.clear()
print(set5)