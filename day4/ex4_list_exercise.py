
import random
names = ['Angela', 'Ben', 'Jenny', 'Michael', 'Chloe']

# You are working in a team of developers.
# Another developer has written the code to import the names in the inputs
# You can run the code to see what this names list looks like.
# Then change the names in the input to see how it imports the names.
print(names)
# 🚨 Remember to remove the print statement above when you submit.

list_item_count = len(names)
#print(list_item_count)

random_payer = random.randint (0,list_item_count-1)
#print(random_payer)

print(f"{names[random_payer]} is going to buy the meal today!")



