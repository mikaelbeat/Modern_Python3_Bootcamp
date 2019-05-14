# Break statement

start = input("Give start number: ")
end = input("Give ending number: ")

for i in range(int(start), int(end)):
    if (i == 5):
        break
    print("Value is: " + str(i))