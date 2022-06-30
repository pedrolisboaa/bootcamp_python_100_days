from random import choice
from time import sleep
from imagens_pedra_papel_tesoura import *

LISTA = ['pedra', 'papel', 'tesoura']

print(f'Vamos jogar Pedra, Papel e Tesoura!')
print(f'Começando em....')
for _ in range(3):
    sleep(1)
    print(f'{3 - _}')

escolha_jogador = input(f'Faça sua escolha: Pedra , Papel ou Tesoura? ').lower()
escolha_computador = choice(LISTA)

if escolha_jogador == 'pedra' and escolha_computador == 'tesoura':
    print(f'Você jogou {escolha_jogador}{pedra} o computador jogou {escolha_computador}{tesoura}')
    print(f'VOCÊÊÊ GANHOUUU!')
elif escolha_jogador == 'tesoura' and escolha_computador == 'papel':
    print(f'Você jogou {escolha_jogador}{tesoura} o computador jogou {escolha_computador}{papel}')
    print(f'VOCÊÊÊ GANHOUUU!')
elif escolha_jogador == 'papel' and escolha_computador == 'pedra':
    print(f'Você jogou {escolha_jogador}{papel} o computador jogou {escolha_computador}{pedra}')
    print(f'VOCÊÊÊ GANHOUUU!')
elif escolha_jogador == escolha_computador:
    print(f'Você jogou {escolha_jogador} o computador jogou {escolha_computador}')
    print('Ixiiiiii deu empate!!')
else:
    print(f'Você jogou {escolha_jogador} o computador jogou {escolha_computador}')
    print('Ixiiiiii você perdeu!!')





