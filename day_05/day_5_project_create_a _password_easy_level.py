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

#EASY LEVEL - exemplo fghf^&23
password = ""

for char in range(1,number_caracter + 1):
    random_char = random.choice(letters)
    password += random_char
    print(random_char)
for symbol in range(1,number_symbol + 1):
    random_symbol = random.choice(symbols)
    password += random_symbol
    print(random_symbol)
for number in range(1,number_number + 1):
    random_number = random.choice(numbers)
    password += random_number
    print(random_number)

print(f"Here is your password: {password}")