# For loop with list

list1 = [1,3,5,7,10,20, "Testing","World","www.pythoncoding.com"]

for i in list1:
    print(i)
    
    
print("\n******************************\n")


for i in "PYTHON":
    print(i)
    
    
print("\n******************************\n")


list2 = [2,5,6,7,8,10]

start = 0

for i in list2:
    start += i

print("List sum is: " + str(start))