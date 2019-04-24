
from random import choice

def eat(food, is_healty):
    if not isinstance(is_healty, bool):
        raise ValueError("is_healty must be a boolean!")
    ending = "because it is good"
    if is_healty:
        ending = "because it is healty"
    return f"I'm eating {food}, {ending}"

def nap(num_hours):
    if num_hours >= 2:
        return f"I overslept! I didn't mean to nap {num_hours} hours"
    return "After 1 hour nap I am full of energy!"

def is_funny(person):
    if person is "Tim": 
        return False
    return True

def laugh():
    return choice(("lol", "haha", "tehehe"))


print(eat("Banana", True))

print(nap(1))