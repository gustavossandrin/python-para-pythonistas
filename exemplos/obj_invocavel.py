class Invocavel:
    def __init__(self, numero):
        self.numero = numero

    def __call__(self):
        return self.numero


if __name__ == '__main__':
    invocaveis = map(Invocavel, range(1, 3))

    for invocavel in invocaveis:
        print(invocavel())
