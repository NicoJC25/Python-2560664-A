'''2. se requiere un programa que compare dos listas y diga cual tiene más elementos.'''
from random import randrange, randint

def lista_aleatoria(lista):
    lista=[round(randrange(100))for i in range(randint(10,25))]
    return lista

lista1=lista_aleatoria(list)
lista2=lista_aleatoria(list)

def compare(l1,l2):
    if len(l1)>len(l2):
        return('La primera lista tiene mas elementos que la segunda')
    elif len(l2)>len(l1):
        return('La segunda lista tiene mas elementos que la primera')
    else:
        return('Ambas listas son iguales')
        
print(lista1)
print(lista2)
print(compare(lista1,lista2))