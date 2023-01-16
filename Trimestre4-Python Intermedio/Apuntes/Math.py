#En este caso, tenemos el modulo math, el cual es de los mas utiles al tener funciones matematicas que resultan -->
#Quizas dificiles de recrear desde 0, entre estas funciones de este modulo, vemos las que pertenecen -->
#A la parte trigonometria:

'''from math import * #Importamos todas las funciones del modulo math
sin(x) #Seno de x
cos(x) #Coseno de x
tan(x) #Tangente de x'''

#Todas estas funciones toman un argumento en forma de radianes (ya que es la el tipo de medida para los angulos) -->
#Y devuelve su correspondiente. Tambien tienen su inverso:

'''from math import *
asin(x) #Arcoseno de x
acos(x) #Arcocoseno de x
atan(x) #Arcotangente de x'''

#Todas las funciones reciben un argumento, verifican que sea correcto y devuelven el respectivon resultado.
#Para trabajar de forma eficaz con todo lo relacionado en los angulos, el modulo proporciona funciones utiles:

'''from math import *
pi #Es el numero "pi"
radians(x) #Convierte x de grados a radianes
degrees(x) #Convierte x de radianes a grados'''

#Ahora un ejemplo de un programa usando estas funciones:

'''from math import pi, radians, degrees, sin, cos, tan, asin #Importar funciones de math

ad=90 #Un numero
ar=radians(ad) #Variable para transformar el numero a radianes
ad=degrees(ar) #Variable para transformar el numero a grados

print(ad==90.) #Evaluar si ad es igual a 90
print(ar==pi/2.) #Evaluar si ar es igual a pi dividido entre 2
print(sin(ar)/cos(ar)==tan(ar)) #Evaluar si el seno de ar sobre el coseno de ar es igual a la tangente de ar
print(asin(sin(ar))==ar) #Evaluar si el arcoseno del seno de ar es igual a ar'''

#Tambien estan los analogos hiperbolicos de cada funcion:

'''from math import *
sinh(x) #El seno hiperbolico
cosh(x) #El coseno hiperbolico
tanh(x) #La tangente hiperbolico
asinh(x) #El arcoseno hiperbolico
acosh(x) #El arcocoseno hiperbolico
atanhh(x) #El arcotangente hiperbolico'''

#Otro gran aspecto es de la exponenciacion, muy util en los programas:

'''from math import *
e #Una constante con un valor aproximado del numero de Euler (e)
exp(x) #El valor de e^x
log(x) #El logaritmo de x
log(x,b) #El logaritmo de x con base b
log10(x) #El logaritmo decimal de x
log2(x) #El logaritmo binario de x

#Agregar tambien:

pow(x,y) #El valor de x^y (aunque esta funcion ya esta incorporada)'''

#Codigo de ejemplo:

'''from math import e, exp, log #Importar funciones de math

print(pow(e,1)==exp(log(e))) #Validar si e elevado a la 1 es igual a e elevado al logaritmo de e
print(pow(2,2)==exp(2*log(2))) #Validar si 2 elevado a la 2 es igual a e elevado a 2 multiplicado por el logaritmo de 2
print(log(e,e)==exp(0)) #Validar si e elevado a la e es igual a e elevado a la 0'''

#El ultimo grupo pertenece a funciones generales tales como:

'''from math import *
ceil(x) #Devuevle el entero mas pequeño mayor o igual que x
floor(x) #Devuelve el entero mas grande menor o igual que x
trunc(x) #El valor de x truncado a un entero
factorial(x) #Devuelve x! (x factorial, tiene que ser un numero positivo y entero)
hypot(x,y) #Devuelve la hipotenusa de un triangulo rectangulo con las longitudes de los catetos iguales'''

#Codigo de ejemplo: 

'''from math import ceil, floor, trunc #Importar funciones de math

x=1.4 
y=2.6

print(floor(x), floor(y)) #El floor de cada numero, es el mismo numero menor o igual al puesto
print(floor(-x), floor(-y)) #El floor en negativo, es el numero menor (mas alejado del 0) que sigue al numero puesto 
print(ceil(x), ceil(y)) #El ceil de cada numero, es el numero mayor que le sigue al puesto
print(ceil(-x), ceil(-y)) #El ceil en negativo, es el numero mayor (mas cercano al 0) que sigue al numero puesto
print(trunc(x), trunc(y)) #El trunc es el mismo numero redondeado
print(trunc(-x), trunc(-y)) #El trunc en negativo sigue siendo el mismo numero redondeado'''