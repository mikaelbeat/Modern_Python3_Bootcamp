
# 'w' writes to file
with open("Haiku.txt", 'w') as file:
    file.write("Writing files is great!\n")
    file.write("Here is another good line\n")
    file.write("Closing now, good bye!\n")
      
      
# 'a' appends to file
with open("Haiku.txt", 'a') as file:
    file.write("Here is another good haiku\n")
    file.write("One of the best haiku ever\n")
    file.write("Last row of haiku!")
