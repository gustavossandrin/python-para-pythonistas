from pytest import approx


class ItemPedido:
    def __init__(self, descricao, preco, quantidade):
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade

    def subtotal(self):
        return self.preco * self.quantidade


def test_subtotal():
    item = ItemPedido('feijão', 3.45, 2)
    assert 6.90 == approx(item.subtotal())


def test_subtotal_negativo():
    item = ItemPedido('feijão', 3.45, -2)
    assert 6.90 == approx(item.subtotal())
