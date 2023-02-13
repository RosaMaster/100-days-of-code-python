# Definindo casas decimais e arredondando resultado

from tkinter import scrolledtext


x = (8 / 3)

print(x)

print(round(x)) # Valor arredondado

print(round(x, 4)) # valor com 4 casa decimais


# Divisão pr 2

resultado = 4 / 2
resultado /= 2
print(resultado) # note que o resultado foi divido novamente por 2

div = 30 / 2
div /= 3 # note que o resutado foi divido por 3 na segunda vez
print(div)

# user scores a point

score = 0
score = score + 1 # OU score += 1
print(score)

score = 0
score = score - 1 # OU score -= 1
print(score)

score = 2
score = score * 3 # OU score *= 3
print(score)

score = 15
score = score / 3 # OU score *= 3
print(score)

# Exemplo  F String

score = 0
height = 1.8
isWinning = True

print(f"your score is {score} and height is {height} = {isWinning}")