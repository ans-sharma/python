# 3. Write two functions that simulate the toss of a fair coin, and the roll of
# an unbiased ‘n’ sided die using the random module.

import random


def coinToss():
    # head = 1 and tail = 0
    prob = random.randint(0, 1)
    if prob == 1:
        print("Heads")
    else:
        print("Tails")


def diceRoll(n):
    prob = random.randint(1, n)
    print(prob)


while(True):
    choice = int(input("Enter 1: to Toss a coin\n      2: to roll a dice\n      3: Exit\n=>"))
    if choice == 1:
        coinToss()
    elif choice == 2:
        n = int(input("no of sides of a dice: "))
        diceRoll(n)
    elif choice == 3:
        exit()
    else:
        print("Wrong Choice")
