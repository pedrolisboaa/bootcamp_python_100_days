
print('Bem vindo a calculadora de gorjetas.')
total_conta = float(input('Informe o total da conta: '))
qtd_pessoas = int(
    input('Informe a quantidade de pessoas para dividir a conta? '))
prct = int(input('Informe quanto deseja deixar de gorjeta? 10, 12 ou 15? '))

pagamento = (total_conta / qtd_pessoas) + \
    (total_conta / qtd_pessoas) * (prct / 100)
print(f'O valor ficou R$ {round(pagamento, 2)} para cada.')
