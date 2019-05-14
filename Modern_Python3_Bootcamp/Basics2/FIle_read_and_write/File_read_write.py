# Read and write to file

# r - read only
# w - write mode
# a - append mode
# r+ - read & write
# w+ - write read
# a+ - append read

# Open file in location -> r for read mode
f = open("data.txt", "r")

# Tell in which position cursor is in the file
# print(f.tell())

# Move cursor to given position in file
# print(f.seek(100))

# Read all data in file
print(f.read())

# Read one line from file
#print(f.readline())

# Read given amount of characters
#print(f.read(5))

# Open file in location -> a for append mode
# f = open("data.txt", "a")
# f.write("This is the next data")
# f.close()
