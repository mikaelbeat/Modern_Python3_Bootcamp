

def add(value1, value2):
    return value1 + value2

def substract(value1, value2):
    return value1 - value2

def math(value1, value2, fn=add):
    return fn(value1, value2)

print(math(5, 5, add))