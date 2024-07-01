# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill.
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if size == 'S':
    if add_pepperoni == 'Y':
        if extra_cheese == 'Y':
            print("Your final bill is: $18.")
        else:
            print("Your final bill is: $17.")
    elif add_pepperoni == 'N':
        if extra_cheese == 'Y':
            print("Your final bill is: $16.")
        else:
            print("Your final bill is: $15.")
elif size == 'M':
    if add_pepperoni == 'Y':
        if extra_cheese == 'Y':
            print("Your final bill is: $24.")
        else:
            print("Your final bill is: $23.")
    elif add_pepperoni == 'N':
        if extra_cheese == 'Y':
            print("Your final bill is: $21.")
        else:
            print("Your final bill is: $20.")
elif size == 'L':
    if add_pepperoni == 'Y':
        if extra_cheese == 'Y':
            print("Your final bill is: $29.")
        else:
            print("Your final bill is: $28.")
    elif add_pepperoni == 'N':
        if extra_cheese == 'Y':
            print("Your final bill is: $26.")
        else:
            print("Your final bill is: $25.")
    