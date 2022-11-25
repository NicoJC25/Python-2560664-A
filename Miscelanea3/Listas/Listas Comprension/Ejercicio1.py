import random
'''1. Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números aleatorios. 
De cada elemento de la lista diga si el elemento está por encima del promedio, 
debajo del promedio o es igual al promedio de todos los números de la lista.  '''
#Crear una lista vacia y crear variables
promedio=0
suma=0
rango=random.randint(10,25)#Crear la cantidad de numeros en la lista de forma aleatoria entre 10 y 25

vector=[round(random.random()*100)for i in range(rango)]#Lista comprendida donde los numeros de la lista seran de 1 a 100 en el rango de rango
for i in range(rango):
    suma+=vector[i]#Suma
print (suma)
promedio=suma//rango
print('El rango de la lista es:',rango)
print('Los valores de la lista son:',vector)
print('El promedio de los valores es:',promedio)
#Para n en el vector, n tomara cada valor de la lista y los comparara con el promedio lanzando el respectivo mensaje por cada situacion
for n in vector:
    if n<promedio:
        print('El numero',n,'es menor al promedio')
    elif n>promedio:
        print('El numero',n,'es mayor al promedio')
    elif n==promedio:
        print('El numero',n,'es igual al promedio')