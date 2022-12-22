'''persona={'Nombre':{
    'primer_nombre':'Nicolas',
    'primer_apellido':'Juez',
        },'Documento':1023370333}'''

'''dictionary={'gato':'chat','perro':'chien','caballo':'cheval'}'''
#Metodo get
'''print(dictionary.get('gato')) #Otro metodo para obtener un valor de una clave
print(dictionary['gato']) #Metodo mas basico'''
#Eliminar elemento
'''del dictionary['perro'] #Elimina el elemento seleccionado'''
#Metodo update
'''dictionary['pollo']='chicken' #Metodo basico
dictionary.update({'pollo':'chicken'}) #Metodo update'''
#Metodo popitem
'''dictionary.popitem() #Elimina el ultimo elemento de la lista'''
#Metodo items
'''for esp, fr in dictionary.items(): #Convierte cada pareja en tuplas
    print(esp,'=',fr)'''
#Metodo values()
'''for x in dictionary.values(): #Imprime los valores de cada clave
    print(x)'''
#Metodo keys()
'''for y in dictionary.keys(): #Imprime las claves
    print(y)'''

#Ejercicio 1
compra = {} #Diccionario vacio

while True: #Mientras sea verdad (esto es un bucle infinito)
    producto = input("Ingresa el nombre del producto: ") #Se pedira el nombre del estudiante
    if producto =='': #Si el nombre es un espacio, break
        break
    
    precio = int(input("Ingresa el precio del producto: ")) #Luego se pide la nota
    
    if producto in compra: #Si el nombre ya estaba anteriormente en el diccionario
        compra[producto] += (precio,) #Se va a alargar la tupla asociada con la nueva calificacion
    else:
        compra[producto] = (precio,) #Si no, se crea una nueva entrada
        
for producto in sorted(compra.keys()): #Para el nombre en los datos organizados del diccionario
    adding = 0 #Suma
    counter = 0 #Rango
    for precio in compra[producto]: #Para las notas en el diccionario de 1 solo estudiante
        adding += precio #Se hace la suma de las notas
        counter += 1 #Se suma 1 al contador por cada vuelta
    print(producto, ":", adding / counter) #Finalmente, el programa imprimira el promedio el cual es la suma sobre el contador o rango
    
#Ejercicio 2
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