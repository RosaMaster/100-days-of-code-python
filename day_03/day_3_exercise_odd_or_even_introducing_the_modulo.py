# Verificar par ou impar

number = int(input("Digite um numero: "))
resultado = number % 2
if resultado == 0:
    print("O numero é par!")
else:
    print("O número é impar!")


# Resolção proposta

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if number % 2 != 0:
    print("This is an odd number.")
else:
    print("This is an even number.")