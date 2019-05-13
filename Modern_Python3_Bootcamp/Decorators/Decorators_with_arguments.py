
from functools import wraps


def ensure_first_arg_is(value):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args and args[0] != value:
                return f"First arg needs to be {value}"
            return func(*args, **kwargs)
        return wrapper
    return inner


@ensure_first_arg_is("burrito")
def fav_food(*foods):
    print(foods)
    
print(fav_food("burrito", "ice cream"))
print(fav_food("ice cream", "burrito"))



@ensure_first_arg_is(10)
def add_to_ten(value1, value2):
    return value1 + value2

print(add_to_ten(10, 12))
print(add_to_ten(1, 2))