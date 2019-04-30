
def copy(data):
    with open(data, "r") as file:
        read_data = file.read()
    with open(f"Copy_{data}", "w") as copy:
        copy.write(read_data)
            
copy("Alice.txt")