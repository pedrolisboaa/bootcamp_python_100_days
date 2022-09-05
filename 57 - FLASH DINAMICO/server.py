from flask import Flask, render_template
from random import randint
from datetime import datetime

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


if __name__ == '__main__':
    meu_site.run(debug=True)
