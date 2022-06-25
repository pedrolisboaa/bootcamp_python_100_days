

def adicao(x, y):
    return x + y


def subtracao(x, y):
    return x - y


def multiplicacao(x, y):
    return x * y


def divisao(x, y):
    return x / y


def operacao(operador, x, y):
    if operador == '+':
        return adicao(x, y)
    elif operador == '-':
        return subtracao(x, y)
    elif operador == '*':
        return multiplicacao(x, y)
    else:
        return divisao(x, y)