
from functools import wraps

def ensure_fewer_than_three_args(func):
    @wraps(func)
    def wrapper(*args):
        if len(args) < 3:
            return func(*args)
        else:
            return "Too many arguments"
    return wrapper




@ensure_fewer_than_three_args
def add_all(*nums):
    return sum(nums)


print(add_all(1, 2))