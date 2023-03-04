class Curso:                                                    #Definimos la clase curso
    def __init__(self,titulo):                                  #Creamos un constructor
        self.__titulo=titulo                                    #E indicamos que lo que se ingrese como argumento va a ser el titulo

    def getTitulo(self):                                        #Definimos un metodo para obtener el titulo
        return self.__titulo                                    #Retorna el titulo

class Aprendiz:                                                 #Definimos la clase aprendiz
    def __init__(self,nombre):                                  #Constructor de la clase
        self.__nombre=nombre                                    #Indicamos que lo que se ingrese como argumento va a ser el nombre del aprendiz
        self.__cursos=[]                                        #Creamos una lista para agregar los cursos

    def agregarCurso(self,nombreCursito):                       #Creamos un metodo para agregar el curso y...
        cursito=Curso(nombreCursito)                            #... dentro del metodo se va a asignar que el curso agregado tambien sera el curso en la clase "Curso"
        self.__cursos.append(cursito)                           #Proceso para agregar el nombre del curso como tal a la lista

    def getCursos(self):                                        #Definimos un metodo para obtener el nombre de los cursos
        return self.__cursos                                    #Retorna la lista de los cursos
    
ap=Aprendiz('Sofia')                                            #Ap sera igual a un objeto perteneciente a la clase aprendiz
ap.agregarCurso('Python Basico')                                #Ap hara interaccion con la funcion de agregar curso de forma directa ya que al crear el curso dentro...
ap.agregarCurso('Python Intermedio')                            #... no hay que renombrar mas objetos por fuera

for c in ap.getCursos():                                        #Creamos un bucle for en el que recorrera la lista de cursos...
    print(c.getTitulo())                                        #... e imprimira uno por uno los cursos agregados desde el titulo de la clase curso
    

del ap                                                          #Elimina el aprendiz y con el, los cursos