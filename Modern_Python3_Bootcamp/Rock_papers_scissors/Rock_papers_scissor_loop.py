from random import randint

player_wins = 0
computer_wins = 0
winning_score = 3

while player_wins < winning_score and computer_wins < winning_score:
    
    random_number = randint(0,3)
    
    if (random_number == 0):
        p2 = "rock"
    elif (random_number == 1):
        p2 = "paper"
    else:
        p2 = "scissors"
        
    print("\n ********** ROCK PAPER SCISSORS & SUPER COMPUTER **********\n")
    print("\nPlayer wins: " + str(player_wins))
    print("\nComputer wins: " + str(computer_wins))
    p1 = input("\nPlayer 1: rock, paper, or scissors: ").lower()
    if (p1 == "quit" or p1 == "q"):
        break
    
    if ((p1 == "rock") or (p1 == "paper") or (p1 == "scissors")):  
        if p1 == p2:
            print("\nComputer played " + str(p2))
            print("\nDraw")
        elif p1 == "rock" and p2 == "scissors":
            print("\nComputer played " + str(p2))
            print("\nYou win!")
            player_wins += 1
        elif p1 == "paper" and p2 == "rock":
            print("\nComputer played " + str(p2))
            print("\nYou win!")
            player_wins += 1
        elif p1 == "scissors" and p2 == "paper":
            print("\nComputer played " + str(p2))
            print("\nYou win!")
            player_wins += 1
        else:
            print("\nComputer played " + str(p2))
            print("\nConputer wins!")
            computer_wins += 1
    else:
        print("\nInvalid input!")
        
print("\n********** FINAL SCORE **********\n")
print("Player: " + str(player_wins) + " - Computer: " + str(computer_wins))