
import re

pat = re.compile(r"^([a-z0-9_\.-]+)@([0-9a-z\.-]+)\.([a-z\.]{2,6})$")


pattern = re.compile(r"""
        ^([a-z0-9_\.-]+) # First part of the email
        @                # Single @ sign
        ([0-9a-z\.-]+)   # Email provider  
        \.               # Single dot
        ([a-z\.]{2,6})$  # 
""", re.VERBOSE | re.IGNORECASE)



match = pattern.search("thomas123@yahoo.com")
print(match.groups())
print(match.group())