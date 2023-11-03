import random
num = random.randint(1,100)
# print(num)

def easy():
  i = 10
  

  for x in range(0, i):
    guess = int(input(f"You have {i} attempts remaining to guess the number\nMake a guess: "))
    if guess > num:
      print("Too High!")
    if guess<num:
      print("Too Low!")
    if guess == num:
      print(f"You Got it. The number is {num}")
      break
    if i == 0:
      print("You are run out og the Game.")
      break
    
def hard():
  i = 5
  #i -= 1

  for x in range(0, i):
    guess = int(input(f"You have {i} attempts remaining to guess the number\nMake a guess: "))
    if guess > num:
      print("Too High!")     
    if guess<num:
      print("Too Low!")
    if guess == num:
      print(f"You Got it. The number is {num}")
      break
    if i == 0:
      print("You are run out og the Game.")
      break

from art import logo  

step1 = input("Welcome to Number Guessing Game!\nI'm thinking of a number between 1 & 100.\nChoose a difficulty. Type 'easy' or 'hard': ")

if step1 == 'easy':
  easy()

elif step1 == 'hard':
  hard()