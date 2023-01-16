#Los diccionarios son una forma de poner pares de valores, uno de estos siendo una "Palabra clave" y el otro un "Valor". Dos conceptos a tener muy en cuenta

#Las palabras clave no pueden duplicarse, pueden ser de cualquier tipo de dato, no son listas realmente, se puede usar len en esta y solo se pueden usar en 1 solo sentido. Ej:

#Diccionario de palabras en Español a Frances. Este diccionario solo puede buscar palabras del español en frances, no al reves

#Ejemplo de un diccionario:
'''dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"} #Se utilizan llaves para estos mismos. Se utilizan claves 'gato' y valores 'chat'. Son el mismo tipo de dato
phone_numbers = {'jefe': 5551234567, 'Suzy': 22657854310} #Aca se utilizan claves con str y los valores son int
empty_dictionary = {} #Diccionario vacio
print(dictionary)
print(phone_numbers)
print(empty_dictionary)'''

#Tambien a tener muy en cuenta es que los str estan encerrados en comillas, cada clave y valor estan separados con ":" para indicar que tal clave significa tal valor
#Tambien que cada para esta separado por una coma
#Hay una parte del modulo que indica que los datos se imprimen en forma desorganizada, en esta version ya no esta eso por lo cual no aplica}

#Para imprimir un dato en especifico, se pone el print, nombre del diccionario y entre corchetes, la palabra clave. Ejemplo:
'''print(dictionary['gato']) #Si es un str, se ponen las comillas para especificar esto mismo, ademas de las minusculas y mayusculas correspondientes
print(phone_numbers['Suzy'])'''

#Esto imprimira como resultado los valores, osea en el caso de "gato" imprimira "chat" y en el caso de "Suzy" imprimira "22657854310"
#Si se utiliza una palabra clave que no exista, saca error
#Podemos usar in y not in para mirar si un elementoe esta en el diccionario. Ejemplo:
'''dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"} #Diccionario
words = ['gato', 'león', 'caballo'] #Palabras a evaluar si estan en el diccionario
for word in words: #Para palabra en la lista words
    if word in dictionary: #Si esa palabra esta en el diccionario
        print(word, "->", dictionary[word]) #Imprimira la palabra y su "valor" (no palabra clave) en el diccionario
    else:
        print(word, "no está en el diccionario") #Si no, este mensaje'''



#Existe un formato llamado sangría francesa que se aplica para los diccionarios largos. Ejemplo:
'''# Ejemplo 1:
dictionary = {
              "gato": "chat",
              "perro": "chien",
              "caballo": "cheval"
              }
# Ejemplo 2:
phone_numbers = {'jefe': 5551234567,
                 'Suzy': 22657854310
                 }'''

#Por si solo, el bucle for no funciona en los diccionaros al no ser datos secuenciales, pero se pueden adaptar para que funcionen en el ciclo for
#Uno de estos metodos es "keys()", este sirve para retornar una lista con todas las claves del diccionario. Ejemplo:
'''dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"} #Diccionario
for key in dictionary.keys(): #Para llave en el diccionario.keys() (osea en todos los elementos del diccionario)
    print(key, "->", dictionary[key]) #Imprimimos primero la palabra clave y luego su corrrespondiente valor'''

#Con la funcion sorted, se organizara de forma alfabetica el diccionario. Ejemplo:
"""for key in sorted(dictionary.keys()): #Para llave en la lista ordenada de dictionary.keys(). Este ejemplo solo funciona si el anterior esta activo
    print(key, "->", dictionary[key])"""

#Cambiar el valor de una palabra clave en el diccionario es facil, simplemente reemplazarlo. Ejemplo:
'''dictionary = {'gato': 'perro', 'perro': 'chien', 'caballo': 'cheval'}
dictionary['gato'] = 'minou' #Se reemplaza el valor de la palabra clave
print(dictionary)'''

#Agregar una palabra clave y valor nuevos es tambien bastante sencillo, solo se ponen estos mismos sin necesidad de un .append o algo por el estilo. Ejemplo:
'''dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
dictionary['cisne'] = 'cygne' #Primero el nombre de la palabra clave y luego el valor
print(dictionary)'''

