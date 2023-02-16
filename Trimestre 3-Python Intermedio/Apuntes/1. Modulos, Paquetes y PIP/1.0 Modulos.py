#Como ya habiamos visto desde hace tiempo, se pueden importar "Modulos":

#Los modulos son por asi decirlo "Librerias" de otros programadores o de el mismo lenguaje de programacion. De estas librerias -->
#Se pueden importar funciones ya establecidas para optimizar el hecho de tener que usarlas en varios programas -->
#Sin necesidad de crearlas desde 0.

#Aunque ya se habian visto estos modulos desde antes, aqui se especifica todo acerca de ellos y puntos clave:

#Se pueden importar varios modulos a la vez de la siguiente manera:
'''import mod1
import mod2, mod3, mod4 #Se separan por medio de una "," cada modulo elegido para importar'''

#Tambien hay otra forma mas estetica de realizarlo y es hacerlo uno por uno en lineas diferentes:

'''import mod1
import mod2
import mod3'''

#Como ya se sabe, al importar un modulo de la forma anterior y usar alguna de sus funciones, se pone el nombre del modulo -->
#Seguido de un punto y luego el nombre de la funcion. Ejemplo:

'''import math

math.acos(8)'''

#Claramente esta forma de importar funciones es un poco incomoda por todo el trabajo que lleva, asi que para ello eciste una forma de -->
#Importar estas funciones sin necesidad de poner el "." y tambien de importar funciones especificas. Ejemplos:

'''from math import * #Este metodo importa todas las funciones del modulo "math"

acos(8) #De esta forma se pueden usar solo poniendo el nombre de la funcion'''

#Ejemplo 2:

'''from math import acos #Aca solo se importa una funcion en especifico

acos(8)'''

#Ejemplo 3:

'''from math import acos, pi, sqrt #Aca se importa mas de 1 funcion especifica

acos(8), pi, sqrt(2) #Aca se ve que se pueden usar'''

#Tambien hay una forma de importar funciones especificas y a su vez cambiar su nombre. Ejemplo:

'''from math import pi as tres #Aca importamos "pi" y a la vez le cambiamos el nombre para que sea "tres"

tres #Aca ya se usa la palabra "tres" en vez de "pi" (tres se vuelve una palabra reservada por lo tanto)'''

#Nota: Este cambio de nombre no lo hace de forma global en la libreria, solo aplica en el programa que se esta usando -->
#Por lo cual aun sigue llamandose "pi" en otros programas diferente a ese

#El cambio de nombre tambien aplica para un modulo como tal. Ejemplo:

'''import math as mates

mates.pi'''