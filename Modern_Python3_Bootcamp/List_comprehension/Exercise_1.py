
names = ["Ellie", "Tim", "Matt"]

numbers = [1, 2, 3, 4,5 ,6]

answer = [person[0] for person in names]
 
answer2 = [num for num in numbers if num % 2 == 0]


print("\nFirst letter of each name: " + str(answer))
print("\nEven numbers from list: " + str(answer2))



