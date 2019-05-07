
from functools import wraps


# @wraps(func) is a function which is called in wrapper function to preserve metadata


def log_function_data(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """I am wrapper function"""
        print(f"you are about to call {func.__name__}")
        print(f"Here's the documentation: {func.__doc__}")
        return func(*args, **kwargs)
    return wrapper


@log_function_data
def add(value1, value2):
    """Adds two numbers together"""
    return value1 + value2


print(add(5, 7))

print("\n ***** Preserved metadata *****")

print(add.__doc__)
print(add.__name__)