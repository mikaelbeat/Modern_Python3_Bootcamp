
import re

def extract_phone(data):
    phone_regex = re.compile(r"\b\d{3} \d{3}-\d{4}\b")
    match = phone_regex.search(data)
    if match:
        return match.group()
    return None

def extract_all_phones(data):
    phone_regex = re.compile(r"\b\d{3} \d{3}-\d{4}\b")
    return phone_regex.findall(data)

  
print(extract_phone("My number is 432 567-8976"))
print(extract_phone("My number is 432 567-897699"))
print(extract_all_phones("All my numbers are 123 456-1212 and 004 123-4567"))
    
    
def is_valid_phone(data):
    phone_regex = re.compile(r"^\d{3} \d{3}-\d{4}$")
    match = phone_regex.search(data)
    if match:
        return True
    return False

print(is_valid_phone("Cat"))
print(is_valid_phone("123 456-5678"))

# fullmatch return only if fullmatch is found. So no ^ or $ signs are needed!
def is_valid_phone_fullmatch(data):
    phone_regex = re.compile(r"\d{3} \d{3}-\d{4}")
    match = phone_regex.fullmatch(data)
    if match:
        return True
    return False

print(is_valid_phone_fullmatch("123 456-5678"))