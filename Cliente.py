from Pessoa import Pessoa


class Cliente(Pessoa):

    def __init__(self):
        super().__init__()
        self.__nome = None
        self.__cpf = None

    def setCpf(self, cpf):
        self.__cpf = cpf

    def getCpf(self):
        return self.__cpf


    def setNome(self, nome):
        self.__nome = nome


    def getNome(self):
        return self.__nome


    def __str__(self):
        return f'nome = {self.__nome}, cpf = {self.__cpf}'
