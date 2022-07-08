from functools import partial
from time import strftime
import functools


def logar(func=None, *, fmt='%H:%M:%S'):
    if func is None:
        return partial(logar, fmt=fmt)

    @functools.wraps(func)
    def envoltoria(*args, **kwargs):
        agora = strftime(fmt)
        print(f'{agora} executando função {func.__name__}')
        return func(*args, **kwargs)

    return envoltoria


@logar
def ola_mundo():
    """função olá mundo"""
    return 'olá mundo'


@logar()
def hello(nome):
    return f'hello {nome}'


if __name__ == '__main__':
    print(ola_mundo())
    print(ola_mundo.__name__)
    print(ola_mundo.__doc__)
    print(hello('gustavo'))
    print(hello.__name__)
