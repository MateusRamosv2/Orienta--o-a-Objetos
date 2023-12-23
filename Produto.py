from Transacao import Transacao



class Produto():
    def __init__(self):
        self.__nome = None
        self.__qtdeEstoque = None
        self.__precoUnit = None
        self.__estoqueMaximo = None
        self.__estoqueMinimo = None
        self.__historico = []
        self.__quantidadeDeb = None
        self.__debitarEstoque = None
        self.__creditarEstoque = None

    def setQuantidadeEstoque(self, qtdeEstoque):
        self.__qtdeEstoque = qtdeEstoque

    def getQuantidadeEstoque(self):
        return self.__qtdeEstoque

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def setPrecoUnit(self, precoUnit):
        self.__precoUnit = precoUnit

    def getPrecoUnit(self):
        return self.__precoUnit

    def setEstoqueMaximo(self, estoqueMaximo):
        self.__estoqueMaximo = estoqueMaximo

    def getEstoqueMaximo(self):
        return self.__estoqueMaximo

    def setEstoqueMinimo(self, estoqueMinimo):
        self.__estoqueMinimo = estoqueMinimo

    def getEstoqueMinimo(self):
        return self.__estoqueMinimo


    def setquantidadeDeb(self, quantidadeDeb):
        self.__quantidadeDeb = quantidadeDeb


    def getquantidadeDeb(self):
        return self.__quantidadeDeb



    def adicionarvenda(self):
        if self.__nome is not None and self.__nome not in self.__historico:
            self.__historico.append(self.__nome)
        elif self.__nome is None:
            print("Erro")





    def exibirhistorico(self):
        for produto in self.__historico:

            print(produto)




    def debitarEstoque(self):
        quantidadeDeb = 0
        if self.qtdeEstoque >= quantidadeDeb:
            self.qtdeEstoque -= quantidadeDeb
            print("Debito realizado !")
        else:
            self.qtdeEstoque = 0
            print("Não realizado")



    def creditarEstoque(self, quantidade):
        if quantidade > 0:
            self.__qtdeEstoque += quantidade
            print("credito realizado")
        else:
            print("Não realizado")

    def vender(self, quantidade, cliente):
        pass
        