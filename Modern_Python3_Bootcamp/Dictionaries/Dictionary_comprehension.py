
print({num: num**2 for num in [1, 2, 3, 4, 5]})

print("\n")

str1 = "ABC"
str2 = "123"
combo = {str1[i]: str2[i] for i in range(0, len(str1))}

print("\nCombo is: " + str(combo))