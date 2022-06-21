from random import choice

# Gerando a palavra secreta
banco_palavras = ['banana', 'pera', 'uva', 'goiaba']
palavra_escolhida = choice(banco_palavras)
print(palavra_escolhida)

# Criando o sublinhado
palavra_secreta = []
for letra in palavra_escolhida:
    palavra_secreta.append('_')

letra_jogador = input('Informe uma letra: ').lower()



