from Aprendiz import *                              #Importamos todos los metodos de la clase Aprendiz que esta en otro archivo
from Curso import *                                 #Importamos todos los metodos de la clase Curso que esta en otro archivov

ap=Aprendiz('2560664A','Diego Suarez',123456)       #Se va a crear un objeto para la clase Aprendiz con los datos de ficha, nombre y N_doc
c1=Curso('Python Intermedio',200)                   #Se va a crear un objeto para la clase Curso con los datos del nombre del curso y duracion (horas)
c2=Curso('Python Avanzado',200)                     #Se va a crear un segundo objeto para la clase curso
#print(c1.getNombre())                              #Imprimir el nombre del curso 1
ap.agregarCurso(c1)                                 #Debido a la relacion de agregacion entre Aprendiz y Curso, se agrega el curso dentro de Aprendiz
ap.agregarCurso(c2)                                 #Mismo proceso de antes pero con el segundo curso.

for curso in ap.getCursos():                        #Ciclo for que va a buscar en cada curso agregado a la clase aprendiz para que...
    print(curso.getNombre())                        #... los imprima uno por uno