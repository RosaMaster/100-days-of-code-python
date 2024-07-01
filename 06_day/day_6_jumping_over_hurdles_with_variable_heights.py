# Exercício HURDLE 4
# link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json


def right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    while wall_on_right():
        move()
    right()
    move()
    right()
    move()
    while wall_on_right() & front_is_clear():
        move()
    turn_left()
    
# INICIO
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()