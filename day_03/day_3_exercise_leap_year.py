year = int(input("Informe o ano a verificar: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"O ano {year} é bissexto.")
        else:
            print(f"O ano {year} não é bissexto.")
    else:
        print(f"O ano {year} é bissexto.")
else:
    print(f"O ano {year} não é bissexto.")


# Resolução Proposta
# # 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")
