import random #Primero importar random
'''Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. 
Llene la lista con números aleatorios. Encuentre la suma y el promedio de los números de la lista'''
suma=0#Variables de la suma de los elementos y el promedio
promedio=0
rango=random.randint(10,25)#Establecer la longitud de la lista
vector=[round(random.random()*100)for i in range(rango)]#Lista comprendida donde los numeros de la lista seran de 1 a 100 en el rango de rango
for i in range(rango):
    suma+=vector[i]#La suma sera igual a todos los elementos de la lista recorridos por i
    promedio=suma//rango#El promedio sera igual a la suma dividida entre el rango que es la cantidad de numeros de la lista
print('El rango de la lista es:',rango)
print('Los elementos de la lista son:',vector)
print('La suma de los elementos de la lista es:',suma)
print('El promedio de los elementos de la lista es:',promedio)