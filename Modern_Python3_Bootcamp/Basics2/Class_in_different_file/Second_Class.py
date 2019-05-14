import Constructors

obj = Constructors.Demo()
obj.hello()
obj.calculate(45,45)
obj.multiply(3,5)
print("\nCalling multiply class function in another file " + str(obj.multiply(3,5)))