
import random


def temperatura():
    return random.randrange(2, 32)


def umidade():
    return random.randrange(10, 95)


def aquecedor(estado):
    if estado == 'on':
        print('Aquecedor LIGADO')
    else:
        print('Aquecedor DESLIGADO')
