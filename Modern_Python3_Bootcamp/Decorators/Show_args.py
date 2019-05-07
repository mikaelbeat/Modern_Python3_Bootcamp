
from functools import wraps


def show_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\nHere are the args: {args}.")
        print(f"Here are the kwargs {kwargs}.")
        return func(*args, **kwargs)
    return wrapper
        
        
@show_args        
def do_nothing(*args, **kwargs):
    pass
        
        
print(do_nothing(1, 2, 3,a="hi",b="bye"))