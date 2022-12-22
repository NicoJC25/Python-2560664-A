from random import random, randint

def buscar(lista):
    numero=int(input('Inserte el numero a buscar: '))
    for i in lista:
        if numero==i:
            return lista.index(i)
        else:
            return -1

lista=[round(random()*100)for i in range(randint(10,25))]

print(lista)
print(buscar(lista))