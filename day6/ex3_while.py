#  Note this code does not run - see
# https://www.udemy.com/course/100-days-of-code/learn/lecture/19115618#overview
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json


def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()

##############    
def jump():
    #move()    
    turn_left()
    
    while wall_on_right():
        move()
    
    turn_right()
    move()
    turn_right()
    move()
    
    while wall_on_right() and not wall_in_front():
        move()
        
    turn_left()
##################
    
while at_goal() != True:
    if wall_in_front():
        jump()
    else:
        move()
    
    
    

#for step in range(6):
 #   jump()