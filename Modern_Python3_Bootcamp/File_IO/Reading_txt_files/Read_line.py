

file = open("Story.txt")

print("\nreadline reads only one line\n")
# Readline read only one line.
data = file.readline()
print(data)


print("\nreadline return lines in list\n")
# Readlines return lines in list.
file.seek(0)
data = file.readlines()
file.close()
print(data)