# ERRO COMUM: Traceback (most recent call last):
#   File "main.py", line 38, in <module> char_list[100]
#   IndexError: list index out of range
# A solicitação do index esta fora da quantidade de itens na lista
# exemplo: print(states_of_america[100]) - sendo  que o index vai de [0] ate [49] - correto seria print(states_of_america[49])

import random

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", 
"Maryland", "South Carolina", "New Hampshira", "Virginia", "New York", "North Carolina", "Rhode Island", 
"Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississipi", "Illinois", "Alabama", "Maine", 
"Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Winsconsin", "Calidornia", "Minnesota", "Oregon", 
" Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", 
"Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(len(states_of_america))
print(states_of_america)

# Lista com Frutas e vegetais
# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", 
# "Pears", "Tomatoes", "Celery", "Potatoes"]

# Lista com duas listas aninhadas

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)

