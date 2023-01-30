import random
'''1. Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números aleatorios. 
De cada elemento de la lista diga si el elemento está por encima del promedio, 
debajo del promedio o es igual al promedio de todos los números de la lista.  '''
#Crear una lista vacia y crear variables
vector=[]
suma=0
promedio=0
cont=0
rango=random.randint(10,25)#Crear la cantidad de numeros en la lista de forma aleatoria entre 10 y 25
for i in range(rango):#Para i en el rango de la ecuacion anterior, que todos los numeros de la lista sean aleatorios entre 1 y 100
    vector.append(round(random.random()*100))
    suma+=vector[i]#La suma de todos los valores de la lista
    promedio=suma//rango#El promedio es la suma dividida en el rango que es la cantidad de numeros en la lista
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