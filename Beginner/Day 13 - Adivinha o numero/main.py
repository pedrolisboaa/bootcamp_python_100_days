from art import logo
from funcoes import *

numero_secreto = 50  # numero_secreto()

print(logo)
print(f'Você deve escolhar uma número entre 1 e 100:')

if input('Escolha a dificuldade, [f]acil ou [d]ificil? ').lower() == 'facil':
    total_vidas = dificuldade('facil')
else:
    total_vidas = dificuldade('dificil')

while total_vidas > 0:
    total_vidas -= 1
    numero = int(input('Informe um número: '))

    resultado = jogo(numero, total_vidas, numero_secreto)
    if not resultado:
        print(f'Você acertou o número {numero_secreto}!! Você ainda tinha {total_vidas} vidas.')
        break
    else:
        print(resultado)

print(f'Fim de Jogo!')
