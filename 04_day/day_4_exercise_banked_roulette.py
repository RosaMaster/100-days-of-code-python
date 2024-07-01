import random


names = input("Informe os nomes da lista separados por [vírgula]: ")

names_list = names.split(",")
print(f"\n{names_list}")

# numero de itens na lista
x = len(names_list)
print(f"\n{x}")

# numero de caracteres no item
y = len(names_list[0])
print(f"\n{y}")

for i in range(1):
    print(f"\n{random.choice(names_list)}")

# Eduardo,Raquel,Gustavo,Felipe,Ricardo,Lucas,Pedro,Paulo,Monica,Camila


### PROPOSTO

# import random

# # Split string method
# names_string = input("Give me everybody's names, seperated by a comma. ")
# names = names_string.split(", ")

# #Write your code below this line 👇

# #Get the total number of items in list.
# num_items = len(names)
# #Generate random numbers between 0 and the last index. 
# random_choice = random.randint(0, num_items - 1)
# #Pick out random person from list of names using the random number.
# person_who_will_pay = names[random_choice]

# print(person_who_will_pay + " is going to buy the meal today!")