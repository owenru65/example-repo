
def format_name(f_name, l_name):
  """Take a first and last name and format them so that 
  they are lower case except the first letter"""
  
  # Above is a docstring

  if f_name == "" or l_name == "":
    return "You didn't provide valide inputs"
  
  formatted_f_name = f_name.title()
  formatted_l_name = l_name.title()

  return f"{formatted_f_name} {formatted_l_name}"



first_name=""
last_name=""

first_name = input("Input first name: ")
last_name = input("Input last name: ")

formatted_full_name = format_name (first_name, last_name)
print(formatted_full_name)

# put function inside print call.
print(format_name("aNgElA", "yU"))

print()










