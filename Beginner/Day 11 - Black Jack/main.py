import random
import os
from art import logo
from random import choices, choice

CARTAS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

if input('Você gostaria de jogar 21? Escolha "s" ou "n": ').lower() == 's':
    os.system('cls')
    print(logo)

    # 1ª rodada
    cartas_jogador = choices(CARTAS, k=2)
    cartas_computador = choices(CARTAS, k=1)

    imprimir_cartas_jogador = f'Suas cartas: {cartas_jogador}'
    imprimir_cartas_computador = f'Cartas do computador: {cartas_computador}'

    print(imprimir_cartas_jogador)
    print(imprimir_cartas_computador)

    # Primeira rodada
    if input('Gostaria de mais uma carta? "s" ou "n": ').lower() == 's':
        cartas_jogador.insert(choice(CARTAS))
        cartas_computador.append(choice(CARTAS))

        print(imprimir_cartas_jogador)
        print(imprimir_cartas_computador)

else:
    print(f'Muito Obrigado!')
