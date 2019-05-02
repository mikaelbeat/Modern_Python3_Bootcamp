

def get_multiples(num=1, count=10):
    next_num = num
    while count > 0:
        yield next_num
        count -= 1
        next_num += num


data = get_multiples(5, 50)

for value in data:
    print(value)