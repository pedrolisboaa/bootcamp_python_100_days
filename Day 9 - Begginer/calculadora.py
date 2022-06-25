from art import logo
from operacoes import *
print(logo)

n1 = float(input('Informe o primeiro número: '))
while True:
    op = input('Informe a operação desejada:\n +\n -\n *\n /\n ')
    n2 = float(input('Informe o segundo número: '))
    resultado_final = operacao(op, n1, n2)
    
    print(f'O resultado de {n1} {op} {n2} == {resultado_final}')

    if input('Deseja continuar com o resultado? [S]im [N]ão: ').upper() == 'N':
        break
    n1 = resultado_final

print(f'Fim da calculadora!')
    
    