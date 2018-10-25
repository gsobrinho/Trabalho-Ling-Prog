# coding: utf-8

import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing
import pickle
from banco import *

# configuração
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = '1234'

app = Flask(__name__)
app.config.from_object(__name__)

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
    updados(pessoa)
    
    return render_template('visualizarPessoa.html', data=pessoa)
 
@app.route("/visualizarPessoa",methods=['GET', 'POST'])
def verPessoa():

    aux = getDados()
    pessoa = {}
    for i in aux:
        if i["CPF"] == request.form['CPF']:
            pessoa = i
             
    
    return render_template('visualizarPessoa.html', data=pessoa)
 

@app.route("/login", methods=['GET', 'POST'])
def login():
    erro = None
    if request.method == 'POST':
        if request.form['user'] != app.config['USERNAME']:
            erro = 'Usuario inalido'
        elif request.form['senha'] != app.config['PASSWORD']:
            erro = 'Senha invalida'
        else:
            session['logado'] = True
            flash('Login OK')
            #aki eu acho que já pode exibir o posLogin
            return  render_template("/posLogin.html")
    return render_template('login.html', erro=erro)




@app.route("/insDoutorado")
def inscDout():
    # dict com os dados de aluno de Doutorado 
   
    aux = getDados()
    doutourado = {}
    lista = []
    doutourado["Tipo"] = "Doutorado"
    for i in aux:
        if i["Tipo"] == "Doutorado":
            lista.append(i)

    doutourado["pessoas"] = lista
 
    return render_template("listarNomes.html", data=doutourado)
    
@app.route("/insMestrado")
def inscMest():
    # dict com os dados de aluno de Doutorado 
   
    aux = getDados()
    mestrado = {}
    lista = []
    mestrado["Tipo"] = "Mestrado"
    for i in aux:
        if i["Tipo"] == "Mestrado":
            lista.append(i)

    mestrado["pessoas"] = lista
 
    return render_template("listarNomes.html", data=mestrado)
    
if __name__ == "__main__":
    app.run(debug=True)


