#Ahora vamos a ver el modulo random.
#Todos los valores que conocemos en computacion como "aleatorio", realmente son "pseudoaleatorios".

#Los valore pseudoaleatorios se refiere a valores que son casi imposibles de predecir pero que al momento de generarse, -->
#Sigue algoritmos muy especificos y bien hechos que forman estos numeros, por lo cual, su generacion no es aleatoria.

#Para generar numeros aleatorio, se toma un valor llamado "semilla", a partir de este valor se emplea un algoritmo que, -->
#De acuerdo al algoritmo enpleado, se genera un valor "aleatorio" a partir de esa semilla.

#Todo este largo proceso, lo realiza el modulo al momento de importarlo y usar sus funciones, vamos alla.

#Para empezar, vemos la funcion "random" (no confundir con el nombre del modulo), esta funciones genera un numero -->
#Aleatorio mayor o igual a 0.0, pero menor que 1.0 . A continuacion, un programa de ejemplo:

'''from random import random #Importamos la funcion random del modulo random

for i in range(5): #En un rango de 5
    print(random()) #Imprimir 5 numeros aleatorios'''

#Ahora bien, existe una funcion llamada "seed" en la que se puede establecer la semilla del generador manualmente.
#He aqui 2 de sus variantes:

'''from random import *
seed() #Semilla totalmente aleatoria
seed(int_value) #Semilla establecida con un valor entero'''

#Ejemplo de codigo con una semilla especifica:

'''from random import random, seed #Importar random y seed

seed(0) #Semilla numero 0

for i in range(5):
    print(random()) #Cinco numeros aleatorios'''

#Con una semilla especifica lo que hacemos es que sin importar cuantas veces lo imprimamos, siempre van a ser los mismos numeros
#Ahora vamos a ver 2 funciones muy utiles del modulo: randrange y randint:

'''from random import randrange, randint #Importamos funciones

print(randrange(1), end=' ') #Imprimir numeros aleatorios en rango de 1 (0 por la regla de la derecha)
print(randrange(0,1), end=' ') #Imprimir de 0 a 1 numeros aleatorios (0 por la regla de la derecha)
print(randrange(0,1,1), end=' ') #Imprimir de 0 a 1 numeros aleatorios con un incremento de 1 en 1 (0 por la regla de la derecha)
print(randint(0,1)) #Imprimir de 0 a 1 numeros aleatorios entre 0 y 1 (si aplica porque este excluye la regla de la derecha)'''

#La desventaja de las funciones anteriores, es que siempre existe una probabilidad de que se repitan valores y, -->
#Mientras mas pequeño el rango, mas probabilidad de repetir un numero. Ejemplo:
'''from random import randint

for i in range(10): #Para i en rango de 1 a 10
    print(randint(1,10), end=',') #Imprime numeros aleatorios entre 1 a 10'''

#En ese ejemplo, al ser un rango tan pequeño, hay una probabilidad muy altan de que se repita algun numero.
#Para eso, existen 2 funciones que soluciona un poco esto:

'''from random import choice, sample

my_list = [1,2,3,4,5,6,7,8,9,10]

print(choice(my_list)) #En este, lo que hace el programa es elegir un elemento al azar de la lista
print(sample(my_list,5)) #En sample, uno elige el rango de elementos aleatorios que debe mostrar
print(sample(my_list,10)) #El rango no puede superar el de la lista '''