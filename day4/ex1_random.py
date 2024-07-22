import random
import my_module  # local in my current dir.

random_integer = random.randint (1,10)

print(random_integer)
print("")
print(my_module.pi)

random_float=random.random()   # 0.000000 to 0.999999999
print(random_float)
print("")

love_score = random.randint(1,100)
print(f"Your love score is {love_score}\n")

