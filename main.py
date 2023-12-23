from datetime import date
from datetime import datetime

from Transacao import Transacao
from Compra import Compra
from Venda import Venda
from Fornecedor import Fornecedor
from Cliente import Cliente
from Pessoa import Pessoa
from Produto import Produto


def principal():



    c1 = Cliente() #Pessoa
    c1.setNome("Marco")
    c1.setCpf("123")
    print(c1.getNome())



    p1 = Produto()
    p1.setNome("Caneta")
    p1.adicionarvenda()
    p1.setQuantidadeEstoque(100)
    p1.setPrecoUnit(1.2)
    p1.setEstoqueMinimo(10)
    p1.setEstoqueMaximo(200)
    p1.exibirhistorico()



    produto1 = Venda()
    produto1.setQdtevenda(95)
    produto1.setDatavenda('26/7/2021')
    print(produto1.getQdtevenda(), produto1.getDatavenda(), c1.getNome())

    f1 = Fornecedor()
    f1.setNome("Antonio")
    f1.setCnpj(456)
    print(f1.getNome(), f1.getCnpj())



    produto1 = Compra()
    produto1.setDatacompra('26/7/2021')
    produto1.setQtdecompra(50)
    produto1.setPrecounit(1.1)
    print(produto1.getDatacompra(), produto1.getQtdecompra(), produto1.getPrecounit())


    p1.exibirhistorico()
    print(p1.exibirhistorico())















    #  print(p1.getNome())
    # print(c1.getNome(), ',', c1.getCpf())
    # print(f1.getNome())


if __name__ == '__main__':
    principal()
