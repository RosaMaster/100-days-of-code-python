# Multiplas condições
# if condition1 & condition2 & condition3


# Multiplas condições

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill += 5
        print(f"Child tickets are ${bill}.")
    elif age <= 18:
        bill += 7
        print(f"Youth tickets are ${bill}.")
    elif age >= 45 and age <= 55:
        print(f"Everithinf is going to be ok. Have a free ride on us!")
    else:
        bill += 12
        print(f"Adult tickets are ${bill}.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        # Add $3 to their bill
        bill += 3
        print(f"Your final bill is ${bill}")
    else:
        print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride!")
