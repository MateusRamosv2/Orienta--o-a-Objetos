
from Pessoa import Pessoa


class Fornecedor(Pessoa):

    def __init__(self):
        super().__init__()
        self.__nome = None
        self.__cnpj = None

    def setCnpj(self, cnpj):
        self.__cnpj = cnpj

    def getCnpj(self):
        return self.__cnpj

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome
