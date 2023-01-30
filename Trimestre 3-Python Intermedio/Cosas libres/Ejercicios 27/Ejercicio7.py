'''7. Se necesita un programa que llene una tupla e imprima lo que esta adentro una por una.'''

from random import *

tupla=tuple(round(randrange(100))for i in range(10))
print(tupla)

def dig_tupla(tp):
    for e in range(0,len(tupla)):
        print(tupla[e],end=' ')

dig_tupla(tupla)