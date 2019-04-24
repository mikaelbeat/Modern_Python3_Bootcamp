# For running doctests input is 
# python -m doctest -v file.py

def add (value1, value2):
    
    """
    >>> add(5, 5)
    10
    
    >>> add(100, 100)
    200
    """
    
    return value1 + value2


def say_hi():
    """
    
    >>> say_hi()
    'hi'

    """
    return 'hi'


def double(values):
    """ Double the values in a list
    
    >>> double([1, 2, 3, 4, 5])
    [2, 4, 6, 8, 10]
    
    >>> double([])
    []
    
    >>> double(["a", "b", "c"])
    ['aa', 'bb', 'cc']

    >>> double([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: "int" and "NoneType"
    
    """
    
    return [2 * element for element in values]