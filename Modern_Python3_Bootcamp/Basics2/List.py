# Lists in Python

list1 = [1, 22.2, "Hello", 600, 3000, "Monday"]

# Fetch full list
print("\nFull list is " + str(list1))

# Fetch by index
print("\nIn second position in list1 is " + str(list1[1]))

# Fetch data from list using range
print("\nFetching second and third data from list1 " + str(list1[1:3]))

# Fetch data from list when giving only starting index 3
print("\nFetch data from list when giving only starting index 3 " + str(list1[3:]))

# Fetch data from list when giving only ending index 3
print("\nFetch data from list when giving only ending index 3 " + str(list1[:3]))

# Update value in list
list1[0] = 1000
print("\nFirst value in list is " + str(list1[0]))

# Insert value to list with given index
print("\nFull list before adding data " + str(list1))
list1.insert(3, "Snake")
print("\nFull list after adding value to index 3 " + str(list1))

# Remove value from the list
print("\nFull list before deleting data " + str(list1))
list1.remove("Monday")
print("\nFull list after deleting last value 'Monday' " + str(list1))