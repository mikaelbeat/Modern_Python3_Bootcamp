
print("\n********** How to add and access docstring **********\n")
def say_hello():
    """ Test comment """
    return "Hello"

print(say_hello.__doc__)