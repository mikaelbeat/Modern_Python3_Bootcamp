# Constructor without arguments
class Demo:
    def __init__(self):
        print("\nThis is constructor")
        
    def hello(self):
        print("\nHello World")
            
    def calculate(self, number1, number2):
        sumOfNumbers = number1 + number2
        print("\nSum of numbers " + str(number1) + " and " + str(number2) + " is " + str(sumOfNumbers))
        
    def multiply(self, number1, number2):
        sumOfNumbers = number1 * number2
        return sumOfNumbers
