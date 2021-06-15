from application import app
from flask import Flask, render_template, request, url_for, redirect
from application.model.dao.produtoDAO import ProdutoDAO

carrinho_list = []

ProdutoDAO = ProdutoDAO()
produto_list = ProdutoDAO.produto_list()

@app.route("/")
def index():
   return render_template("index.html", produto_list = produto_list , carrinho_list = carrinho_list)

@app.route("/adicionarProd/<id>")
def adicionar(id):
    for produto in produto_list:
        if int(id)==produto.get_id():
            carrinho_list.append(produto)
            return redirect(url_for('index'))

@app.route("/removerProd/<id>")
def removerProd(id):
    for produto in carrinho_list:
        if int(id)==produto.get_id():
            carrinho_list.remove(produto)
            return redirect(url_for('index'))

