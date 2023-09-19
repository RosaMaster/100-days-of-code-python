# Instruções
# Você escreverá uma compreensão de lista para criar uma nova lista chamada result. Esta nova lista deverá conter apenas os números pares da lista numbers.

# NÃO modifique a lista numbersdiretamente. Tente usar List Comprehension em vez de Loop .

# Exemplo de saída
# [2, 8, 34]
# Dica
# Use o método de palavras-chave para iniciar a compreensão da Lista e preencha as partes relevantes.
# Os números pares podem ser divididos por 2 sem resto.
# Lembre-se de como funciona o operador módulo.
# Teste seu código
# Verifique se seu código está fazendo o que deveria. Quando estiver satisfeito com seu código, clique em enviar para verificar sua solução.

# Solução
# https://repl.it/@appbrewery/day-26-2-solution


numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

#Write your 1 line code 👇 below:
result = [number for number in numbers if number % 2 == 0]


#Write your code 👆 above:

print(result)