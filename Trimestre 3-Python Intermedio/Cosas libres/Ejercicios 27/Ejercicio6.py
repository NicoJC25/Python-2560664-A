'''6. Hacer un programa que pida una lista de números y los impresa al revés y agregue otro valor en
alguna de ellas.'''

from random import *

lista=[round(randrange(100))for i in range(randint(10,25))]
lista_reversa=[]


def reverso(list):
    for n in reversed(lista):
        lista_reversa.append(n)
    return lista_reversa

print('Esta es la lista en el orden normal: ',lista)
print('Esta es la lista en el orden reverso:',reverso(lista))
