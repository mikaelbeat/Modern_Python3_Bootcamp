
print("\n*** Map with numbers ***\n")
nums = [2, 4, 6, 8, 10]


doubles = map(lambda x: x * 2, nums)

for num in doubles:
    print(num)
    
    
print("\n*** Map with string ***\n")

people = ["Darcy", "Christina", "Dana", "Annabel"]

peeps = map(lambda name: name.upper(), people)
print(list(peeps))