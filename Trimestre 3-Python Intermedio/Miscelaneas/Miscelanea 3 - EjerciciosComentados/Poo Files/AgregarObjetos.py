from Aprendiz import *                                          #Importamos la clase Aprendiz con sus metodos
from Curso import *                                             #Importamos la clase Curso con sus metodos

nombre=input('ingrese nombre del aprendiz')                     #Se crea una variable de tipo input para ingresar el nombre del aprendiz
documento=int(input('ingrese documento del aprendiz'))          #Se crea una variable de tipo input para ingresar el documento del aprendiz
ficha=input('ingrese ficha del aprendiz')                       #Se crea una variable de tipo input para ingresar la ficha del aprendiz

ap=Aprendiz(ficha,nombre,documento)                             #Se crea un objeto para aprendiz el cual va a tener como atributos los input anteriormente creados

nombreCurso=input('ingrese nombre del curso')                   #Se crea una variable de tipo input para ingresar el nombre del curso
horas=int(input('ingrese intensidad horaria del curso'))        #Se crea una variable de tipo input y de numeros enteros para ingresar las horas del curso
c1=Curso(nombreCurso,horas)                                     #Se crea un objeto para curso el cual va a tener como atributos los 2 input anteriores
ap.agregarCurso(c1)                                             #Se indica que en la clase aprendiz, se va a agregar el curso anteriormente nombrado

with open('herencia/aprendices.txt','a') as flujo:              
    flujo.write(ap.getFicha()+','+ap.getNombre()+','+str(ap.getDocumento())+'\n') 

#De la linea 15 a la 17, se indica que se va a crear un flujo en un archivo llamado aprendices.txt
#Esto se hace para luego agregar todos los datos escritos en el archivo en una linea de codigo para que luego...
#... cuando en algun momento se quiera volver a ejecutar el programa, los datos queden guardados y no se pierdan por cada ejecucion nueva.

#En la linea 15, se adjunta la ruta relativa debido a que ambos archivos estan en la misma carpeta y luego se coloca la a...
#... debido a que lo que se quiere hacer es adjuntar estos datos en el archivo.

#Por ultimo, en la linea 16 se hace esta forma de adjuntacion poniendo el flujo con un metodo para escribir los datos en el archivo
#Se colocan los metodos get para obtener cada dato e indicar que van agregados ahi. Debido a que al momento de agregar son cadenas diferentes...
#... se utiliza el operador aritmetico "+" para juntar cada cadena de texto y de esta forma queden en la misma linea.
#Por ultimo, tambien entre cada cadena se coloca en str unas comas para indicar la division de cada dato y al final un salto de linea...
#... por si se agregan nuevos datos que estos sean en la linea que sigue.