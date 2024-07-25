#
# This code will not run. From reeborg.ca 
# 
# 
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()    
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()



for step in range(6):
    jump()

    ### OR

number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    print (number_of_hurdles)
    number_of_hurdles -= 1
