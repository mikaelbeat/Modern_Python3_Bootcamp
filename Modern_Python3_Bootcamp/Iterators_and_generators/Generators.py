
# Generator returns generator object
# yield stores value, so counting starts where count was previously left
# Print statemenst goes for 1 -3 and for loop continues to 4 - 5

def count_up_to(value):
    count = 1
    while count <= value:
        yield count
        count += 1
        

print(count_up_to(10))

counter = count_up_to(5)

print("\n***** Printing counter several times *****\n")

print(next(counter))
print(next(counter))
print(next(counter))

print("\n***** Using for loop *****\n")

for value in counter:
    print(value)