programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again.",
  "Loop":"Looping",
  123:"XXX"
}


print(programming_dictionary["Bug"])
print(programming_dictionary[123])
print(programming_dictionary["Loop"])


# add new items to dictionary

programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary["Loop"])

print()
print(programming_dictionary)

empty_list = []  # shown for reference
empty_dictionary = {}

# # Wipe an existing dictionary
# programming_dictionary = {}
# print()
# print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"

print()
print(programming_dictionary)
print()

# Loop through a dictionary
for key in programming_dictionary:
  print(key)

print()
for key in programming_dictionary:
  print(programming_dictionary[key])
  






