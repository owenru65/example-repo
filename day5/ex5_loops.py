
target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇

total=0

for number in range(0,target+1): 
  if number%2 ==0:
    #print(number)
    total += number
  
print(total)

# OR better
total=0
for number in range(2,target+1,2):
  total += number

print(total)

