

def generate_evens():
    values = []
    for i in range(2, 50, 2):
        values.append(i)
    return values

# def generate_evens():
#     result = []
#     for x in range(1,50):
#         if x % 2 == 0:
#             result.append(x)
#     return result

print(generate_evens())