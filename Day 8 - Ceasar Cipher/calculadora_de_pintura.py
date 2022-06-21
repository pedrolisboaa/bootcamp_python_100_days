def calcular_qtd_latas(altura, largura):
    from math import ceil
    return ceil(altura * largura / 5)


altura_parede = float(input('Informe a altura da parede: '))
largura_parede = float(input('Informe a largura da parede:  '))

print(f'Você deve comprar {calcular_qtd_latas(altura_parede, largura_parede)} latas.')
