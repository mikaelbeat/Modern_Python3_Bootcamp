
from random import randint

randomNumber = randint(1,3)

if (randomNumber == 1):
    p2 = "rock"
elif (randomNumber == 2):
    p2 = "paper"
else:
    p2 = "scissors"
    

print("\n ********** ROCK PAPER SCISSORS & SUPER COMPUTER **********\n")
p1 = input("Player 1: rock, paper, or scissors: ")
p1 = p1.lower()


if ((p1 == "rock") or (p1 == "paper") or (p1 == "scissors")):  
    if p1 == p2:
        print("\nComputer played " + str(p2))
        print("\nDraw")
    elif p1 == "rock" and p2 == "scissors":
        print("\nComputer played " + str(p2))
        print("\nYou win!")
    elif p1 == "paper" and p2 == "rock":
        print("\nComputer played " + str(p2))
        print("\nYou win!")
    elif p1 == "scissors" and p2 == "paper":
        print("\nComputer played " + str(p2))
        print("\nYou win!")
    else:
        print("\nComputer played " + str(p2))
        print("\nConputer wins!")
else:
    print("\nInvalid input!")