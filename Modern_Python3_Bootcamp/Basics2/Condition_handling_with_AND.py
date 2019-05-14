# Number is positive and divisible by 2

number = input("Give number: ")

number = int(number)

if (number >= 0 and number %2==0):
    print("Number is valid")
else:
    print("Number is invalid")