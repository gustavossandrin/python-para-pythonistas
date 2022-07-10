import pytest
from pytest import approx

from descriptors.framework import Propriedade, Modelo


class Quantidade(Propriedade):
    def validar(self, valor):
        if valor <= 0:
            raise TypeError('quantidade deveria ser positiva')


class ItemPedido(Modelo):
    quantidade = Quantidade()
    preco = Quantidade()

    def __init__(self, descricao, preco, quantidade):
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade

    def subtotal(self):
        return self.preco * self.quantidade


def test_subtotal():
    item = ItemPedido('feijão', 3.45, 2)
    assert 6.90 == approx(item.subtotal())


def test_set_quantidade_negativa():
    item = ItemPedido('feijão', 3.45, 2)
    with pytest.raises(TypeError):
        item.quantidade = -2


def test_set_quantidade_negativa_no_init():
    with pytest.raises(TypeError):
        ItemPedido('feijão', 3.45, -2)


def test_set_preco_negativo():
    item = ItemPedido('feijão', 3.45, 2)
    with pytest.raises(TypeError):
        item.preco = -3.45


def test_set_preco_negativo_no_init():
    with pytest.raises(TypeError):
        ItemPedido('feijão', -3.45, 2)


def test_propriedade_de_descriptor():
    item = ItemPedido('ervilha', 1.21, 2)
    assert {'descricao': 'ervilha', '_preco': 1.21,
            '_quantidade': 2} == item.__dict__
