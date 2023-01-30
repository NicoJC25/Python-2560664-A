'''9. Se necesita llenar una temperatura y este muestre si está por encima, abajo o en cero.'''

from random import *

temperatura=list(randrange(-20,30)for i in range(1))
print(temperatura)

def temp(tem):
    for i in temperatura:
        if i>0:
            return('es mayor a 0')
        elif i<0:
            return('es menor a 0')
        else:
            return('es igual a 0')

print('La temperatura arrojada es de',temperatura,'grados, por lo cual,',temp(temperatura),)