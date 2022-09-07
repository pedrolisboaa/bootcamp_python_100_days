from flask import Flask

app = Flask(__name__)


@app.route('/')
def ola_mundo():
    return 'Olá mundo!'


@app.route('/teste')
def ola_teste():
    return 'Olá teste'


@app.route('/home')
def home():
    return """
    <h1> Está é minha HOME</h1>
    <h2>Testando o h2</h2>
    
    """



if __name__ == '__main__':
    app.run()
