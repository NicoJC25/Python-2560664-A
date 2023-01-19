#Ahora bien, ahora vamos a ver como crear un modulo totalmente propio y como usarlo en nuestros archivos
#Para esto, tomar como referencia la carpeta "Ejemplos", los archivos "main" y "module".

#Lo primero es crear dos archivos, uno totalmente vacio llamado "module.py" y otro llamado "main.py" -->
#en el archivo de module no vamos a escribir nada pero en el de main, vamos a escribir "import module" y lo vamos a ejecutar.
#Nota: Fundamental tener ambos archivos en la misma carpeta, para que esto funcione

#Ahora bien, luego de ejecutarse, si no ocurre nada, es porque todo salio bien, hemos importado el modulo.
#A su vez, ha aparecido una carpeta llamada "__pycache__" la cual trae un archivo con un nombre dependiendo del tipo de Python usado y su version.
#Este archivo lo que hace es, en un lenguaje que python interpreta facilmente, traducir las instrucciones del modulo -->
#hacia el archivo principal para que la lea bien el programa y pueda ejecutar sus funciones.

#Ahora, vamos a poner un proceso en el archivo module, en este caso un print que dice lo siguiente: (recordar ver los archivos en la carpeta ejemplo)

'''print('Me gusta ser un modulo')'''

#Si se ejecuta en el archivo de module, sale este mensaje, al igual que si vamos al main, se imprime este mismo mensaje.
#Python realiza la importacion del modulo 1 sola vez ya que si por ejemplo, un modulo (mod2) tiene la instruccion (import mod1) -->
#y entonces un archivo principal tiene como instrucciones (import mod1) e (import mod2), entonces se pensaria que se importaria 2 veces -->
#las mismas instrucciones pero solo se ejecutan 1 vez, ya que Python recuerda si esas instrucciones ya fueron importadas anteriormente.

#Luego, en el archivo de module, vamos a poner una nueva instruccion:

'''print(__name__'''

#Esta instruccion, al imprimirse en ese mismo archivo, suelta el nombre "__main__" -->
#pero, si se imprime en el archivo main, sale lo siguiente: "module"
#Si se imprime la funcion en el archivo base, sale que es main, osea del que se esta haciendo la funcion primero -->
#Pero, si se imprime en un archivo diferente, sale el nombre del archivo de donde viene la funcion principal.

#Ahora, se puede usar esa variable para saber el contexto en el que se activo el archivo de la siguiente forma:

'''if __name__ == "__main__":
    print("Yo prefiero ser un módulo")
else:
    print("Me gusta ser un módulo")'''

#Tambien se puede usar de formas mas inteligentes para revisar si en un modulo con muchas funciones complejas -->
#todas funcionan correctamente.

#Para saber cuantas veces han sido invocadas las funciones, se necesita un contador de la siguiente forma:

'''counter = 0

if __name__ == "__main__":
    print("Yo prefiero ser un módulo")
else:
    print("Me gusta ser un módulo")'''

#De esta forma, se puede ejecutar la variable directamente en el otro archivo aunque puede traer efectos secundarios:

'''import module
print(module.counter)'''

#Lo que pasa es que si este modulo claramente termina en manos de otras personas, si no son de confiar, pueden ver esa variable personal o privada.
#Python no tiene como ocultar a otros las variables, solo se puede informarles a los demas que es tuya, que la pueden leer pero no modificarla.
#Esto se hace poniendo uno o dos guiones bajos antes de la variable (_conter) o (__conter)

#Ahora vamos a poner funciones dentro del modulo, una donde se sume los resultados de una lista y otra donde se multipliquen los resultados de otra lista:

'''#!/usr/bin/env python3 

""" module.py - Un ejemplo de un módulo en Python """

__counter = 0


def suml(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum


def prodl(the_list):
    global __counter    
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod


if __name__ == "__main__":
    print("Yo prefiero ser un módulo, pero puedo realizar algunas pruebas por ti")
    my_list = [i+1 for i in range(5)]
    print(suml(my_list) == 15)
    print(prodl(my_list) == 120)'''

#Comentar que, la linea donde comienza con un "#!" tiene como funcion indicar en sistemas operativos Unix o similares -->
#como debe ejecutar el mismo el contenido del archivo, se usa mucho en entornos con servidores web y es muy importante adjuntarla.
#Antes de cada programa, se debe escribir la funcion del programa tanto en forma de una linea o multilinea, esto se llama "doc-string".
#Ya se pueen importar las funciones "suml()" y "prodl()".
#Tambien se implementa el uso de __name__ para saber si el archivo es ejecutado de forma independiente

#Ahora vamos a poner a prueba el modulo en el otro archivo utilizando las siguientes instrucciones:

'''from module import suml, prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))'''

#Por ultimo, queda agregar que si por alguna razon, el archivo principal y el modulo no estan en la misma carpeta, se hace lo siguiente:
#Hay que saber que Python tiene una funcion para saber como se almacenan las ubicaciones cuando Python tiene que buscar un modulo al importarlo -->
#esta funcion se llama "path" y se encuentra en el modulo "sys", se puede importar de la siguiente forma:

'''import sys

for p in sys.path:
    print(p)'''

#Al ajecutarlo, sale toda la ruta por la que Python busca el modulo importado, de forma que se pueden ver varias carpetas y archivos.

#Para solucionar el problema de los archivos en carpetas separadas, se puede agregar desde la variable path, que Python busque en la -->
#carpeta en donde esta el modulo que se desea importar, seria de la siguiente forma:

'''from sys import path

path.append('..\\modules')

import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))'''

#Se han utilizado dos "\\" debido a que con uno se usa para escapat de otros caracteres.
#Se ha usado el nombre relativo de la carpeta, solo funcionara si se inicia el archivo "main" directamente desde la carpeta de inicio -->
#y no podra funcionar si el directorio actual no se ajusta a la ruta relativa, por lo cual, se puede usar una ruta absoluta para evitar problemas:

'''path.append('C:\\Users\\user\\py\\modules')'''

#Se puede usar tanto append como insert si no se desea que sea el ultimo elemento de la lista de rutas.