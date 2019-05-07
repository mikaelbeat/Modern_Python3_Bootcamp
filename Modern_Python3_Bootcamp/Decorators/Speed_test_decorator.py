
from time import  time
from functools import wraps

def speed_test(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"Executin {func.__name__}")
        print(f"Time Elapsed: {end_time - start_time}")
        return result
    return wrapper


@speed_test
def sum_nums_gen():
    return sum(x for x in range(50000000))


@speed_test
def sum_nums_list():
    return sum([x for x in range(50000000)])

print("\n***** Run using generics *****")
print(sum_nums_gen())

print("\n***** Run using list comprehension *****")
print(sum_nums_list())
        