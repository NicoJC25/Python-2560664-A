import random
'''Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números aleatorios. Encuentre la moda de los números de la lista'''
#Asignar variables y el rango de la lista
vec=[]
vecCant=[]
rango=random.randint(10,25)
#Para i en rango de la ecuacion anterior, hacer que los valores de la lista sean aleatorios entre 1 y 100
for i in range(rango):
   vec.append(round(random.random()*100))
print(vec)
cont=0
for i in range(len(vec)):#Para i en el rango de la longitud del vector
    cont=0
    for j in vec: #Para j en el vector    
        if vec[i] == j:#Si algun valor de la lista i es igual al de la lista j, aumentara el contador en 1
            cont+=1 
    if cont!=0: #Si el contador es diferente a 0, se agregara su valor al final de una lista nueva 
        vecCant.append(cont)
    else:#Si es 0, se agregara un 0 al final de la lista
        vecCant.append(0)
print(vec)
print(vecCant)
mayor=0
pos=0
for i in range(len(vec)):#Para i en el rango de la longitud del vector
    if mayor<vecCant[i]:#Si el valor de mayor es menor al valor evaluado de la lista con la moda
       mayor=vecCant[i]#Mayor obtendrá el valor de esta misma lista
print('El mayor es ',mayor)
for j in range(len(vecCant)):#Para j en el rango de la longitud de vecCant
    if mayor==vecCant[j]:#Si mayor es igual a los valores de vecCant
        print('la moda es ',vec[j])#Imprimira esos valores iguales