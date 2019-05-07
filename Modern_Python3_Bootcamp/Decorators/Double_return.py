
from functools import wraps


def double_return(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        return [value, value]
    return wrapper
        
              

@double_return
def add(value1, value2):
    return value1 + value2


@double_return
def greet(name):
    return "Hi, I'm " + name



print(add(1, 2))
print(greet("Colt"))