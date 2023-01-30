from random import random as ran, randint as rang, randrange as rang2

def lista_random (lista):
    lista=[round(rang2(100))for i in range (rang(10,25))]
    print('Esta es la lista:')
    return lista
def sumar_lista (lista):
    suma=0
    rango=len(lista)
    for i in range(rango):
        suma+=lista[i]
    print('La suma de los elementos de la lista es: ')
    return suma

def par (lista):
    par=[x for x in lista if x%2==0]
    print('Los pares de la lista son: ')
    return par

def impar (lista):
    impar=[x for x in lista if x%2!=0]
    print('Los impares de la lista son:')
    return impar

def promedio (lista):
    suma=0
    rango=len(lista)
    for i in range(rango):
        suma+=lista[i]
    
    promedio=suma//rango
    print('El promedio de los elementos de la lista es: ')
    return promedio


