# Dictionaries in Python
# Given keys must be unique, otherwise first keys value is overwritten

dictio1 = {"K1":"Val1", 2:"Val3", "K3":32}

# Fetch all keys and values in dictionary
print("\nAll keys and values in dictionary dictio1 are " + str(dictio1))

# Fetching all keys and values using .items function
print("\nAll keys and values using .items function" + str(dictio1.items()))

# Fetching all values in dictionary
print("\nAll values in dictionary are " + str(dictio1.values()))

# Fetch all keys in dictionary
print("\nAll keys in dictionary are " + str(dictio1.keys()))

# Fetch value from given key
print("\nKey K1 value is " + dictio1["K1"])

# Fetching amount how many key value pairs are in dictionary
print("\nDictionary has " + str(len(dictio1)) + " key value pairs")

# Add a new key value pair to dictionary
print("\nAll values in dictio1 before adding new data " + str(dictio1))
dictio1["K4"] = 6000
print("\nAll values in dictio1 after adding new key value pair 'K4 - 6000' " + str(dictio1))
