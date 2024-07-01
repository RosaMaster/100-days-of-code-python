import os
import random
#from replit import clear
from art import logo

clear = lambda: os.system('cls')
bids = {}
bidding_finished = False
# lista de numeros possiveis para fazer pares para chegar a 21
#Fique atento na hora de escolher a carta que irá descartar para formar 21 pontos e não ultrapassar esse valor.
def cartao_negocios():
  """
    Retorna uma carta aleatória do baralho. 
    10 Rainha 10 Rei 10 Valete 11 Ás ou 1
  """
  cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  cartao = random.choice(cartas)
  return cartao


def calcula_score(cartas):
  """Pegue uma lista de cartas e retorne a pontuação calculada a partir das cartas"""

  if sum(cartas) == 21 and len(cartas) == 2:
    return 0
  if 11 in cartas and sum(cartas) > 21:
    cartas.remove(11)
    cartas.append(1)
  return sum(cartas)


def compare(usuario_score, computador_score):
  if usuario_score > 21 and computador_score > 21:
    return "Você foi até lá. Você perdeu 😤"
  if usuario_score == computador_score:
    return "Empate 🙃"
  elif computador_score == 0:
    return "Perdeu, oponente tem 21😱"
  elif usuario_score == 0:
    return "Ganhe com um 21 😎"
  elif usuario_score > 21:
    return "Não foi desta vez!!!"
  elif computador_score > 21:
    return "O oponente foi até lá. Você ganha 😁"
  elif usuario_score > computador_score:
    return "Você ganhou 😃"
  else:
    return "Você perdeu 😤"


def play_game():

  print(logo)
  usuario_cartas = []
  computador_cartas = []
  e_game_over = False

  for _ in range(2):
    usuario_cartas.append(cartao_negocios())
    computador_cartas.append(cartao_negocios())

  while not e_game_over:
    usuario_score = calcula_score(usuario_cartas)
    computador_score = calcula_score(computador_cartas)
    print(f"   Suas cartas: {usuario_cartas}, atual score: {usuario_score}")
    print(f"   Primeiro cartão do computador: {computador_cartas[0]}")

    if usuario_score == 0 or computador_score == 0 or usuario_score > 21:
      e_game_over = True
    else:
      user_should_deal = input("Digite 's' para obter outro cartão, digite 'n' para passar: ")
      if user_should_deal == "s":
        usuario_cartas.append(cartao_negocios())
      else:
        e_game_over = True

  while computador_score != 0 and computador_score < 17:
    computador_cartas.append(cartao_negocios())
    computador_score = calcula_score(computador_cartas)

  print(f"   Sua mão final: {usuario_cartas}, final score: {usuario_score}")
  print(f"   Mão final do computador: {computador_cartas}, final score: {computador_score}")
  print(compare(usuario_score, computador_score))


while input("Você quer jogar 21? Digite 's' ou 'n': ") == "s":
  clear()
  play_game()

