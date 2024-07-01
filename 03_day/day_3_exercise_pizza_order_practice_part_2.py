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

bill = 0

# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if size == 'S':
    bill += 15
    if add_pepperoni == 'Y':
        bill += 2
        if extra_cheese == 'Y':
            bill += 1
            print(f"Your final bill is: ${bill}.")
        else:
            print(f"Your final bill is: ${bill}.")
    elif add_pepperoni == 'N':
        if extra_cheese == 'Y':
            bill += 1
            print(f"Your final bill is: ${bill}.")
        else:
            print(f"Your final bill is: ${bill}.")
elif size == 'M':
    bill += 20
    if add_pepperoni == 'Y':
        bill += 3
        if extra_cheese == 'Y':
            bill += 1
            print(f"Your final bill is: ${bill}.")
        else:
            print(f"Your final bill is: ${bill}.")
    elif add_pepperoni == 'N':
        if extra_cheese == 'Y':
            bill += 1
            print(f"Your final bill is: ${bill}.")
        else:
            print(f"Your final bill is: ${bill}.")
elif size == 'L':
    bill += 25
    if add_pepperoni == 'Y':
        bill += 3
        if extra_cheese == 'Y':
            bill += 1
            print(f"Your final bill is: ${bill}.")
        else:
            print(f"Your final bill is: ${bill}.")
    elif add_pepperoni == 'N':
        if extra_cheese == 'Y':
            bill += 1
            print(f"Your final bill is: ${bill}.")
        else:
            print(f"Your final bill is: ${bill}.")
