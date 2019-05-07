
from functools import wraps

def only_ints(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        if any([arg for arg in args if type(arg) != int]):
            return "Please only invoke with integers."
        return fn(*args, **kwargs)
    return inner



@only_ints
def add(*nums):
    return sum(nums)



print(add(1, 2, 3))