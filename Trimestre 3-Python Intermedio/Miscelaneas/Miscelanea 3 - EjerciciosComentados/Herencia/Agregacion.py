class Aprendiz:                                                     #Definimos una clase aprendiz
    def __init__(self,nombre):                                      #Creamos el constructor
        self.__nombre=nombre                                        #Indicamos que el nombre del aprendiz sera lo que se ingrese como argumento
        self.__cursos=[]                                            #Indicamos que se va a crear una lista llamada cursos
    def agregarCurso(self,nombreCurso):                             #Definimos un metodo para ingresar un curso
        self.__cursos.append(nombreCurso)                           #Forma en que se agrega el curso
    def verCursos(self):                                            #Definimos una funcion para ver los cursos agregados en la lista
        return self.__cursos                                        #Return para ver la lista

class Curso:                                                        #Definimos una clase curso
    def __init__(self,nombreCurso):                                 #Constructor de la clase
        self.__nombreCurso=nombreCurso                              #Indicamos que lo que se ingrese como argumento va a ser el nombre del curso

    def getNombreCurso(self):                                       #Metodo para ver el nombre del curso agregado
        return self.__nombreCurso                                   #Return del nombre
    
ob=Aprendiz('Miguel')                                               #Ob sera un aprendiz
c1=Curso('Python Basico')                                           #Primer curso llamado "Python Basico"
c2=Curso('Python Intermedio')                                       #Segundo curso
c3=Curso('Java Basico')                                             #Tercer curso

ob.agregarCurso(c1)                                                 #Con ob que es el aprendiz, agregamos el primer curso ya hecho con las variables anteriores
ob.agregarCurso(c2)                                                 #Agregamos un segundo curso de la misma forma
ob.agregarCurso(c3)                                                 #Y el tercer curso

for curso in ob.verCursos():                                        #Creamos un bucle for que va a iterar en la lista de los cursos
    print(curso.getNombreCurso())                                   #E imprimira uno por uno los cursos de la lista

del ob                                                              #Eliminamos el objeto de la clase aprendiz...
#print(ob)
print('.....',c1.getNombreCurso())                                  #...para comprobar que aun asi existe el curso
