from flask import Flask, request, make_response, redirect, abort

app = Flask(__name__)

@app.route('/')
def hello_world():
    return f'<h1>Avaliação contínua: Aula 030</h1>' \
           f'<ul>' \
           f'<li><a href="/">Home</a></li>' \
           f'<li><a href="/user/Fabio%20Teixeira/PT23820X/IFSP">Identificação</a></li>' \
           f'<li><a href="/contextorequisicao">Contexto da requisição</a></li>' \
           f'</ul>'

@app.route('/user/<name>/<register>/<institution>')
def user(name, register, institution):
    return f'<h1>Avaliação contínua: Aula 030</h1>' \
           f'<h1>Aluno: {name}</h1>' \
           f'<h1>Prontuário: {register}</h1>' \
           f'<h1>Instituição: {institution}</h1>' \
           f'<a href="/">Voltar</a>'

@app.route('/contextorequisicao')
def contexto_requisicao():
    browser = request.headers.get('User-Agent')
    ip = request.remote_addr
    host = request.headers.get('Host')
    return '<h1>Avaliação Contínua: Aula 030</h1>' \
           '<h1>Seu navegador é: {}</h1>' \
           '<h1>O IP do computador remoto é: {}</h1>' \
           '<h1>O host da aplicação é: {}</h1>' \
           '<a href="/">Voltar</a>'.format(browser, ip, host)  

if __name__ == '__main__':
    app.run(debug=True)
