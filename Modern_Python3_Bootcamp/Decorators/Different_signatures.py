
def shout(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper


@shout
def greet(name):
    return f"Hi, I'm {name}"


@shout
def order(main, side):
    return f"Hi, I'd like the {main}, with a side of {side}, please"


@shout
def lol():
    return "lol"


print(greet("todd"))

print(order("burger", "fries"))

print(lol())
