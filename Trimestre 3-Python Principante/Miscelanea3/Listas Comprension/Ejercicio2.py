import random
'''Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números aleatorios. Muestre cuales y cuantos son primos'''
#Hacer una lista vacia y ponerle tamaño aleatorio entre 10 y 25
rango=random.randint(10,25)
vector=[round(random.random()*100)for i in range(rango)]#Lista comprendida de valores entre 1 a 100 aleatorios para la lista
print('Lista:',vector)
for n in vector: #Para n en vector, n tomara el valor de cada cifra en la lista y se crearan 2 variables llamadas i y cont
    i=1
    cont=0
    while(n>=i):#Mientras n sea mayor o igual a i, si el residuo del valor de la lista dividido en i es 0, entonces el contador aumentara 1
        if n%i==0:
            cont+=1
        i+=1#E i siempre aumentara por cada vuelta
    if not cont>2 or n <=1: #Si el numero no cumple ninguna de estas condiciones, es primo
        print('El numero',n,'es primo')