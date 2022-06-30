def numero_primo(numero):
    for i in range(2, numero):
        if numero % i == 0:
            return 'não é primo'
    return 'é primo'


numero = int(input('Informe um número: '))
print(f'O {numero} {numero_primo(numero)}')

# Vei não estou acreditando que acertei isso!
