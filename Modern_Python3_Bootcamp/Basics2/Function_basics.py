# Function basics

def testing():
    print("\nThis is one function!")
        
testing()


def calculate(number1, number2):
    sum = number1 + number2
    print("\nSum of numbers " + str(number1) + " and " +str(number2) + " is " + str(sum))
    
calculate(5, 6)


def multiply(number1, number2):
    sum = number1 * number2
    return sum

print("\nResult from multiply funcion " + str(multiply(6, 2)))



def addition(number1, numbe2):
    sum = number1 + numbe2
    return sum

sumFromMultiply = multiply(6, 2)

sumFromAddition = addition(sumFromMultiply, 10)

print("\nSum from addition is " + str(sumFromAddition))


# Fuction without arguments can also return value
def function_without_arguments():
    value = 100
    return value

print("\nFunction return value " + str(function_without_arguments()))