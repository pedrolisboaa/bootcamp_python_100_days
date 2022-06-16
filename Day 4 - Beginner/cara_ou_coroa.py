def jogar_moeda():
    from random import choice
    return choice(['cara', 'coroa'])

cara = 0
coroa = 0
for _ in range(10):
    jogada = jogar_moeda()
    print(jogada)
    if jogada == 'cara':
        cara += 1
    else:
        coroa += 1

print(f'Ao todo foram {cara} caras.')
print(f'Ao todo foram {coroa} coroas.')