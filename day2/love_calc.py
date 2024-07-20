print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

name1=name1.lower()
name2=name2.lower()

name=name1 + name2
#print (name)

true_count = name.count("t") + name.count("r") +name.count("u") +name.count("e")
#print(f"true - {true_count}")

love_count = name.count("l") + name.count("o") +name.count("v") +name.count("e")
#print(f"love - {love_count}")


score=str(true_count) + str(love_count)
score=int(score)

#print(f"Score = {score}")

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")




