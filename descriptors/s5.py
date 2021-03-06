import pytest
from pytest import approx


class Quantidade:
    def __init__(self):
        self._nome = f'_{id(self)}'

    def set_nome(self, nome):
        self._nome = f'_{nome}'

    def __get__(self, item, owner):
        return getattr(item, self._nome)

    def __set__(self, item, valor):
        if valor <= 0:
            raise TypeError('quantidade deveria ser positiva')
        setattr(item, self._nome, valor)


_flag_new_executado = False


class ItemPedido:
    quantidade = Quantidade()
    preco = Quantidade()

    def __new__(cls, *args, **kwargs):
        global _flag_new_executado
        if not _flag_new_executado:
            for nome, propriedade in cls.__dict__.items():
                if hasattr(propriedade, 'set_nome'):
                    propriedade.set_nome(nome)
            _flag_new_executado = True
        return super().__new__(cls)

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
