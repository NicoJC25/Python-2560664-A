import random
'''Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números aleatorios. 
Sume los pares y saque el promedio de los impares'''
#Crear variables y lista
total_pares=0
total_impares=0
promedio_impares=0
rango=random.randint(10,25)#Rango aleatorio de la lista entre 10 a 25 cifras
vector=[round(random.random()*100)for i in range(rango)]#Lista comprimida con valores aleatorios de 1 a 100 en la lista

par=[x for x in vector if x%2==0]#lista comprimida de pares
for x in range(len(par)):
    total_pares+=par[x]
impar=[x for x in vector if x%2!=0]#Lista comprimida de impares
for x in range(len(impar)):
    total_impares+=impar[x]

promedio_impares=(total_impares//len(impar)) #Promedio de los impares
        
print ('La longitud de la lista es:',rango,'y los valores de la lista son:',vector)
print ('La suma de los pares fue:',total_pares)
print ('El promedio de los impares es:',promedio_impares)