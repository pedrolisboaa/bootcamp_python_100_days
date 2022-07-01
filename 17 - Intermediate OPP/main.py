from jogo import Jogo
from perguntas import banco_de_perguntas

j = Jogo()
for i in range(len(banco_de_perguntas)):
    j.fazer_pergunta()
    j.mostrar_pontuacao()