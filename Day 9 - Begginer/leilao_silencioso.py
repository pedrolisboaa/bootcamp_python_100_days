from art import logo
import os

print(logo)

lances = {

}
print(f'Bem vindo ao leilão secreto!!!')

while True:
    nome_pessoa = input('Qual seu nome? ').strip()
    lance_pessoa = float(input('Informe seu lance: R$'))
    lances[nome_pessoa] = lance_pessoa

    nova_pessoa = input('Deseja adicionar mais lances? [S]im ou [N]ão: ').upper()
    if nova_pessoa == 'N':
        break
    os.system('cls')


maior_lance = 0
nome_campeao = ''
for chave, valor in lances.items():
    if valor > maior_lance:
        maior_lance = valor
        nome_campeao = chave

print(f'Quem levou o item foi {nome_campeao.upper()} com lance de R$ {maior_lance:.2f}')

