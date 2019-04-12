
print("\n********** Accessing values in nested list **********\n")

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("\nSecond value from first nested list " + str(nested_list[0][1]))

print("\nSecond value from second nested list " + str(nested_list[1][1]))

print("\nSecond value from third nested list " + str(nested_list[2][1]))


print("\n********** Printing all values in nested list **********\n")

for l in nested_list:
    for val in l:
        print(val)
        
print("\nAnother approach")    
print(nested_list)