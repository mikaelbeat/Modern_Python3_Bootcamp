
while True:
    try:
        number = int(input("\nPlease enter a number: "))
    except ValueError:
        print("\nThat's not a number")
    else:
        print("\nI'm in the else. You entered a number!")
        break
    finally:
        print("\nRuns no matter what!")