# 🚨 Don't change the code below 👇
age = input("What is your current age?")

# 🚨 Don't change the code above 👆

#Write your code below this line 👇
year = 90 - int(age)
months = round(year * 12)
weeks = round(year * 52)
days = round(year * 365)

print(f"You have {days} days, {weeks} weeks, and {months} months left")