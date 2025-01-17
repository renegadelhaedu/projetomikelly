from flask import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/verificar', methods=['POST'])
def ver():
    nome = request.form.get('nome')

    if nome == 'mikelly':
        return '<h1>voce é aluna da turma do 3 ano</h1>'
    elif nome == 'rene':
        return '<h1>mikelly detesta vc</h1>'
    else:
        return '<h1>voce nao é Mikelly</h1>'

if __name__ == '__main__':
    app.run()