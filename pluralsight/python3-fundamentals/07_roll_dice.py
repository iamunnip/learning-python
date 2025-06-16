import random

roll = random.randint(1, 6)

guess = int(input("Guess the dice roll "))

if roll == guess:
    print("Correct, rolled " + str(roll))
else:
    print("Wrong, rolled " + str(roll))
