from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return """
        <h1 style="text-align: center">Testando uma forma de escrever HTML</h1>
        <p> Mais é muito feio escrever tudo inline</p>
        <img src="https://toppng.com/uploads/preview/ramo-de-folha-11551057834ovgookcxcv.png" alt="logo instagram" width="200">
    """


@app.route('/contato')
def contato():
    return 'Essa é a página de contato.'


@app.route('/nome/<nome_usuario>')
def mostrando_nome(nome_usuario):
    return f'Seja bem vindo {nome_usuario.upper()}.'


@app.route('/completo/<nome>/<sobrenome>')
def mostrar_nome_completo(nome, sobrenome):
    return f'Ola {nome} {sobrenome}, tudo bem?'


@app.route('/conta/<nome>/<int:idade>')
def conta(nome, idade):
    return f'{nome}, tem {idade} anos.'


if __name__ == '__main__':
    app.run(debug=True)
