import pytest


def fatorial(n):
    produto = 1
    for i in range(2, n+1):
        produto *= i
    return produto


@pytest.mark.parametrize('n, esperado', [
    (1, 1),
    (2, 2),
    (3, 6),
    (5, 120),
    (9, 362880)
])
def test_fatorial(n, esperado):
    assert esperado == fatorial(n)


def test_atribuicao_de_funcao():
    fat = fatorial
    assert 120 == fat(5)
    assert fat is fatorial
    assert 'fatorial' == fat.__name__
    assert callable(fat)


