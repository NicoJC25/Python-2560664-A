import random


def llenar_lista(lista):
    lista=[round(random.randrange(100))for i in range(random.randint(5,15))]
    print(lista)
    return lista


def sum_lista(lista):
    suma=0
    for i in lista:
        suma+=i
    return suma

lista=llenar_lista(list)
print('La suma de los elementos de la lista es:',sum_lista(lista))