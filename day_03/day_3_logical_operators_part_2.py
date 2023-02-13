# Multiplas condições
# if condition1 & condition2 & condition3


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

if size == 'S' and add_pepperoni == 'Y' and extra_cheese == 'Y':
    bill += 18
elif size == 'S' and add_pepperoni == 'Y' and extra_cheese == 'N':
    bill += 17
elif size == 'S' and add_pepperoni == 'N' and extra_cheese == 'Y':
    bill += 16
elif size == 'S' and add_pepperoni == 'N' and extra_cheese == 'N':
    bill += 15
elif size == 'M' and add_pepperoni == 'Y' and extra_cheese == 'Y':
    bill += 24
elif size == 'M' and add_pepperoni == 'Y' and extra_cheese == 'N':
    bill += 23
elif size == 'M' and add_pepperoni == 'N' and extra_cheese == 'Y':
    bill += 21
elif size == 'M' and add_pepperoni == 'N' and extra_cheese == 'N':
    bill += 20
elif size == 'L' and add_pepperoni == 'Y' and extra_cheese == 'Y':
    bill += 29
elif size == 'L' and add_pepperoni == 'Y' and extra_cheese == 'N':
    bill += 28
elif size == 'L' and add_pepperoni == 'N' and extra_cheese == 'Y':
    bill += 26
elif size == 'L' and add_pepperoni == 'N' and extra_cheese == 'N':
    bill += 25


print(f"Your final bill is: ${bill}.")