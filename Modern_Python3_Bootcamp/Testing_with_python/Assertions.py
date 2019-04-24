# Running python file excluding any assertions
# python -O file.py


def add_positive_numbers(value1, value2):
    assert value1 > 0 and value2 > 0, "Both numbers must be positive!"
    return value1 + value2

print("\n***** Assertion demo *****\n")
print(add_positive_numbers(5, 5))
#print(add_positive_numbers(5, -5))


print("\n***** Assertion, junk food *****\n")
def eat_junk_food(food):
    
    assert food in ["pizza", 
                    "candy",
                    "ice cream"], "Food must be a junk food!"
    
    return f"\nI am eating {food}\n"

food = input("Enter a food please: ")
print(eat_junk_food(food))


print("\n***** Validate input *****\n")
def say_hi(name):
  assert name == "Colt", "I only say hi to Colt!"
  return f"Hi, {name}!"
 
print(say_hi("Charlie"))