from flask import Flask, render_template,request
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
   now = datetime.utcnow()
   return render_template('index.html', current_time=now)

@app.route('/user/<name>/<prontuario>/<instituicao>')
def user(name, prontuario, instituicao):
    return render_template('user.html', name=name,prontuario=prontuario, instituicao=instituicao)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/contextorequisicao/<name>')
def contextorequisicao(name):
    user_agent = request.headers.get('User-Agent')  # Informações do navegador
    remote_ip = request.remote_addr  # IP do usuário
    host = request.host  # Host da aplicação

    return render_template('contexto.html', name=name, user_agent=user_agent, remote_ip=remote_ip, host=host)

if __name__ == '__main__':
    app.run(debug=True)