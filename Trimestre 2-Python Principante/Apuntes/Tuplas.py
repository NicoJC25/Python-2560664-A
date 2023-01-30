#Una tupla es un valor en parentesis parecido a una lista, solo que sus valores son inmutables

#Ejemplo de tupla:

tuple_1=(1,2,3,4,5) #Son muy parecidas a las variables solo que tienen la misma sintaxis de como escribiriamos una lista
tuple_2=1., .5, .34, .125 #Tambien se pueden escribir sin parentesis de esta forma

one_element_tuple=(1,) #Asi las tuplas tengan un elemento, hay que colocar una coma al final en este caso para que el programa la reconozca como tupla y no como variable

#Los elementos se pueden leer como los elementos de una lista, ejemplo:
'''my_tuple = (1, 10, 100, 1000) #Creamos la tupla
print(my_tuple[0]) #Primera posicion
print(my_tuple[-1]) #Ultima posicion
print(my_tuple[1:]) #Desde la primera posicion hasta la penultima
print(my_tuple[:-2]) #Desde la primera posicion hasta la antepenultima
for elem in my_tuple: #Imprime cada elemento de la tupla uno por uno
    print(elem)'''

#CUIDADO: No confundirse intentando modificar la tupla, no se puede usar ni .append, insert, del u otra de estas variables, el programa sacara error

#Se puede usar la variable len(), + para unir tuplas, * para multiplicarlas y los operadores in y not in. Ejemplo:
my_tuple = (1, 10, 100)
t1 = my_tuple + (1000, 10000) #Ejemplo de union de tuplas
t2 = my_tuple * 3 #Ejemplo de multiplicacion de tuplas
print(len(t2)) #Longitud de la primera tupla
print(t1)
print(t2)
print(10 in my_tuple) #Indicar en booleano si 10 esta en la tupla
print(-10 not in my_tuple) #Indicar en booleano si -10 no esta en la tupla'''

#Se pueden intercambiar tuplas, ademas de agregar variables a estas mismas. Ejemplo: 
'''var = 123 #Variable
t1 = (1, )
t2 = (2, )
t3 = (3, var) #La tupla 3 llevara un literal y la variable
t1, t2, t3 = t2, t3, t1 #Intecambia valores de tuplas
print(t1, t2, t3)'''

#Se puede eliminar una tupla usando del. Ejemplo:
'''my_tuple = 1, 2, 3, 
del my_tuple
print(my_tuple)    # NameError: name 'my_tuple' is not defined'''

#Ejercicio de tupla llenada por compresion
'''import random
tupla=tuple((i for i in range(1,11)))
print(tupla)
tupla1=tuple((round(random.random()*100)for i in range(10)))
print(tupla1)'''