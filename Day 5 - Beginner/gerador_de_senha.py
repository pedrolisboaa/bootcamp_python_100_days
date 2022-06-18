import string
from random import choices, shuffle

LETRAS = list(string.ascii_letters)
NUMEROS = list(string.digits)
CARACTERES = list(string.punctuation)

print(f'Bem vindo ao gerador de senhas!!')
qtd_letras = int(input('Informe quantas letras sua senha deve ter: '))
qtd_numeros = int(input('Informe quantos números deve ter sua senha: '))
qtd_caracteres = int(input('Informe quantos caracteres deve ter sua senha: '))

nova_senha = [*choices(LETRAS, k=qtd_letras), *choices(NUMEROS, k=qtd_numeros), *choices(CARACTERES, k=qtd_caracteres)]
shuffle(nova_senha)
senha_completa = "".join(nova_senha)
print(senha_completa)



