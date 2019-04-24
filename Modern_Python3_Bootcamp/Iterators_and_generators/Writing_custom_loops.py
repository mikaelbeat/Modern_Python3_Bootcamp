
# Custom for loop

def my_for(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            value = (next(iterator))
        except StopIteration:
            break
        else:
            func(value)
        
    
my_for("Hello", print)

#my_for([1, 2, 3, 4, 5])