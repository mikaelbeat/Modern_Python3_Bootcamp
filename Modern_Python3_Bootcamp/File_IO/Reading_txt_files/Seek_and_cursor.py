

file = open("story.txt")

# Seek moves cursor to given position and starts read from there on.
file.seek(1)
data = file.read()
file.close()
print(data)