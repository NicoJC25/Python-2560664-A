import random
'''Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números aleatorios. Encuentre la desviación estandar'''
#Crear una lista vacia y la cantidad de valores entre 10 y 25
suma=0
promedio=0
desviacion=0
rango=random.randint(10,25)
#Para i en rango de la ecuacion anterior, hacer que los valores de la lista sean aleatorios entre 1 y 100
vector=[round(random.random()*100)for i in range(rango)]#Lista comprendida donde los numeros de la lista seran de 1 a 100 en el rango de rango
for i in range(rango):
    suma+=vector[i]#Sumar todos los valores
    promedio=suma//rango#Sacar el promedio
    vector.sort()#Organizar los valores de menor a mayor
    tamaño=len(vector)#El tamaño sera la longitud de la lista
    tamaño_division=tamaño-1#El tamaño para dividir sera el tamaño anterior menos 1
desviacion=(suma-promedio)**2#La desviacion sera la resta entre la suma y el promedio elevada a la 2
division=desviacion//tamaño_division#La division sera la desviacion entre la variable tamaño_division
resultado=division**0.5#El resultado es la raiz cuadrada de esta division
print('La lista es:',vector)
print('El tamaño de la lista es:',rango)
print('La desviacion estandar es:',resultado)