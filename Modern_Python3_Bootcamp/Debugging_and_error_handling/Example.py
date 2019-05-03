

def divide(a, b):
    try:
        result =  a / b
    except ZeroDivisionError:
        print("\nDon't divide by zero!")
    except TypeError as err:
        print("\nValues must be int of float")
        print(err)
    else:
        print(f"{a} divided by {b} is {result}.")
    
    
print(divide(50, 2))
print(divide(50, 0))
print(divide(50, "f"))