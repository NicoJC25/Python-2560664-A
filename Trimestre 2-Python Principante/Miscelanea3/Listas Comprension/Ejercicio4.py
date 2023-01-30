import random
'''Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. 
Llene la lista con números aleatorios. Ordenar el arreglo, de mayor a menor y de menor a mayor (algoritmo de la burbuja)'''
#Crear una lista vacia y la cantidad de valores entre 10 y 25
rango=random.randint(10,25)
vector=[round(random.random()*100)for i in range(rango)]#Lista comprendida donde los numeros de la lista seran de 1 a 100 en el rango de rango
print('La lista sin ordenar es:',vector)
intercambio=True
while intercambio: #Mientras el intercambio sea verdad, sera falso momentaneamente
    intercambio=False
    for i in range(len(vector)-1):#Para i en rango de la longitud del vector menos 1
        if vector[i]<vector[i+1]:#Si el primer valor de la lista es menor al segundo, se van a intercambiar, si no se dejan igual y se comparan los 2 siguientes valores--
            vector[i],vector[i+1]=vector[i+1],vector[i]#Ya que i se ira sumando un espacio en la lista por cada ejecucion del for
            intercambio=True#Volvemos a decir que el intercambio sera verdad
vector2=vector[:]
intercambio2=True
while intercambio2: #Mientras el intercambio sea verdad, sera falso momentaneamente
    intercambio2=False
    for j in range(len(vector2)-1):#Para i en rango de la longitud del vector menos 1
        if vector2[j]>vector2[j+1]:#Si el primer valor de la lista es mayor al segundo, se van a intercambiar, si no se dejan igual y se comparan los 2 siguientes valores--
            vector2[j],vector2[j+1]=vector2[j+1],vector2[j]#Ya que i se ira sumando un espacio en la lista por cada ejecucion del for
            intercambio2=True#Volvemos a decir que el intercambio sera verdad

print('La lista ordenada en forma descendiente es:',vector)
print('La lista ordenada en forma ascendente es:',vector2)