

numbers = [4, 5, 6]

decrement_list = map(lambda value: value - 1, numbers)

print(list(decrement_list))




def decrement_list(data):
    return list(map(lambda value: value -1, data))


print(decrement_list(numbers))