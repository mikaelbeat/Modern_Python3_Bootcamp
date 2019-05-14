# Fetching substring

emailAddress = "mydemoemail@fake.com"

print("Full string -> " +emailAddress)

# Fetch value from given index
print("Fetch value from given index -> " + emailAddress[0])

# Fetch substring using start and end index
# Even though given range is 0-6 values from 0-5 is returned
print("Fetch substring using start and end index -> " + emailAddress[0:11])

# Fetch substring by giving start index only
print("Fetch substring by giving start index only -> " + emailAddress[11:])

# Fetch substring by giving end index only
print("Fetch substring by giving end index only -> " + emailAddress[:6])