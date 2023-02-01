from random import *

def lista_aleatoria(lista):
    lista=[round(randrange(100))for i in range(randint(10,25))]
    return lista

def pares(lista):
    par=[x for x in lista if x%2==0]
    return par