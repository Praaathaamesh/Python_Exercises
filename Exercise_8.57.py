# roll dice in such a way that every time you get the same number

import random
random.seed(10)
x = random.randint(1,6)
def roll_dice():
  return x
n = int(input("please enter how many times you want to roll the dice: "))
for i in range(n+1):
  print("you rolled a: ", roll_dice())