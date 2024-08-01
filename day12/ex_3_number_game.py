
from art import logo
import os, random

os.system ('clear')
print(logo)
print("Welcome to the number guessing game!")

play_game = True

while play_game:
  print("I'm thinking of a number between 1 and 100")
  mode = input("Choose a difficulty (hard/easy): ")
  if mode == "hard":
    attempts = 5
  else:
    attempts = 10

  computer_random_number = random.randint(1,100)
  print(f"Comp = {computer_random_number}")
  while attempts > 0:
    print(f"You have {attempts} remaining to guess the number ")
    user_guess = int(input("Make a guess: "))
    if user_guess < 1 or user_guess > 100:
      print("Your guess is out of range.")
      continue

    if user_guess == computer_random_number:
      print(f"You got it - the answer was {computer_random_number}")
      break
    elif user_guess < computer_random_number:
      print("Too low")
    else:
      print("Too high")

    attempts -= 1
    if attempts == 0:
      print("You lose\n")
    else:
      print("Guess again")
  

  reply = input("Play again(y/n): ")
  if reply == "n":
    play_game = False
  else:
    os.system ('clear')





  







