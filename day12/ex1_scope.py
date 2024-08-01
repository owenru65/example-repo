################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Global scope
player_health = 10

# local scope
def drink_potion():
  potion_strength = 2
  print(potion_strength)   # local scope
  print(player_health)     # global scope

drink_potion()
# print(potion_strength)  Not in scope outside function

def game():
  def drink_potion2():
    potion_strength = 2
    print(potion_strength)   # local scope
    print(player_health)     # global scope
  
  drink_potion2()

# drink_potion2()  # Call fails as function only in local scope inside game() function

game()