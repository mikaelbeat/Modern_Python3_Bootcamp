
file = open("data.txt", 'r')
print(file.read())
file.close()


with open("data.txt", 'r') as file:
    print(file.read())