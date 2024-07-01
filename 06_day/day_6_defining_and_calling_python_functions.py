# Functions disponiveis no python
# Link: https://docs.python.org/3/library/functions.html

print("Print é o exemplo de função de impressão.") #Usada para imprimir no Terminal

#Criando a propria função

def my_function():
    print("Hello")
    print("Bye")

my_function() # Para executar a função é necessário realizar a chamada da mesma

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
for step in range(6):
    way()
