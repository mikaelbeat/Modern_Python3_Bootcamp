
import re

url_regex = re.compile(r"(https?)://(www\.[A-za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)")

match = url_regex.search("http://www.youtube.com/videos")

print("\n***** Print match.group() *****\n")
print(match.group())
print("\n")


print("\n***** Print match.group(0) *****\n")
print(match.group(1))
print("\n")


print("\n***** Print match.group(1) *****\n")
print(match.group(2))
print("\n")


print("\n***** Print match.groups() *****\n")
print(match.groups())
print("\n")


print("\n***** Print match.groups() *****\n")
print(f"Protocol: {match.group(1)}")
print(f"Domain: {match.group(2)}")
print(f"Everything else: {match.group(3)}")