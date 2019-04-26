
import re

print("\n***** Substitution using Regex *****\n")

text = "Last night Mrs. Daisy and Mr. White murdered Mr. Chow."

pattern = re.compile(r"(Mr\.|Mrs\.|Ms\.) [a-z]+", re.IGNORECASE)
result = pattern.sub("REDACTED", text)

print(result)


print("\n***** Another approach *****\n")


text = "Last night Mrs. Daisy and Mr. White murdered Mr. Chow."

pattern = re.compile(r"(Mr\.|Mrs\.|Ms\.) ([a-z])[a-z]+", re.IGNORECASE)
result = pattern.sub("\g<1> \g<2>", text)

print(result)
