from perguntas import banco_de_perguntas


class Jogo:
    def __init__(self):
        self.numero_pergunta = 0
        self.pontuacao = 0
        self.pergunta = 0
        self.resposta = 0

    def fazer_pergunta(self):
        pergunta_partida = banco_de_perguntas[self.numero_pergunta]['text']
        resposta_partida = banco_de_perguntas[self.numero_pergunta]['answer']

        resposta = input(f"Q.{self.numero_pergunta + 1} {pergunta_partida} (True / False):? ")
        if resposta == resposta_partida:
            self.pontuacao += 1
            print(f'Parabéns você acertou!')
        else:
            print(f'Que pena você errou!')

        self.numero_pergunta += 1

    def mostrar_pontuacao(self):
        print(f'Total de pontos {self.pontuacao}/12')
