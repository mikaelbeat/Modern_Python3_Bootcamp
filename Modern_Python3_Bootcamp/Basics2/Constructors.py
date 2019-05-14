# Constructor without arguments
class Demo:
    def __init__(self):
        print("\nThis is constructor")
         
obj = Demo()

# Constructor with arguments
class Demo2:
    def __init__(self, number1, number2):
        sumOfNumbers = number1 + number2
        print(sumOfNumbers)
    
obj2 = Demo2(50,75)