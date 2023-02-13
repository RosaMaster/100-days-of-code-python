import random

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", 
"Maryland", "South Carolina", "New Hampshira", "Virginia", "New York", "North Carolina", "Rhode Island", 
"Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississipi", "Illinois", "Alabama", "Maine", 
"Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Winsconsin", "Calidornia", "Minnesota", "Oregon", 
" Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", 
"Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# print(states_of_america)

print(states_of_america[0])
print(states_of_america[5])

# Utilizando a lista em ordem descrescente

print(states_of_america[-1])
print(states_of_america[-3])

# Alterando um item

states_of_america[1] = "Pencilvania"
print(states_of_america[1])

# Acrescentando item

states_of_america.append("São Paulo")
print(states_of_america)

# Extendendo a lista com outra lista

states_of_america.extend(["Columbus", "Little Rock", "Las Vegas"])
print(states_of_america)

# ERRO se tentar usar append para incluir uma lista dentro de uma lista

states_of_america.append(["Rio", "Minas", "Acre"])
print(states_of_america)
print(states_of_america[-1]) # Note que o item é uma lista 

# Reverse list
print(states_of_america.reverse())