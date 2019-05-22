

# Check is all values string

data = ["Data", "Cat", 3]


def is_all_strings(data):
    return all(type(value) == str for value in data)
        
print(is_all_strings(data))
     
    


def do_check(*args):
    for value in args:
        result = isinstance(value, str)
    return result



print(do_check(data))