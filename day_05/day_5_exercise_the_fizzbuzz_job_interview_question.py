#Write your code below this row 👇

for number in range(1, 101):
    if (number % 3 == 0) & (number % 5 == 0):
        print("FizzBuzz")
    elif (number % 3 == 0) & (number % 5 != 0):
        print("Fizz")
    elif (number % 3 != 0) & (number % 5 == 0):
        print("Buzz")
    else:
        print(number)
        
# Resolução

# for number in range(1, 101):
#     if number % 3 == 0 & number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)