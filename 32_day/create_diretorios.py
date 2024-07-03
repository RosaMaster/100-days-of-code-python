import os

# Cria 100 diretorios de 1 a 100

for i in range(280, 289):     # range de 1 a 100
    print(i)                # imprime o valor de i
    dir = f'./{i}_'         # cria a variavel dir com o valor de i
    os.mkdir(dir)           # cria o diretorio com o nome de dir

