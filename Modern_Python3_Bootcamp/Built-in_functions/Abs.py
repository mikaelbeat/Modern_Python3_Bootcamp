
from math import fabs
from builtins import round

# Absolute value

data = -5
data2 = -4.5
data3 = [1, 2, 3, 4 ,5]

print("\n***** Absolute value of -5 is 5 ******\n")
print(abs(data))


print("\n***** Absolute value of -4.5 is 4.5 ******\n")
print(abs(data2))


print("\n***** Sum adds valuest together, 0 is from what value calculation starts ******\n")
print(sum(data3, 0))


print("\n***** Round returns value by given decimals ******\n")
value = 12.31313131313
print(round(value, 2))


print("\n***** Round, if return decimal amount is set to None, value will just be rounded ******\n")
value = 12.61313131313
print(round(value, None))