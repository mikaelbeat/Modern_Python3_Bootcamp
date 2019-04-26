

import re

def is_valid_time(data):
    time = re.compile(r"^\d{1,2}:\d{1,2}$")
    match = time.search(data)
    if match:
        return True
    return False


print(is_valid_time("10:45"))
print(is_valid_time("1:45"))
print(is_valid_time("10.45"))
print(is_valid_time("1999"))
print(is_valid_time("122:22545454545"))