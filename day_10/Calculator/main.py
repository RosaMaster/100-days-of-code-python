import os
from art import logo

# Calculator
#ADIÇÃO / ADD
def add(n1, n2):
    """Função de Adição"""
    return n1 + n2

# SUBTRAÇÃO / SUBTRACT
def subtract(n1, n2):
    """Função de Subtração"""
    return n1 - n2

# MULTIPLICAÇÃO / MULTIPLY
def multiply(n1, n2):
    """Função de Multiplicação"""
    return n1 * n2

# DIVISÃO / DIVIDE
def divide(n1, n2):
    """Função de Divisão"""
    return n1 / n2

# OPERADORES /OPERATIONS
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "sen" seno,
    "cos" cosseno,
    "tan" tangente,
}

# ENTRADA / INPUT
def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculator: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()