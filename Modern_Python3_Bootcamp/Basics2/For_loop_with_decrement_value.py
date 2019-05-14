# For loop with decrement value

start = input("Give starting number: ")
end = input("Give ending number: ")
decrement = input("Give decrement value: ")

for i in range(int(start), int(end), int(decrement)):
    print("Decrement value is: " + str(i))