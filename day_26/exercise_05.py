# Instruções
# Você usará o Dictionary Comprehension para criar um dicionário chamado weather_fque pega cada temperatura em graus Celsius e a converte em graus Fahrenheit.

# To convert temp_c into temp_f:

# (temp_c * 9/5) + 32 = temp_f

# NÃO crie um dicionário diretamente. Tente usar o Dictionary Comprehension em vez de um Loop .

# Exemplo de saída
# {

# 'Monday': 53.6,

# 'Tuesday': 57.2,

# 'Wednesday': 59.0,

# 'Thursday': 57.2,

# 'Friday': 69.8,

# 'Saturday': 71.6,

# 'Sunday': 75.2

# }

# Dica
# Use o método de palavras-chave para iniciar a compreensão do Dicionário e preencha as partes relevantes.

# Você pode obter cada um dos itens de um dicionário usando o método .items(): https://www.w3schools.com/python/ref_dictionary_items.asp

# Solução
# https://repl.it/@appbrewery/day-26-5-solution


weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:
weather_f = {day: (temp * 9 / 5) + 32 for (day, temp) in weather_c.items()}

print(weather_f)
