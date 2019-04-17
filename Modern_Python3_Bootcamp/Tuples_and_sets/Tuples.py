
alphabet = ("a", "b", "c", "d", "a")

print("\n********** Looping tuples **********\n")
for value in alphabet:
    print(value)
    
    
print("\n********** Counting tuples values **********\n")
print(alphabet.count("a"))


print("\n********** Returns index of tuple value **********\n")
print(alphabet.index("a"))


# Tuples can be used as keys in dictionaries
locations = {
    (35.68, 39,69): "Tokyo Office",
    (40.71, 74.00): "New York Office",
    (37.77, 122.41): "San Francisco Office"
    }

