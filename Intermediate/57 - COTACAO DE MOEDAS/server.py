from flask import Flask, render_template
from uteis import data_hora
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html', da_hr=data_hora.AGORA)


if __name__ == '__main__':
    app.run(debug=True)
