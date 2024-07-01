# bilhete para altura maior que 180cm e bilhete por $7 para < 18 e $12 para > 18

height = int(input("Informe a altura: "))
age = int(input("Informe sua idade: "))
if height > 120:
    if age >= 18:
        print("You can ride in rollercoaster, please pay $12")
    else:
        print("You can ride in rollercoaster, please pay $7")
else:
    print("Sorry, you have to grow taller before you can ride!")


# Resolução proposta

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride!")

    