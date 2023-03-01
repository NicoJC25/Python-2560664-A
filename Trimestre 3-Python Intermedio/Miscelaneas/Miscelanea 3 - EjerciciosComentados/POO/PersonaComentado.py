class Persona:                                   #Iniciamos una clase llamada "Persona" con la palabra reservada "class"
    def __init__(self,nombre):                   #Definir la funcion constructora. Esta funcion hace que los procesos del objeto sean inicializados y se pueda manipular
        self.__nombre=nombre                     #Indica que el metodo self.__nombre, tendra el valor de el parametro ingresado en el campo de nombre
        #print('Constructor Activado')           

#Nota: El parametro "self" lo que hace es representar el objeto recien creado. Este parametro puede tener...
#...cualquier nombre pero se recomienda que sea este mismo ya que asi se puede identificar su funcion.

#El uso de los dos guiones bajos luego del self. es para indicar que esta en privado, lo cual que no se puede manipular esa funcion.

    def getNombre(self):                         #Definimos una nueva funcion que tiene como parametro el objeto
        return self.__nombre                     #Retornamos el metodo que se creo anteriormente ya que al estar en privado en la funcion anterior, no habia posibilidad de ver que era lo que habia adentro

    def setNombre(self,nombre):                  #Definimos una funcion que tiene como parametros el objeto y de nuevo un nombre
        self.__nombre=nombre                     #El objeto cambiara su valor a lo que se ingrese en el parametro de nombre

ob=Persona('Maria')                              #Ob será igual a la clase persona que a su vez se le ingresara como parametro el nombre "Maria"

#Nota: Aunque solo se haya ingresado un argumento, es valido ya que self como tal no cambia su valor al ser el objeto y se aplicara...
#... al parametro de la derecha, osea a nombre

print(ob.getNombre())                            #Imprima el resultado del metodo en la funcion getNombre
ob.setNombre('Ana')                              #Se ingresara como argumento el nombre Ana para luego...
print(ob.getNombre())                            #...ejecutar la otra funcion y cambiar el nombre.
#print(type(ob))

class Aprendiz(Persona):
    def __init__(self,nombre,ficha):
        Persona.__init__(self,nombre)
        self.__ficha=ficha

    def getFicha(self):
        return self.__ficha

app=Aprendiz('Pedro',12345)
print(app.getFicha())
print(app.getNombre())