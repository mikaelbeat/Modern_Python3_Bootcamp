from random import randint

number = randint(1,10)
guess = None

while  True:
    guess = input("\nGuess the number between 1 and 10: ")
    guess = int(guess)
    if (guess > number):
        print("\nYour guess is too high, try again!")
    elif (guess < number):
        print("\nYOur guess is too low, try again!")
    else:
        print("\nYou guessed it!")
        choise = input("\nDo you want to play again? y / n ")
        if (choise == "n"):
            print("\nThank you for playing!")
            break