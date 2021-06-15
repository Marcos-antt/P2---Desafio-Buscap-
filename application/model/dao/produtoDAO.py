from application.model.entity.produto import Produto
import json 



class ProdutoDAO():


    def produto_list(self):
        return self.__produto_list




    def dict_to_list(self, lista_prod):
        lista = []
        for produto_item in lista_prod:
            produto = Produto()
            produto.set_id(produto_item["id"])
            produto.set_name(produto_item["name"])
            produto.set_imagens(produto_item["images"])
            preco = produto_item["price"]
            produto.set_preco(preco["value"])
            produto.set_prestacao(preco["installments"])
            produto.set_valorPrestacao(preco["installmentValue"])
            lista.append(produto)
        return lista

    def produto_list(self):
        list = []
        with open("buscape.json", "r") as file:
            produto_list = json.load(file)
            list = self.dict_to_list(produto_list)
        return list 

    