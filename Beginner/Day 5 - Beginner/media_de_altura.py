altura_estudantes = input('Informe a altura dos estudantes: ').split()
altura_estudantes_float = sum([float(x) for x in altura_estudantes]) / len(altura_estudantes)

print(f'A altura média da turma é {altura_estudantes_float:.2f}m.')



