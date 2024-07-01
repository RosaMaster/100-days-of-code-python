# Exercício HURDLE 3
# Link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

def right():
    turn_left()
    turn_left()
    turn_left()
    
def up():
    turn_left()
    move()
    right()
    move()
    right()
    move()
    turn_left()
    
# INICIO
while not at_goal():
    if wall_in_front():
        up()
    else:
        move()