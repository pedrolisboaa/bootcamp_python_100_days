pontos = input('Informe o maiores scores: ').split()
pontos_numeral = []

for _ in pontos:
    pontos_numeral.append(float(_))

print(f'O maior número foi {max(pontos_numeral)}')
