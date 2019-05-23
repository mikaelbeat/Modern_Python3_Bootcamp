

data = [1, 50, 2, 66, 90]
data2 = "Alcatraz"


def extremes(*args):
    mi = min(*args)
    ma = max(*args)
    return mi, ma


print(extremes(data))
print(extremes(data2))