# Compare two strings
print("\nCompare strings")
text1 = "demo"
text2 = "Demo"

if (text1 == text2):
    print("Strings are same")
else:
    print("Strings are different")
    
    
# One string has spaces around
print("\nCompare strings when other string has spaces around")
text1 = "Demo"
text2 = "     Demo      "

if (text1.strip() == text2.strip()):
    print("Strings are same")
else:
    print("Strings are different")
    
    
# Compare strings when other has uppercase letters
print("\nCompare strings when other has uppercase letters")
text1 = "demo"
text2 = "Demo"

if (text1.upper() == text2.upper()):
    print("Strings are same")
else:
    print("Strings are different")
    
    
# Reverse my string
print("\nReverse my string")
text1 = "madam"
text2 = ""

stringLength = len(text1)

for i in range((stringLength - 1), -1, -1):
    text2 += text1[i]
    
if (text1 == text2):
    print("String is palendrome")
else:
    print("String is not palendrome")
    
print("String " + text1 + " converted backwards is " + text2)