
# r  - reading
# w  - writing, overwrites all
# a  - appends to file
# r+ - read and write to file(writing based on cursor)


# 'w' writes to file
with open("Data.txt", 'r+') as file:
    file.seek(10)
    file.write("Added using r+\n")

       
