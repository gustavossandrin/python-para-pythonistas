class Jquery:
    def __init__(self):
        self.funcao = None

    def ready(self, funcao):
        self.funcao = funcao

    def pagina_pronta(self):
        print('pagina pronta')
        if self.funcao is not None:
            self.funcao()


jquery = Jquery()

jquery.ready(lambda: print('olá mundo'))

if __name__ == '__main__':
    print('Main')
    jquery.pagina_pronta()
