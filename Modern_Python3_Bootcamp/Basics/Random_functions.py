
from random import randint
from random import choice


# Setting random number between 1 -3
random_number = randint(1,10)

print("***** Random number using randint *****")
print(f"\nRandom number is {random_number}")


# Using choice to randomly choice value
values = ("Yellow", "Green", "Red", "Black")
choice_value = choice(values)

print("\n***** Random number using choice *****")
print(f"\nRandom value is {choice_value}")

