import random
'''Llene una lista con la serie de Fibonacci. La cantidad de elementos de la lista la debe ingresar el usuario. Mínimo debe tener 5 elementos y máximo 20'''
#Crear una lista vacia y la cantidad de valores que pida el usuario entre 5 y 20
vector=[]
aux=True
A=0
B=1
C=1
while aux:#Mientras aux sea verdad
    rango=int(input('Elija la cantidad de elementos a ejecutar de la serie de Fibonacci: '))#Pedir la altura de la piramide
    if rango>=5 and rango<=20:#Si la altura esta entre 5 y 20, aux sera falso
        aux=False
    else:
        print('Deben de ser minimo 5 elementos y maximo 20')#Si no, soltar este mensaje y volver a pedir el numero
#Para i en rango del numero pedido, insertar la ecuacion para sacar Fibonacci
for i in range(rango):       
    C=A+B
    A=B
    B=C
    vector.append(C)#Y agregar al final de la lista el valor de C por cada vuelta
print ('La lista con los valores de Fibonacci hasta la posicion insertada es:',vector)