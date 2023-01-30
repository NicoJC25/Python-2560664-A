from random import random as ran, randint as rang, randrange as rang2

def lista_random (lista):
    lista=[round(rang2(100))for i in range (rang(10,25))]
    return lista

def sumar_lista (lista):
    suma=0
    rango=len(lista)
    for i in range(rango):
        suma+=lista[i]
    return suma

def par (lista):
    par=[x for x in lista if x%2==0]
    return par

def impar (lista):
    impar=[x for x in lista if x%2!=0]
    return impar

def promedio (lista):
    suma=sumar_lista(lista)
    rango=len(lista)
    promedio=suma//rango
    return promedio


