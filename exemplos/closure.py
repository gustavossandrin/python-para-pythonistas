def criar_conta(saldo):
    def retirada(valor):
        nonlocal saldo
        if valor >= saldo:
            raise ValueError('retirada não pode ser maior que o saldo')
        saldo -= valor
        return saldo

    return retirada


if __name__ == '__main__':
    retirar = criar_conta(100)
    print(retirar(50))
    print(retirar(50))
