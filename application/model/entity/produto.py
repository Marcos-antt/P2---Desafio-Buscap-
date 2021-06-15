class Produto:

    def __init__(self, id=None, imagens=list,  name=None, preco=None, valorPrestacao=None, prestacao=None):
        self.__id = id 
        self.__imagens = imagens
        self.__name = name
        self.__preco = preco
        self.__valorPrestacao = valorPrestacao
        self.__prestacao = prestacao

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_imagens(self):
        return self.__imagens
    
    def set_imagens(self, img):
        self.__imagens = img

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        self.__preco = preco

    def get_prestacao(self):
        return self.__prestacao

    def set_prestacao(self, prestacao):
        self.__prestacao = prestacao

    def get_valorPrestacao(self):
        return self.__valorPrestacao

    def set_valorPrestacao(self, valorPrestacao):
        self.__valorPrestacao = valorPrestacao
