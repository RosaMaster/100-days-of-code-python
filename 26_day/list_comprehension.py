numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)

new_list_01 = []

for n in numbers:
    add_1 = n + 1
    new_list_01.append(add_1)
    
print(new_list_01)


### Compression List

new_list_02 = [n + 10 for n in numbers]
print(new_list_02)


