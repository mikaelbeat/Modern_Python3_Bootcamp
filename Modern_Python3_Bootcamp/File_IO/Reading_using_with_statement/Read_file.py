
# File must be close
file = open("Data.txt", 'r')
print(file.read())
file.close()

# File is closed automaticly
with open("Data.txt", 'r') as file:
    print(file.read())