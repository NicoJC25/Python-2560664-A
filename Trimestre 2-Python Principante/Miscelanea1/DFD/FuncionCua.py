A=0
B=0
C=0
X=0


P = input('¿Desea poner el valor de A?: ')
if P == 'si':
    A = int(input('Ingrese el valor de A: '))
P = input('¿Desea poner el valor de B?: ')
if P == 'si':
    B = int(input('Ingrese el valor de B: '))
P = input('¿Desea poner el valor de C?: ')
if P == 'si':
    C = int(input('Ingrese el valor de C: '))
P = input('¿Desea poner el valor de X?: ')
if P == 'si':
    X = int(input('Ingrese el valor de X: '))


F = (A*(X**2)) + (B*X) + C
print ('La funcion cuadratica es: ',F)