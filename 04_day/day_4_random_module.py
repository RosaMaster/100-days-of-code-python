# SITE: askpython.com

import random
import day_4_my_module

# Número inteiro
random_integer = random.randint(1, 10)
print(random_integer)

# Número Decimais
random_float = random.random()
print(random_float)

# Multiplicando o número aleatório
multi = random_float * 5
print(multi)

# Número Decimais
random_float_2 = random.uniform(0, 5)
print(random_float_2)

# importando varialvel de outro documento
print(f"{day_4_my_module.pi}")

# Utilizando seed()
random_seed = random.seed(1)
print(random_seed)

# get the state of the generator
state = random.getstate()
print(state)

# Gerando bits aleatorios
random_bit = random.getrandbits(32)
print(random_bit)

# exemplo_1
love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

# exemplo_2
sequence = [random.randint(0, i) for i in range(10)]
print(f'Antes de embaralhar {sequence}')

random.shuffle(sequence)
print(f'Após embaralhar {sequence}')

# exemplo_3 Escolher lista aleatoria
a = ['one', 'eleven', 'twelve', 'five', 'six', 'ten']
print(a)

for i in range(5):
    print(random.choice(a))

# exemplo_4 Love Score
love_score = random.randint(1, 100)
print(f'Your love score is {love_score}')
