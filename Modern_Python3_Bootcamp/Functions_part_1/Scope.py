
# Defining variable which resides outside the function
# global

total = 0

def increment():
    global total
    total += 1
    return total

print(increment())


# Defining variable which resides outside the function
# nonlocal

def outer_func():
    
    count = 0
    
    def inner_func():
        nonlocal count
        count += 1
        return count
    
    return inner_func()