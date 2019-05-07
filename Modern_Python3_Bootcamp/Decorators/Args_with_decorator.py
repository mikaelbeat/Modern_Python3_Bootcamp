
from functools import wraps


def ensure_no_kwargs(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError("No kwargs allowed!")
        return func(*args, **kwargs)
    return wrapper

@ensure_no_kwargs
def greet(name):
    print(f"Hi there {name}.")
    


greet("Tony")