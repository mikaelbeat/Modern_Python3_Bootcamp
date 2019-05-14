# Tuples in Python
# Size of the tuple cannot be changed
# Data values in tuple cannot be changed

tuple1 = (45, "Monday", 12.5, "Friday", "Monday")
tuple2 = ("Monkey", 6000)

# Fetching amount of data values in tuple
print("\nIn tuple1 is " +  str(len(tuple1)) + " values.")

# Fetching all data in tuple
print("\nAll data in tuple1 is " + str(tuple1))

# Fetching value in index positio 3 from tuple1
print("\nIndex 3 position in tuple1 is value " + str(tuple1[3]))

# Fetching amount how many times specific value is in tuple
print("\nIn tuple1 value 'Monday' is " +  str(tuple1.count("Monday")) + " times.")

# Fetching index location of specific value in tuple
print("\nIn tuple1 value 'Friday' is located in index " + str(tuple1.index("Friday")))

# Concatenate two tuples to one
tuple3 = tuple1 + tuple2
print("\nTuple3 data is " + str(tuple3))

# Using for loop to get data in tuple
print("\nUsing for loop to get data from tuple3\n")
for i in tuple3:
    print(i)