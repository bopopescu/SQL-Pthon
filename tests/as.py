import random

Balls = list(range(1, 51))
Powerballs = list(range(1, 21))
print(Balls)

list_winners = []
list_powerball = []
for i in range(5):
    # if  Balls.pop(random.randint(0, len(Balls)))
    i = Balls.pop(random.randint(0, len(Balls)))
    print(i)

    list_winners.append(i)
pwerball = Powerballs.pop(random.randint(0, len(Powerballs)))
print("List of numbers " + str(list_winners) + " Bonus Ball " + str(pwerball))

# while len(list_winners) <= 5:
# print(choices.pop())
# print(list_winners)
