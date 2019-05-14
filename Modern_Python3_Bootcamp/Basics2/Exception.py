# Exception handling in Python

try: 
    number1 = input("Please enter first number ")
    number2 = input("Please enter second number ")
    sum = int(number1) + int(number2)
    print("\nSum of numbers " + str(number1) + " and " + str(number2) + " is " + str(sum))
except:
    print("\nYou gave invalid data for calculation")
finally:
    print("\nThis code is run always in the end")