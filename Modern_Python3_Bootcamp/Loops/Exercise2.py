
from random import randint

number = 0
rounds = 0

while number != 5:
    number = randint(1,10)
    rounds += 1
    print("Round: " +str(rounds) + " random number is " + str(number))
    
print("Randon number is 5 in round " + str(rounds))
    
    