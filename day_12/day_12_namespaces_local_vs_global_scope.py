################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


################### Local Scope ####################

def drink_potion():
  potion_strength = 2
  print(potion_strength)
  
drink_potion()
# Note que se realizar o print da variável fora da função da erro
# print(potion_strength)
# Isso se deve devido ao limite de usar apenas no ambiente interno da função


################### Global Scope ####################

player_health = 10


def drink_potion():
  potion_strength = 2
  print(potion_strength)
  
drink_potion()
print(player_health)


################### There is no Block Scope ####################


game_level = 3

def create_enemy():
  
  enemies = ["Skeleton", "Zombie", "Alien"]
  
  if game_level < 5:
    new_enemy = enemies[0]

  print(new_enemy)
  

################### Modifyng Global Scope ####################

enemies = 1

def increase_enemies():
  print(f"enemies inside function: {enemies}")
  return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")



################### Global Constantes ####################

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@rosa_master"

def calc():
  TWITTER_HANDLE
