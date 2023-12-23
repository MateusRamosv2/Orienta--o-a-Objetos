from Transacao import Transacao
from datetime import datetime


class Compra(Transacao):

    def __init__(self):
        super().__init__()
        self.__precoUnit = None
        self.__dataCompra = None
        self.__produto = None
        self.__fornecedor = None
        self.__qtdeCompra = None


    def setPrecounit(self, precoUnit):
        self.__precoUnit = precoUnit

    def getPrecounit(self):
        return self.__precoUnit

    def setDatacompra(self, data):
        self.__dataCompra = datetime.strptime(data, '%d/%m/%Y')

    def getDatacompra(self):
        return self.__dataCompra

    def setProduto(self, produto):
        self.__produto = produto

    def getProduto(self):
        return self.__produto

    def setFornecedor(self, fornecedor):
        self.__fornecedor = fornecedor

    def getFornecedor(self):
        return self.__fornecedor

    def setQtdecompra(self, qtdeCompra):
        self.__qtdeCompra = qtdeCompra

    def getQtdecompra(self):
        return self.__qtdeCompra
