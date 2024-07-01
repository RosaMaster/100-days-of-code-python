# Calculator Love

print("Welcome to the LOVE CALCULATOR!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_name1 = str.lower(name1)
lower_name2 = str.lower(name2)

combined_string = lower_name1 + lower_name2

t = combined_string.count("t")
r = combined_string.count("r")
u = combined_string.count("u")
e = combined_string.count("e")

true = t + r + u + e

l = combined_string.count("l")
o = combined_string.count("o")
v = combined_string.count("v")
e = combined_string.count("e")

love = l + o + v + e

love_score = str(true) + str(love)

score = int(love_score)

if (score < 10) or (score > 90):
    print(f"Your love score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

##### ------------------ #####
# RESOLUÇÃO PROPOSTA

# # 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# name = name1 + name2
# lower_name = name.lower()
# t = lower_name.count("t")
# r = lower_name.count("r")
# u = lower_name.count("u")
# e = lower_name.count("e")

# true = t + r + u + e

# l = lower_name.count("l")
# o = lower_name.count("o")
# v = lower_name.count("v")
# e = lower_name.count("e")

# love = l + o + v + e
# true_love = str(true) + str(love)
# true_love = int(true_love)

# if (true_love < 10) or (true_love > 90):
#   print(f"Your score is {true_love}, you go together like coke and mentos.")
# elif (true_love >= 40) and (true_love <= 50):
#   print(f"Your score is {true_love}, you are alright together.")
# else:
#   print(f"Your score is {true_love}.")