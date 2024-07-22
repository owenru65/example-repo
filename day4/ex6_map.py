line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

input1Str= str(position[0])
input2=int(position[1])
print(f"{input1Str} - {input2}")

if input1Str == "A":
  input1 = 0
elif input1Str == "B":
  input1 = 1
else:
  input1 = 2

print(f"{input1} - {input2}")

input2 -= 1

map [input2][input1] = "X"




# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")