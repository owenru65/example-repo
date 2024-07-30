import os
from art import logo
os.system ('clear')

def get_largest_bid (bids):
  highest_bid_value = 0
  highest_bid_name = ""

  for key in bids:
    if bids[key] > highest_bid_value:
      highest_bid_value = bids[key]
      highest_bid_name = key
      
  print(f"The winner is {highest_bid_name} with a bid of ${highest_bid_value}")


print(logo)

new_bid = True
bid_dictionary = {}

while new_bid:
  name = input("What is your name? ")
  bid = int(input("What is your bid: $"))

  bid_dictionary[name] = bid

  reply = input("Are there any other bidders (yes/no): ")
  if reply == "no":
    new_bid = False
  else:
    os.system ('clear')


print (bid_dictionary)

get_largest_bid(bids = bid_dictionary)



