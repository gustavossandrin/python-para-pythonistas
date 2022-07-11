import time
from threading import Thread


def contar(nome, n):
    for i in range(n):
        # time.sleep(.1)
        print(nome, i)


for i in range(3):
    t1 = Thread(target=contar, args=(i, 100))
    print('startando thread', i)
    t1.start()
