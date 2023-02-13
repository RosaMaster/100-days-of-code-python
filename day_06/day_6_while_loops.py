# Laço FOR

# for item in list_of_itens:
    # Do something to each item
    
# for number in range(a, b):
    # print(number)
    
    
## LAÇO WHILE
    #while something_is_true
        # Do something repeatedly
        
# Exercício HURDLE 2 
# link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
        
def right():
    turn_left()
    turn_left()
    turn_left()

def way():
    move()
    turn_left()
    move()
    right()
    move()
    right()
    move()
    turn_left()
    
# INICIO
while not at_goal():
    way()