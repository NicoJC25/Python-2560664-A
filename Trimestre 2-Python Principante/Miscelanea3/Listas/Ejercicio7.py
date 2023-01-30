import random #Primero importar random
'''Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. 
Llene la lista con números aleatorios. Encuentre la suma y el promedio de los números de la lista'''
vector=[]#Crear una lista vacia
suma=0#Variables de la suma de los elementos y el promedio
promedio=0
rango=random.randint(10,25)#Establecer la longitud de la lista
for i in range(rango):#Para i en el rango de la condicion anterior
    vector.append(round(random.random()*100))#Decir que los elementos de la lista seran aleatorios entre numeros de 1 a 100
    suma+=vector[i]#La suma sera igual a todos los elementos de la lista recorridos por i
    promedio=suma//rango#El promedio sera igual a la suma dividida entre el rango que es la cantidad de numeros de la lista
print('El rango de la lista es:',rango)
print('Los elementos de la lista son:',vector)
print('La suma de los elementos de la lista es:',suma)
print('El promedio de los elementos de la lista es:',promedio)