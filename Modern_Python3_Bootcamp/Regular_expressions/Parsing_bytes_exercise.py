

import re

def parse_bytes(data):
    bytes_regex = re.compile(r"\b\d{7}[01]\b")
    match = bytes_regex.findall(data)
    if match:
        return match
    return None
    
    
print(parse_bytes("11110000, 434343, 101, 00001111"))