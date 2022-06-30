notas_alunos = {
    'Pedro': 81,
    'Juliana': 78,
    'Olivia': 99,
    'Marcia': 74,
    'Kadyja': 64,
    'Patricia': 45,
    'Marcelo': 85,
    'Antonia': 73
}

for chave, valor in notas_alunos.items():
    if valor >= 91:
        print(f'{chave} - Outstanding')
    elif valor >= 81:
        print(f'{chave} - Exceeds Expectations')
    elif valor >= 71:
        print(f'{chave} - Acceptable')
    else:
        print(f'{chave} - Fail')