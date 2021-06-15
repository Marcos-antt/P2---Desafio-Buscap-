from application import app
from flask import Flask, render_template, request, url_for
from application.model.dao.produtoDAO import ProdutoDAO



ProdutoDAO = ProdutoDAO()
produto_list = ProdutoDAO.produto_list()

@app.route("/")
def index():
   return render_template("index.html", produto_list=produto_list)