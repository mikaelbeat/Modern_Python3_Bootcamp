
def sum_all_values(*args):
    total = 0
    for num in args:
        total += num
    print(total)
    
    
nums = [1, 2, 3, 4, 5, 6]

# Using * before parameters defines that python should take all values
# from collection individually and then pass them on to function
sum_all_values(*nums)