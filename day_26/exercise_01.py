# Instruções
# Você escreverá uma compreensão de lista para criar uma nova lista chamada squared_numbers. Esta nova lista deve conter todos os números da lista numbers, mas cada número deve ser elevado ao quadrado.

# por exemplo 

# 4 * 4 = 16
# 4 ao quadrado é igual a 16.

# NÃO modifique a lista numbersdiretamente. Tente usar List Comprehension em vez de Loop .

# Exemplo de saída
# [1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]
# Dica
# Use o método de palavras-chave para iniciar a compreensão da Lista e preencha as partes relevantes.

# Certifique-se de que squared_numbersesteja impresso no console para que a verificação do código funcione.

# Teste seu código
# Verifique se seu código está fazendo o que deveria. Quando estiver satisfeito com seu código, clique em enviar para verificar sua solução.

# Solução
# https://repl.it/@appbrewery/day-26-1-solution


numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:
squared_numbers = [number * number for number in numbers]


#Write your code 👆 above:

print(squared_numbers)