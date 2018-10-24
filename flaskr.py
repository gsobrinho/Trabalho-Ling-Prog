# coding: utf-8

import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing

# configuração
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)


def conectar_bd():
    return sqlite3.connect(app.config['DATABASE'])

def criar_bd():
    with closing(conectar_bd()) as bd:
        with app.open_resource('esquemabanco.sql',mode='r') as sql:
            bd.cursor().executescript(sql.read())
        bd.commit()
criar_bd()

@app.before_request
def pre_requisicao():
    g.bd = conectar_bd()

@app.teardown_request
def encerrar_requisicao(exception):
    g.bd.close()

@app.route("/")
def inicial():
  return render_template("Initial.html")

@app.route("/formDoutorado")
def formDoutorado():
  return render_template("formDoutorado.html")


@app.route("/formMestrado")
def formMestrado():
  return render_template("formMestrado.html")

@app.route("/cadatroConcluido",methods=['GET', 'POST'])
def cadConcluido():
    pessoa = request.form
    #salve Pessoa no BD
    return render_template('visualizarPessoa.html', data=pessoa)
 


@app.route("/login", methods=['GET', 'POST'])
def login():
    erro = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Usuário inválido'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Senha inválida'
        else:
            session['logado'] = True
            flash('Login OK')
            #aki eu acho que já pode exibir o posLogin
            return redirect(url_for('exibir_entradas'))
    return render_template('login.html', erro=erro)



@app.route("/insDoutorado")
def inscDout():
    # dict com os dados de aluno de Doutorado 
    doutourado = {}
    return render_template("listarNomes.html", data=doutourado)
    
@app.route("/insMestrado")
def inscMest():
    # dict com os dados de aluno de Doutorado 
    mestrado = {}
    return render_template("listarNomes.html", data=mestrado)
    
if __name__ == "__main__":
    app.run(debug=True)


