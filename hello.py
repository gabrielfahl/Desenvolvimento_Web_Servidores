from flask import Flask, render_template,request, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Chave forte'
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(FlaskForm):
    name = StringField('qual seu nome?', validators=[DataRequired()])
    Submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            Flask('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))

@app.route('/user/<name>/<prontuario>/<instituicao>')
def user(name, prontuario, instituicao):
    return render_template('user.html', name=name,prontuario=prontuario, instituicao=instituicao)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/contextorequisicao/<name>')
def contextorequisicao(name):
    user_agent = request.headers.get('User-Agent') 
    remote_ip = request.remote_addr  
    host = request.host  

    return render_template('contexto.html', name=name, user_agent=user_agent, remote_ip=remote_ip, host=host)

if __name__ == '__main__':
    app.run(debug=True)