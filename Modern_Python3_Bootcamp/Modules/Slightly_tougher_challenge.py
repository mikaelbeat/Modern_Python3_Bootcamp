
import keyword

# keyword.iskeyword(value)
# Checks is Python keyword in given value set, eg. def


def contains_keyword(*args):
    for value in args:
        if keyword.iskeyword(value):
            return True
    return False
    
    
print(contains_keyword("def", "monkey"))
        