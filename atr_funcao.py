nome = 'gustavo'


def f(a: int, b=2, *, c=3) -> str:
    """Função exemplo para verificar atributos"""


f.parametro_dinamico = True

if __name__ == '__main__':
    print(f.__doc__)
    print(f.__defaults__)
    print(f.__globals__)
    print(f.__dict__)
    print(f.__closure__)
    print(f.__annotations__)
    print(f.__kwdefaults__)
