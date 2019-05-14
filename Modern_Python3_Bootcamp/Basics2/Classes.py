
class Demo:
    def welcome(self):
        print("\nThis is class function")
        
obj = Demo()
obj.welcome()


class Demo2:
    def hello(self):
        print("\nHello World")
            
    def calculate(self, number1, number2):
        sumOfNumbers = number1 + number2
        print("\nSum of numbers " + str(number1) + " and " + str(number2) + " is " + str(sumOfNumbers))
        
    def multiply(self, number1, number2):
        sumOfNumbers = number1 * number2
        return sumOfNumbers
    
obj2 = Demo2()
obj2.hello()
obj2.calculate(50, 50)
print("Return value from class function is " + str(obj2.multiply(5, 6)))

        

        
    