
numbers1 = [1, 2, 3, 4]
numbers2 = [3, 4, 5, 6]

names = ["Ellie", "Tim", "Matt"]

answer = [val for val in [1,2,3,4] if val in [3,4,5,6]]

answer2 = [val[::-1].lower() for val in ["Elie", "Tim", "Matt"]]


print(answer)
print(answer2)