#Otra forma es usando el metodo update(). Ejemplo:
'''dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
dictionary.update({"pato": "canard"}) #El nombre del diccionario .update y entre los parentesis las llaves del diccionario y la palabra clave y su valor escritos con la sintaxis de un diccionario
print(dictionary)'''

#Eliminar palabras clave funciona con del al igual que casi todo, al eliminar una palabra clave tambien se elimina su valor. Ejemplo:
'''dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
del dictionary['perro'] #La palabra del, el nombre del diccionario y luego la palabra clave a eliminar
print(dictionary)'''

#Si queremos eliminar directamente el ultimo elemento de la lista, utilizamos el metodo popitem(). Ejemplo:
'''dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
dictionary.popitem() #Nombre del diccionario .popitem y no poner nada en los parentesis
print(dictionary)    # salida: {'gato': 'chat', 'perro': 'chien'}'''

#Programa usando todo lo anterior, el programa trata de poner nombres de estudiantes y sus notas, luego sacar el promedio de estas notas. Atento a la explicacion de cada linea:
'''school_class = {} #Diccionario vacio
while True: #Mientras sea verdad (esto es un bucle infinito)
    name = input("Ingresa el nombre del estudiante: ") #Se pedira el nombre del estudiante
    if name == ' ': #Si el nombre es un espacio, break
        break
    
    score = int(input("Ingresa la calificación del estudiante (0-10): ")) #Luego se pide la nota
    if score not in range(0, 11): #Si la nota no esta entre 0 y 10, break
	    break
    
    if name in school_class: #Si el nombre ya estaba anteriormente en el diccionario
        school_class[name] += (score,) #Se va a alargar la tupla asociada con la nueva calificacion
    else:
        school_class[name] = (score,) #Si no, se crea una nueva entrada
        
for name in sorted(school_class.keys()): #Para el nombre en los datos organizados del diccionario
    adding = 0 #Suma
    counter = 0 #Rango
    for score in school_class[name]: #Para las notas en el diccionario de 1 solo estudiante
        adding += score #Se hace la suma de las notas
        counter += 1 #Se suma 1 al contador por cada vuelta
    print(name, ":", adding / counter) #Finalmente, el programa imprimira el promedio el cual es la suma sobre el contador o rango'''

#Para resumir como interactuan las tuplas y diccionarios aqui, al insertar un nombre, para ese nombre se va a crear una tupla -->
#Esa tupla va a contener las notas del estudiante, por lo cual al ser tupla, estos valores se vuelven inmutables -->
#Al poner un nombre nuevo, se crea una tupla con los valores de ese otro nombre, por lo cual decimos que los nombres son las palabras clave y las tuplas (notas), los valores de esa palabra clave
#Por ultimo y no tanto referente al ejercicio como tal, aparece que un if tiene error de tabulacion, por alguna razon aparece pero realmente no hay error en el programa

#Con el metodo clear(), se pueden eliminar todos los elementos del diccionario y con del, tanto especificamente un elemento como todo el diccionario. Ejemplo:
'''pol_esp_dictionary = {
    "zamek" : "castillo",
    "woda"  : "agua",
    "gleba" : "tierra"
    }
print(len(pol_esp_dictionary))    # salida: 3
del pol_esp_dictionary["zamek"]    # eliminar un elemento
print(len(pol_esp_dictionary))    # salida: 2
pol_esp_dictionary.clear()   # eliminar todos los elementos
print(len(pol_esp_dictionary))    # salida: 0
del pol_esp_dictionary    # elimina el diccionario'''

#Con el metodo copy() se puede copiar un diccionario. Ejemplo:
'''pol_esp_dictionary = {
    "zamek" : "castillo",
    "woda"  : "agua",
    "gleba" : "tierra"
    }
copy_dictionary = pol_esp_dictionary.copy() #Nombre del diccionario copia y luego el nombre del diccionario original .copy()'''

#Al copiar un diccionario en otro, son independientes, por lo cual si se eliminan las palabras de un diccionario, en el otro aun seguiran intactas

#Diccionarios anidados:
Aprendiz={'Nombre'
          :{'Primer nombre':'Pedro',
            'Segundo nombre':'Alberto'},
          'Documento':12345,
          'Ficha':2560664}