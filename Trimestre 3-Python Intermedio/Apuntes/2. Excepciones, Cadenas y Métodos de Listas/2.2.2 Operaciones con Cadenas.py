#Ahora, tambien vemos el uso de ciertas operaciones especiales en las cadenas que tambien aplican en las listas.

#La funcion "min"

#Esta funcion lo que hace es que al ingresar su respectivo argumento, ejecuta cual de los caracteres del contenido es el primero que aparece en la tabla ASCII.
#Para que la funcion no ejecute un error, no deben haber espacios en blanco. Ejemplo:

'''print(min("aAbByYzZ")) #Ejemplo con una cadena

t = 'Los Caballeros Que Dicen "¡Ni!"'
print('[' + min(t) + ']') #Ejemplo con mas elementos externos

t = [0, 1, 2] #Ejemplo con una lista
print(min(t))'''

#Como se debe de suponer, tambien existe un funcion que encuentra el caracter maximo de algun dato ingresado: max. Ejemplo:

'''print(max("aAbByYzZ")) #Ejemplo con una cadena

t = 'Los Caballeros Que Dicen "¡Ni!"' #Ejemplo con mas elementos externos
print('[' + max(t) + ']')

t = [0, 1, 2] #Ejemplo con una lista
print(max(t))'''


#Ahora veremos el metodo "index"

#Este metodo lo que hace es que, al momento de ingresr su argumento (cadena, lista, etc.), y, al ingresar el caracter que se desea buscar -->
#si encuentra el caracter especificado, indicara la posicion en la que se encuentra este mismo. Ejemplo:

'''print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))'''

#Nota: Recordemos que es un metodo, asi que hay que utilizar una sintaxis diferente a la de una funcion.


#Otra funcion importante es la proclamada "list". Esta funcion convierte una entidad (cadena, tupla, diccionario) en una lista. Ejemplo:

'''print(list("abcabc"))'''

#El metodo count, sirve para contar la cantidad de veces que hay un elemento especificado en una secuencia. Ejemplo:

'''print("abcabc".count("b"))
print('abcabc'.count("d"))'''

