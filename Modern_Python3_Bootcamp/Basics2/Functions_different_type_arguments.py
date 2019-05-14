# Functions with different types arguments

# Keyword arguments
def takeInput(number1, number2):
    sumOfNumbers = number1 + number2
    print("\nSum of numbers " + str(number1) + " and " +  str(number2) + " is " + str(sumOfNumbers) + ".")
    
takeInput(number1=1000, number2=4000)

# Default argument
# Default argument must always be defined in last
def defaultArguments(number1, number2=100):
    sumOfNumbers = number1 + number2
    print("\nSum of numbers " + str(number1) + " and " +  str(number2) + " is " + str(sumOfNumbers) + ".")
    
defaultArguments(500)
