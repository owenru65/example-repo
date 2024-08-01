import random
import os
from art import logo, vs
from game_data import data
# print (logo , vs, data, len(data))
random_numbers_chosen = []

def get_random_data():
  random_number = random.randint(0,49)
  while random_number in random_numbers_chosen:
    random_number = random.randint(0,49)

  random_numbers_chosen.append(random_number)
  # print(random_numbers_chosen)
  # print("Random numbers used: ", len(random_numbers_chosen))
  return data[random_number]

def display_data(info_dict):
  name = info_dict["name"]
  desc = info_dict["description"]
  country = info_dict["country"]
  ab=""

  if LOGO == "MAIN":
    print(logo)
    ab="A"
  else:
    print(vs)
    ab="B"

  print(f"Compare {ab}: {name}, {desc}, from {country}")
  
def compare_followers(counta, countb):
  # print(counta, countb)
  if counta > countb:
    return "A"
  else:
    return "B"
  
######################### MAIN ##################

play_game = True
user_score = 0

while play_game:
  data_a = get_random_data()
  data_b = get_random_data()

  LOGO="MAIN"
  display_data(data_a)
  LOGO="VS"
  display_data(data_b)

  user_answer = (input("Who has the more followers? Type A or B: ").upper())
  answer = compare_followers(data_a["follower_count"], data_b["follower_count"])

  if user_answer == answer:
    user_score += 1
    print(f"You are right!! Current score = {user_score}")
  else:
    print(f"Sorry - that's wrong. Final score = {user_score}")
    play_game = False
  





# name': 'Instagram',
#         'follower_count': 346,
#         'description': 'Social media platform',
#         'country': 'United States'



