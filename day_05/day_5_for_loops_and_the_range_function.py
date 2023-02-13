# LAÇO RANGE
# for number in range(a, b)
#    print(number)

# Exemplo 1 - Definindo Range
for number in range(10):
    print(number)
print("******")
    
# Exemplo 2 - Definindo Intervalo for number in range(a, b)
for number in range(1, 10):
    print(number)
print("******")
    
# Exemplo 3 - Definindo Intervalo e degrau for number in range(a, b, c) 
for number in range(1, 100, 7):
    print(number)
print("******")

# Exemplo 4 - Somando valores de Range
total = 0
for number in range(1, 101):
    total += number
    print(number)
    print(total)
print(number)
print(total)
print("******")

# Exemplo 5 - Soma de Gauss
for number in range(1, 101):
    print(number)
total = (number * (number + 1)) / 2
print(total)
print("******")