from Aprendiz import *                                      #Importamos la clase Aprendiz con todos sus metodos
from Curso import *                                         #Importamos la clase Curso con todos sus metodos

with open('herencia/aprendices.txt','r') as flujo:          
    datos=flujo.read()    
    print(datos)
    #flujo.write('2560664,maria,123')

#El with anterior sirve para abrir el flujo del archivo con los datos guardados y leerlos.
#Esto se hace poniendo la ruta claramente, en este caso relativa y luego el comando "r" que cumple la funcion anteriormente nombrada...
#... osea, leer los datos del archivo.
#Se asigna a una variable llamada datos el flujo con el metodo read para que se cumpla esta lectura y luego se imprime la variable...
#... que en un correcto funcionamiento muestra los datos del archivo

aprendices=[]                                               #Se crea una lista de aprendices que se usara mas adelante
with open('herencia/aprendices.txt','r') as flujo:
    for linea in flujo:
        #print(linea)
        aprendices.append(linea.rsplit())

#El with anterior sirve para agregar en una lista nueva los datos de los aprendices.
#Esto se hace con un proceso parecido al anterior adjuntando la ruta, el comando "r" para la lectura y luego ya cambia un poco este with.
#Se va a crear un ciclo for para indicar que por cada linea en el flujo, se va a agregar como un elemento de la lista
#Con esto nos referimos a que por ejemplo en la posicion 1 de la lista, iria la linea 1 del archivo de los datos completa
#De esta forma en la lista dividimos todos los datos de los aprendices.
#La forma en la que se agrega es poniendo el nombre de la lista con el metodo .append para agregar en la ultima posicion...
#... de la lista un dato y luego entre parentesis el dato que se quiere agregar que en este caso es la variable linea...
#... que como lo dice su nombre, contiene una linea en especifico del archivo de datos. Luego va un metodo mas para linea que es rsplit...
#... este metodo lo que busca es dividir cada linea en diferentes posiciones, indicando que cuando los parentesis de rsplit estan vacios...
#... va a tomar comandos de espacios como en este caso el "\n" para saber en que momento dividir cada posicion de la lista.

datosxlinea=[]                                              #Se crea una lista para cada dato por linea que se usara mas adelante
for aprendiz in aprendices:
    datosxlinea.append(aprendiz[0].split(','))

#En el ciclo for anterior hacemos un proceso para que cada dato de cada linea se pueda dividir y se puedan agregar de esta forma a un objeto.
#Esto se hace creando este ciclo que va a recorrer cada posicion de la lista.
#Ya en la linea 34 como vemos vamos a agregar a la nueva lista cada dato en posiciones diferentes. Como ya vimos en la primera lista...
#... cada elemento de la lista es una linea completa del archivo de datos, asi que para agarrar un dato en especifico...
#... se va a indicar que aprendiz que agarra cada linea como tal, va a buscar dentro de la posicion del elemento que esta buscando.
#Por ejemplo, si el primer elemento de la lista es una linea que contiene los datos: "2560664A,ana,12345"...
#... entonces como se ve en el .append, va a buscar en la posicion 0 de ese elemento, osea tomara el valor de "2560664A" nada mas...
#... y luego lo agregara a la nueva lista. De esta forma solo estamos agarrando un dato como tal.
#Ya para dividirlo utilizamos nuevamente el split que reconoce que por cada coma en laa lista principal se debe separar el dato y volverlo...
#... un elemento diferente a los demas.


#print(ob.getNombre())

print(datosxlinea)                                          #Print para ver la lista con los datos por separado

listaDeObjetos=[]                                           #Se crea otra lista para los objetos como tal que se van creando
for apr in datosxlinea:
     f=apr[0]
     n=apr[1]
     d=apr[2]
     ob=Aprendiz(f,n,d)
     print(ob)
     listaDeObjetos.append(ob)

#El ciclo for anterior busca crear un objeto a partir de los datos que acabamos de sacar del archivo y a su vez agregarlo a una lista de objetos.
#Esto se hace creando un ciclo en donde se va a buscar por cada elemento de la lista.
#Luego, debido a que cada dato esta en una posicion diferente, se indica que el primer dato el cual es el numero de ficha...
#... se va a asignar a una variable llamada f. Ya podemos ver que como tal se asigna indicando la posicion del dato el cual al ser el primero, es la 0
#Luego se repite el proceso con el nombre del aprendiz que esta en la posicion 1 y el numero de documento que esta en la posicion 2
#Ya luego se crea un objeto con las variables anteriormente nombradas y se hace una prueba imprimiendo el objeto.
#La impresion no sera de los valores del objeto como tal ya que no es un getter pero se ve que funciona
#Finalmente, un .append del objeto a la lista de objetos.

for xx in listaDeObjetos:
    print(xx.getNombre())
    print(xx.getDocumento())
    print(xx.getFicha())


#Por ultimo, un ciclo for para imprimir los datos del objeto por medio de los getters
#Se crea una variable "xx" para la lista de objetos y esta variable sera como un objeto ya que se utilizara de esta forma...
#... para acceder a cada getter de los objetos.