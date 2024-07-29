def greet():
  print("Hello")
  print("How do you do")
  print(f"Nice weather")
  
greet()
        
def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How do you do {name}")
  print("Nice weather")
  name="Bob"
  print(name)

name="Russell"
greet_with_name(name)
print(name)
print()

# Functions with more than 1 input
def greet_with (name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}")
  
print()

greet_with("Russell", "Harpenden")
print()


greet_with(location="Harpenden", name="Russell" )
