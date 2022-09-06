from flask import Flask, render_template
from random import randint
from datetime import datetime
from api import retornar_idade, retornar_sexo, retornar_todos_post

meu_site = Flask(__name__)


@meu_site.route("/")
def index():
    numero_aleatorio = randint(0, 100)
    nome_completo = 'pedro lisboa'
    ano_atual = datetime.now().year
    return render_template(
        'index.html',
        numero=numero_aleatorio,
        nome=nome_completo,
        ano_atual=ano_atual
    )


@meu_site.route("/pergunta/<nome>")
def pergunta(nome):
    nome = nome
    sexo = retornar_sexo(nome)
    idade = retornar_idade(nome)
    return (render_template(
        'pergunta.html',
        nome=nome,
        sexo=sexo,
        idade=idade))


@meu_site.route("/blog")
def blog():
    posts = retornar_todos_post()
    return render_template('blog.html', posts=posts)


if __name__ == '__main__':
    meu_site.run(debug=True)
