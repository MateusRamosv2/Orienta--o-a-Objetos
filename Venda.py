from Transacao import Transacao
from datetime import datetime

class Venda(Transacao):

    def __init__(self):
        super().__init__()
        self.__dataVenda = None
        self.__cliente =  None
        self.__qdteVenda =  None


    def setDatavenda(self, data):
        self.__dataVenda = datetime.strptime(data, '%d/%m/%Y')

    def getDatavenda(self):
        return self.__dataVenda

    def setCliente(self, cliente):
        self.__cliente = cliente

    def getCliente(self):
        return self.__cliente


    def setQdtevenda(self, qdteVenda):
        self.__qdteVenda = qdteVenda

    def getQdtevenda(self):
        return self.__qdteVenda




