peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

imc = round(peso / altura ** 2, 2)

print(f'Seu IMC é {imc}.')
if imc < 18.5:
    print('Abaixo do PESO')
elif imc <= 24.9:
    print('NORMAL')
elif imc <= 29.9:
    print('SOBREPESO')
elif imc <= 39.9:
    print('OBESIDADE')
else:
    print('OBESIDADE GRAVE.')