

enemies = 1

def increase_enemies():
  global enemies   # not great to use global
  enemies += 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Global constants
# Convention is to use upper case variable names.

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@russel_o"