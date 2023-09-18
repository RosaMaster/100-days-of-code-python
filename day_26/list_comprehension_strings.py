
list_name = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]

new_list_upper = [name.upper() for name in list_name]
print(new_list_upper)

new_list_hi = [f"Hi {name}" for name in list_name]
print(new_list_hi)

name = "Angela"

letter_list = [letter for letter in name]
print(letter_list)