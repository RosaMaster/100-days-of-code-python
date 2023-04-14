from product import MENU

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "tea": 20,
    "chocolate": 40,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Desculpe, mas não temos {item}.")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Por favor insira a moeda.")
    total = int(input("Quantas moedas de R$ 1,00 ?: ")) * 1.0
    total += int(input("Quantas moedas de R$ 0,50 ?: ")) * 0.5
    total += int(input("Quantas moedas de R$ 0,25 ?: ")) * 0.25
    total += int(input("Quantas moedas de R$ 0,10 ?: ")) * 0.10
    total += int(input("Quantas moedas de R$ 0,05 ?: ")) * 0.05
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Aqui está R$ {change:.2f} de troco.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Desculpe, isso não é dinheiro suficiente. Dinheiro devolvido.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Aqui está seu {drink_name} ☕️. Aproveite!")


is_on = True

while is_on:
    choice = input("​Qual bebida você escolhe? (tea/milk/espressocurto/espressolongo/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"tea: {resources['tea']}g")
        print(f"chocolate: {resources['chocolate']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
