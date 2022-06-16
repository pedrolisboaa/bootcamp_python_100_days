from random import choice

nomes = input(f'Informe o nome das pessoas, separando com uma "virgula": ')
lista_de_nomes = nomes.split(',')

print(f'{choice(lista_de_nomes)} foi o sorteado para pagar a conta!!')
