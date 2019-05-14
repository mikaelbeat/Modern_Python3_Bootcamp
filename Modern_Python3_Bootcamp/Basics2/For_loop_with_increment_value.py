# For loop increment value

start = input("Give start number: ")
end = input("Give ending number: ")
increment = input("Give increment number: ")

for i in range(int(start), int(end), int(increment)):
    print("Value is: " + str(i))

