# Common string functions

print("\n********************** SET 1 ****************************")

emailAddress = "testingWORLD@edu.com"

# Fetch length of the string
print("\nLength of the email address is " + str(len(emailAddress)) + " characters.")

# Convert string to uppercase
print("\nString converterd to uppercase " + str(emailAddress.upper()))

# Convert string to lowercase
print("\nString converted to lowercase " + str(emailAddress.lower()))

# Set first letter to capital
print("\nFirst letter set to capital in string " + str(emailAddress.capitalize()))


print("\n********************** SET 2 ****************************")

emailAddress2 = "  testingWORLD@edu.com  "

# Fetch length of the string
print("\nFull lenght string with spaces " + str(len(emailAddress2)))

# Removes spaces from front of the string
print("\nlstrip removes two spaces in front of the string " + str(len(emailAddress2.lstrip())))

# Removes spaves after the string
print("\nrstrip removes two spaces after the string " + str(len(emailAddress2.rstrip())))

# Removes spaces around the string
print("\nstrip removes spaces around the string " + str(len(emailAddress2.strip())))


print("\n********************** SET 3 ****************************")

emailAddress3 = "testingworld@edu.com"

# Replace part of the string
print("\nReplaced edu to yahoo in string " + emailAddress3.replace("edu", "yahoo"))

# Find out is specific letter found in string using for loop
for i in emailAddress3:
    if (i == "w"):
        print("\nLetter w is found in string")

# Find out how many times specific letter found in string using for loop
times = 0
for i in emailAddress3:
    if (i == "e"):
        times += 1
print("\nLetter e is found " + str(times) + " times.")

# Find out how many times specific letter found in string

fullString = len(emailAddress3) # Returns string length 20
lettersRemovedFromString = len(emailAddress3.replace("e", "")) # Returns string length 18

print("\nLetter e is found in string " + str(fullString - lettersRemovedFromString) + " times.")


print("\n********************** SET 4 ****************************")

emailAddress4 = "This is my email address testingworld@edu.com email me!"

# Find given value in the string
value = "edu"
print("\nGiven value is found in string in index position of " + str(emailAddress4.find(value)))

# Split string with given separator
list1 = emailAddress4.split(" ")
print("\nNumber of strings in list is " + str(len(list1)))
print(list1)

# Using for loop to check if given string is found in list
for i in list1:
    if (i == "my"):
        print("\nString my is found in list")
        
# Using for loop to check how many times given string is found in list
foundTimes = 0

for i in list1:
    if (i == "email"):
        foundTimes += 1
print("\nWord email is found in string " + str(foundTimes) + " times.")
        
        



































