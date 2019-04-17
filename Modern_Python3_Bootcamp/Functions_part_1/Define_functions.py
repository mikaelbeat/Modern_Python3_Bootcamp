print("\n********** Basic function **********\n")
def happy_birthday(name):
    print(f"Happy bithday to {name}")
    
happy_birthday("cat")


print("\n********** Return function **********\n")

def calculate_something(value1, value2):
    sum = value1 + value2
    return sum

sum_for_values = calculate_something(5, 5)
print(sum_for_values)