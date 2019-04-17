
print("\n********** Calculating with args **********\n")
def sum_all_nums(*args):
    total = 0
    for number in args:
        total += number
    return total
    
    
print(sum_all_nums(5, 6, 7))


print("\n********** Another args example **********\n")
def check_user(*args):
    if "Colt" in args and "Steele" in args:
        return "Welcome back!"
    return "Unknown user"

print(check_user("Colt", "Steele"))
print(check_user("Matt", "Damon"))

