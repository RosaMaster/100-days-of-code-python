import random

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade', 'Tony', 'Steve', 'Natasha']

names_age = {name: random.randint(20, 40) for name in names}

print(names_age)

filter_age = {name: age for (name, age) in names_age.items() if age >= 35}

print(filter_age)
