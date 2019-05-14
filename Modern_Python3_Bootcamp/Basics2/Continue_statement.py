# Continue statement

number = input("Give number: ")

for i in range(1,11):
    if (int(number)* i %10 == 0):
        continue
    print(int(number) * i)