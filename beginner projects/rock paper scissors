rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

print("Lets play Rock, Paper, Scissors!")
choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors. "))

if choice == 0:
  print(rock)
elif choice == 1:
  print(paper)
else:
  print(scissors)

print("Computer chose:")

random_num = random.randint(0,2)
if random_num == 0:
  print(rock)
elif random_num == 1:
  print(paper)
else: 
  print(scissors)

#if pick rock
if choice == 0:
  if random_num == 0:
    print("It's a tie.")
  if random_num == 1:
    print("You lose.")
  elif random_num == 2:
    print("You win!")

#if pick paper
if choice == 1:
  if random_num == 1:
    print("It's a tie.")
  elif random_num == 2:
    print("You lose.")
  elif random_num == 0:
    print("You win!")

# if pick scissors
if choice == 2:
  if random_num == 2:
    print("It's a tie.")
  elif random_num == 0:
    print("You lose.")
  elif random_num == 1:
    print("You win!")
