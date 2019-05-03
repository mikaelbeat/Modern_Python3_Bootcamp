
d = {"name": "Ricky"}


def get(dictionary, key):
    try:
        return d[key]
    except KeyError:
        return None
    
    
print(get(d, "city"))