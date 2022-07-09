def meu_partial(funcao, *args, **kwargs):
    def internal(*internal_args, **internal_kwargs):
        return funcao(*args, *internal_args, **kwargs, **internal_kwargs)

    return internal


def soma(a, b):
    return a + b


nova_soma = meu_partial(soma, 6)
print(nova_soma(7))
