# coding: utf-8

import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing

# configuração
DATABASE = '/tmp/Testeflask.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)

pessoa ={}
pessoa["Nome"] = "Ana Mendes Sobrinho"
pessoa["Linha De Pesquisa"] = "Sistemas Complexos Adaptativos"
pessoa["NomePai"]="Sanderson Sobrinho" 
pessoa["NomeMae" ]="Valeria Cristina Mendes" 
pessoa["CPF" ]="12445532355" 
pessoa["Sexo"]="Feminino"
pessoa["Nacionalidade"]= "Estrangeiro"
pessoa["AnoChegada"]= "XXXX"
pessoa["Pais"]= "Acre"

pessoa["Logradouro" ]="Rua sem nome"
pessoa["NumeroCasa" ]="2012"
pessoa["Complemento" ] = ""
pessoa["Bairro" ]="Anchovas"
pessoa["Cidade"] = "Rio de Japeri"
pessoa["UF" ]="RJ" 
pessoa["CEP" ]="26463200"


pessoa["TelefoneRes." ]="2126614848"  
pessoa["TelefoneCel" ]="21995442378"  
pessoa["Email" ]="email@email.com"

pessoa2 = pessoa.copy()


pessoas = [pessoa, pessoa2]

data={}
data["pessoas"] = pessoas
data["tipo"] = "Doutorado"

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

@app.route("/listpessoa")
def listpessoa():
	
    return render_template('listarNomes.html', data=data)

@app.route("/pessoa")
def verpessoa():
	#pessoa e um dicionario com os dados do inscrito
    return render_template('visualizarPessoa.html', data=pessoa)
@app.route("/form1")
def formDot():
	return render_template('formDoutorado.html')

@app.route("/form2")
def formMest():
	return render_template('formMestrado.html')

@app.route("/")
def pagInicial():
    return render_template('Initial.html', data=pessoa)

@app.route("/nana",methods=['POST'])
def pag():
	nana = request.form["CPF"]
	return render_template('nana.html', texto=nana)

@app.route("/login")
def login():
    return render_template('login.html', data=pessoa)

if __name__ == "__main__":
    app.run(debug=True)
