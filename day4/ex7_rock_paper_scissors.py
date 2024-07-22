import random

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

rps = [ rock, paper, scissors ]
r=0
p=1
s=2

#Write your code below this line 
your_choice=int(input("\n\n\nWhat do you choose? Type 0 for rock, 1 for paper and 2 for scissors: "))

print ( rps [your_choice] )

print("\nComputer chose:\n")

rps_comp = random.randint (0,2)

print ( rps [rps_comp] )

if your_choice == rps_comp:
  print("You draw")
elif your_choice == r and rps_comp == p:
  print("You lose")
elif your_choice == r and rps_comp == s:
  print("You win")
elif your_choice == s and rps_comp == r:
  print("You lose")
elif your_choice == s and rps_comp == p:
  print("You win")
elif your_choice == p and rps_comp == s:
  print("You lose")
elif your_choice == p and rps_comp == r:
  print("You win")
