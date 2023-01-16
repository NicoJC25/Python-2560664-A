#Durante todo lo que trabajamos en un computador, este pasa por una serie de procesos que permite que -->
#Las funciones solicitadas se ejecuten, de esta forma, tambien ocurre cuando escribimos un programa:
#1. El codigo: Primero esta el codigo, donde escribimos todo lo que queremos hacer
#2. Python: Esta Python en segunda instancia, de por si funcionando como el entorno en el que se escribe el codigo
#3. El sistema operativo: En un tercer campo, esta el sistema operativo donde se aloja Python y en el cual manda las instrucciones
#4. El hardware: Por ultimo esta el hardware que es el que realiza todos los procesos externos para que los pasos -->
#realizados anteriormente puedan cumplirse.

#Quizas esta informacion no es muy util en muchos casos, pero realmente lo llega a ser debido a que en algunos programas -->
#vamos a querer saber donde esta alojado nuestro programa y mucho mas, ahi entra el modulo "platform".

#Con el modulo platform, podemos ver mucha informacion relacionada al dispositivo en el cual se esta escribiendo el programa, -->
#una de sus funciones principales es la llamada "platform", la cual indica todas las capas de un entorno en un escrito -->
#El programa tiene sus variantes que veremos a continuacion:

'''from platform import platform #Importamos platform

print(platform()) #Platform con los parentesis vacios va a arrojar todos los nombres de las capas sin excepcion
print(platform(1)) #Platform con un 1 solo, es "alised", el cual va a arrojar todos los nombres alternos de las capas
print(platform(0, 1)) #Platform poniendo false "aliased" y 1 (True) al otro lado, es "terse", el cual arrojara todos los nombres de la forma mas acortada posible'''

#Con la funcion machine, se conoce exclusivamente el nombre generico del procesador que ejecuta el sistema operativo. Ejemplo:

'''from platform import machine

print(machine())'''

#Con la funcion processor, el programa devuelve el nombre real del procesador si es porsible. Ejemplo:

'''from platform import processor

print(processor())'''

#Con la funcion system, el programa devuelve el nombre generico del sistema operativo usado. Ejemplo:

'''from platform import system

print(system())'''

#Con la funcion version, se conoce la version del sistema operativo. Ejemplo:

'''from platform import version

print(version())'''

#Las siguientes 2 funcione son muy importantes:
#python_implementation permite saber que tipo de Python es el que estamos usando
#python_version_tuple devuelve una tupla de 3 elementos, conformados por la parte mayor de la version, la parte menor y el nivel del parche
#Asi es como se escribe en codigo:

'''from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)'''

#Pagina para ver modulos de Python: https://docs.python.org/3/py-modindex.html

