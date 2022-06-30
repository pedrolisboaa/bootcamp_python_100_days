def numero_secreto():
    from random import randint
    return randint(1, 100)


def dificuldade(resposta):
    if resposta == 'facil':
        return 10
    return 5


def jogo(numero, total_de_vidas, numero_secreto):
    if numero > numero_secreto:
        return f'O número secreto é menor! Você ainda tem {total_de_vidas} vidas.'
    if numero < numero_secreto:
        if total_de_vidas == 0:
            return f'Você perdeu!!!!'
        return f'O número secreto é maior! Você ainda tem {total_de_vidas} vidas.'
    return False
