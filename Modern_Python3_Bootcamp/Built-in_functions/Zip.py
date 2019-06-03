
# Compares values in same index and returns list of tuples

nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9, 10]

data = zip(nums1, nums2)


print("\n***** Printing zipped result as a list of tuples ******\n")
print(list(zip(nums1, nums2)))


print("\n***** Printing zipped result as a dictionary ******\n")
print(dict(zip(nums1, nums2)))


print("\n***** Using * unpacks zip and returns tuples ******\n")
print(list(zip(*data)))