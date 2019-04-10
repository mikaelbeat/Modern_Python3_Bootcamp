 
for i in range(1,21):
    if i == 4 or i == 13:
        print(str(i) + " is unlucky number")
    elif i % 2 != 0:
        print(str(i) + " is odd number")
    else:
        print(str(i) + " is even number")
        
        
print("\n********** Another approach **********\n")
        
        
for i in range(1,21):
    if i == 4 or i == 13:
        state = "unlucky"
    elif i % 2 == 0:
        state = "even"
    else:
        state = "odd"
    print(f"{i} is {state}")