
# Runs lambda for each value in the iterable and returns a map object


print("\n*** Basic function ***\n")
def calculate(value):
    return value + value

print(calculate(5))



print("\n*** Lambda function ***\n")
calculate2 = lambda value: value + value

print(calculate2(5))


