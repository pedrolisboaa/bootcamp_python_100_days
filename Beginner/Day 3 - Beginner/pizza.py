# Precos

preco = 0

print(f'Bem vindo a pizzaria!')
tamanho = input('Informe o tamanho da sua pizza? [P], [M], [G]: ').upper()

if tamanho == 'P':
    preco += 15
elif preco == 'M':
    preco += 20
else:
    preco += 25

calabresa = input('Gostaria de adicionar Calabresa? [S] / [N]: ').upper()
if calabresa == 'S':
    if tamanho == 'P':
        preco += 2
    else:
        preco += 3

queijo = input('Gostaria de adicionar queijo? [S] / [N]: ').upper()
if queijo == 'S':
    preco += 1

print(f'O preço total ficou em R$ {preco}')