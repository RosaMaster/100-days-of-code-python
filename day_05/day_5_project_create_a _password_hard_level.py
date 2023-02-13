# CREATE PASSWORD

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("WELCOME TO THE PYPASSWORD GENERATOR!\n")
number_caracter = int(input("How many letters would you like in your password?\n"))
number_symbol = int(input("How many symbols would you like in your password?\n"))
number_number = int(input("How many numbers would you like in your password?\n"))

#HARD LEVEL - exemplo g^H2kw8&
password_list = []

for char in range(1,number_caracter + 1):
    password_list.append(random.choice(letters))
    
for symbol in range(1,number_symbol + 1):
    password_list.append(random.choice(symbols))
    
for number in range(1,number_number + 1):
    password_list.append(random.choice(numbers))
    
print(f"Here is your password: {password_list}")
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char
    
print(f"Your password is: {password}")