import random
'''Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números aleatorios. 
Sume los pares y saque el promedio de los impares'''
#Crear variables y lista
total_pares=0
total_impares=0
promedio_impares=0
cont=0
vector=[]
rango=random.randint(10,25)#Rango aleatorio de la lista entre 10 a 25 cifras
for i in range(rango):#Para i en el rango de la ecuacion anterior, que los numeros sean aleatorios entre 1 y 100
    vector.append(round(random.random()*100))
#Para i en el rango del rango de la lista, si el residuo de la cifra de la lista al dividirse en 2 es 0, entones es par el numero. Si no es impar
for i in range(rango):
    if vector[i]%2==0:
        total_pares+=vector[i]#Suma de todos los pares
    else:
        total_impares+=vector[i]
        cont+=1
        promedio_impares=total_impares//cont#Promedio de los impares
        
        
print ('La longitud de la lista es:',rango,'y los valores de la lista son:',vector)
print ('La suma de los pares fue:',total_pares)
print ('El promedio de los impares es:',promedio_impares)