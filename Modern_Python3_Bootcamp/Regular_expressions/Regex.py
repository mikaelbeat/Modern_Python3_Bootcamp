
import re

print("\n***** Match not found return None *****\n")

pattern = re.compile(r"\d{3} \d{3}-\d{4}")
res = pattern.search("Hello World!")
print(res)


print("\n***** search method *****\n")

# pattern.search return first found value
res = pattern.search("Call me at 310 445-9876 or 310 234-9999")

# Prints out object
print(res)

# res.group() gets found value from object
found_result = res.group()
print(found_result)


print("\n***** findall *****\n")

# pattern.findall return list of all found values
res = pattern.findall("Call me at 310 445-9876 or 310 234-9999")
print(res)


print("\n***** Another approach *****\n")

result = re.search(r"\d{3} \d{3}-\d{4}", "Call me at 310 445-9876").group()
print(result)