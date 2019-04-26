
import re

# (?P<first>[A-Za-z]+)
# ?P<> is used to give name for the group     ->  ?P<group name>

def parse_name(data):
    name_regex = re.compile(r"^(?P<title>Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)$")
    matches = name_regex.search(data)
    print(matches.group("first"))
    


parse_name("Mrs. Tilda Swinton")