import random
'''Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números aleatorios. Encuentre la mediana de los números de la lista'''
#Crear una lista vacia y la cantidad de valores entre 10 y 25
vector=[]
rango=random.randint(10,25)
#Para i en rango de la ecuacion anterior, hacer que los valores de la lista sean aleatorios entre 1 y 100
for i in range(rango):
    vector.append(round(random.random()*100))
print('La lista sin ordenar es:',vector)
#vector.sort hara que se organicen todos los elementos de la lista
vector.sort()
print('La lista ordenada es:',vector)
mitad=int(rango//2)#La mitad sera el numero que esta en el rango dividido entre 2
#Si el rango de la lista es par, sumar y dividir los 2 numeros centrales
if rango %2==0:
    mediana=(vector[mitad-1]+vector[mitad])//2
else:#Si no, solo tomar el valor central
    mediana=vector[mitad]
print('La longitud del vector es:',rango)
print ('La mediana del vector es:',mediana)