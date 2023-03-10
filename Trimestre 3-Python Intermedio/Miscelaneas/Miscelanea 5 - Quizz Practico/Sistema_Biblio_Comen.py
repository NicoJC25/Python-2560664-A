class Lector:
    def __init__(self,nombre,direccion,telefono):
        self.__nombre=nombre
        self.direccion=direccion
        self.telefono=telefono
        self.__pedido=''
        
    def agregarPedido(self,ID_usuario,Titulo_m,Codigo_m):
        Ped=Pedido(ID_usuario,Titulo_m,Codigo_m)
        Ped2=str(Ped.getID_U()),Ped.getTitulo_M(),str(Ped.getCodigo_M())
        self.__pedido=Ped2
        
    def getPedido(self):
        print (self.__pedido)
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre=nombre
        return self.__nombre
    
    def getDireccion(self):
        return self.direccion
    
    def setDireccion(self, direccion):
        self.direccion=direccion
        return self.direccion
    
    def getTelefono(self):
        return self.telefono
    
    def setTelefono(self, telefono):
        self.telefono=telefono
        return self.telefono
    
    def getAll(self):
        print (self.__nombre, self.direccion, self.telefono, sep=(', '))

#De primero tenemos la clase lector del diagrama de clases, en donde vemos que los atributos de la clase son nombre, direccion y telefono.
#A su vez, esta se volvera una clase padre ya que segun la modificacion realizada al diagrama, se decidio este cambio.

#De la linea 2 a la linea 6 esta el constructor con los datos que se van a ingresar. Algunos datos son de caracter privado...
#... y otros de caracter publico dependiendo de lo ajustado al diagrama y sus correspondientes modificaciones.

#De la linea 8 a la 11 se va a crear un metodo para agregar pedido. Esta decision debido a que segun el diagrama...
#... la relacion entre lector y pedido es de composicion, es decir: El pedido se compone del lector, sin lector no hay pedido.
#Asi que segun las reglas de codificacion, se realiza la opcion del programa para que desde el lector, se haga el pedido...
#... significando que si el lector deja de existir, el pedido tambien lo hara.
#La forma de hacerlo es creando un objeto llamado Ped. Ese objeto tomara las caracteristicas de la futura clase pedido...
#... y dependiendo de los argumentos ingresados, este objeto los agregara a si mismo.
#Luego, debido a unos problemas en la impresion del objeto, se creara un segundo objeto que...
#... tomara los valores del primer objeto y los transformara en formato str dentro de una tupla para que sean legibles
#Finalmente, se indica que self.__pedido tendra el valor del segundo pedido, agregando todos los valores de forma efectiva.

#En la linea 13 se crea un metodo para obtener el valor de pedido simplemente retornando el mismo

#De ahi para abajo, todos los metodos son getter (obtener un valor) y setter (cambiar un valor) para...
#... los atributos de la clase (nombre, telefono direccion)

#Como ultimo recalcar que el setter funciona ingresando un parametro en el metodo fuera del self e indicar que...
#... ese parametro sera el nuevo valor de ese atributo.


class Estudiante(Lector):
    def __init__(self, nombre, direccion, telefono, codigo_estudiante):
        Lector.__init__(self, nombre, direccion, telefono)
        self.__codigo_estudiante=codigo_estudiante
        
    def getCodigo_E(self):
        return self.__codigo_estudiante
    
    def setCodigo_E(self):
        self.__codigo_estudiante+=1
        return self.__codigo_estudiante
    
    def getAll(self):
        print(Estudiante.getNombre(self), Estudiante.getDireccion(self), Estudiante.getTelefono(self), self.__codigo_estudiante, sep=(', '))
        

#Esta es la clase Estudiante. Debido a un cambio en el diagrama, a partir de Lector salen 2 subclases nuevas, una de ellas Estudiante.
#La forma de especificar la herencia de esta subclase a partir de la clase padre es al momento de crearla...
#... poner entre parentesis el nombre de la clase padre de la cual va a ser la subclase.    

#De la linea 66 a la 68 se hace el constructor. Este constructor sera diferente ya que de primeras esta el constructor de esta subclase...
#... poniendo todos los atributos que va a tener (tanto los atributos de su clase padre como de esta misma), siendo...
#... el codigo del estudiante el unico atributo en esta clase.
#Luego, hay que de nuevo escribir el constructor pero de la clase padre, ya que es una regla de Python como tal...
#... para que el programa pueda reconocer que es una clase hija. Se pone el nombre de la clase padre...
#... seguida de un punto, luego el __init__ y entre parentesis los atributos de la clase padre como tal
#Tambien se puede llamar al constructor de la clase padre no escribiendo su nombre sino la funcion "super()."
#Por ultimo, se establece el parametro del codigo del estudiante con el self, siendo dato de caracter privado.

#De ahi en adelante los metodos son setter del codigo del estudiante y getter del mismo.

#Por ultimo, hay un metodo para obtener todos los datos, tanto los de la clase padre como los de esta misma clase.
#Aqui la forma de llamar los datos cambia ya que al no estar los getter de cada dato en la misma clase, la forma de invocacion...
#... cambia. Para ello, y esto solo funciona exclusivamente en un caso de herencia, se pone de primeras el nombre...
#... de la clase padre, seguido por un punto y el getter que se quiera invocar. Al ser un metodo, recibe como argumento el self.
#De esta forma, invocamos un dato de una clase padre en una clase hija. Por ultimo recalcar que esta forma de invocacion...
#... si en la clase padre hay un getter. Sin getter del dato que se quiera ver, no sirve.


class Docente(Lector):
    def __init__(self, nombre, direccion, telefono, codigo_docente):
        Lector.__init__(self, nombre, direccion, telefono)
        self.__codigo_docente=codigo_docente
    
    def getCodigo_D(self):
        return self.__codigo_docente
    
    def setCodigo_D(self):
        self.__codigo_docente+=1
        return self.__codigo_docente
    
    def getAll(self):
        print(Estudiante.getNombre(self), Estudiante.getDireccion(self), Estudiante.getTelefono(self), self.__codigo_docente, sep=(', '))
        

#Por este lado tenemos la clase Docente. Esta clase tambien es una clase hija de Lector teniendo como unico dato...
#... el codigo del Docente.

#La forma de escribir esta clase es mas de lo mismo siendo el constructor con todos los datos tanto propios como heredados...
#... e invocando tambien el constructor de la clase padre. Se establece que self.__codigo_docente sera igual a uno de los argumentos...
#... y ya seria el constructor como tal.

#Los otros metodos mas de lo mismo siendo getter y setter del codigo_docente y el getter general con el cambio de la forma de invocacion...
#... de los getters de la clase padre.


class Pedido:
    def __init__ (self, ID_usuario, titulo_material, codigo_material):
        self.__ID_usuario=ID_usuario
        self.titulo_material=titulo_material
        self.__codigo_material=codigo_material
    
    def getID_U(self):
        return self.__ID_usuario
    
    def getTitulo_M(self):
        return self.titulo_material
    
    def setTitulo_M(self, titulo_material):
        self.titulo_material=titulo_material
    
    def getCodigo_M(self):
        return self.__codigo_material
    
    def setCodigo_M(self, codigo_material):
        self.__codigo_material=codigo_material
        return self.__codigo_material
    
    def getAll(self):
        print (self.__ID_usuario, self.titulo_material, self.__codigo_material, sep=(', '))


#Esta es la clase Pedido, una de las clases mas importantes del programa, ya que aqui se podria decir se conecta todo.

#Esta clase recibira como argumentos sus atributos: ID del usuario que hace el pedido, titulo del material y el codigo del material.
#De esta forma, se puede ver en el constructor como se establece lo que va a ser cada dato y si estan de caracter publico o privado.

#El resto de metodos se basan en setters y getters para cada dato y por ultimo el getter general que al no tener ningun tipo de...
#... relacion en formato herencia, solo se escriben los datos de forma normal con el self.


class Material:
    def __init__(self, titulo_material, tipo_material, autor):
        self.__titulo_material=titulo_material
        self.tipo_material=tipo_material
        self.__autor=autor
        
    def getTitulo_M(self):
        return self.__titulo_material
    
    def setTitulo_M(self, titulo_material):
        self.__titulo_material=titulo_material
        return self.__titulo_material
    
    def getTipo_M(self):
        return self.tipo_material
    
    def setTipo_M(self, tipo_material):
        self.tipo_libro=tipo_material
        return self.tipo_material
    
    def getAutor(self):
        return self.__autor
    
    def setAutor(self, autor):
        self.__autor=autor
        return self.__autor
    
    def getAll(self):
        print(self.__titulo_material, self.tipo_material, self.__autor, sep=(', '))


#Esta es la clase Material. Esta clase es algo especial y diferente ya que en el diagrama como tal no estaba establecido pero...
#... debido a las modificaciones, se escribio que se crearia una clase padre llamada Material que tuviera como hijas...
#... la clase Libro y la clase Revista. De esta forma, los datos repetidos se agruparian de mejor forma y mas optimizada

#Entre la linea 167 y 170 esta el constructor de la clase con sus correspondientes parametros que son los atributos de la clase...
#... Titulo del material, Tipo del material y Autor, siendo los datos que se repiten en ambas clases hijas.
#Luego ya se establece por medio del self que valor sera de cual atributo y su caracter publico o privado.

#El resto de metodos se basan en getters y setters de cada atributo y un getter general que al ser una clase padre y no ser...
#... una clase hija, la forma de invocacion de los datos es normal.


class Libro(Material):
    def __init__ (self, titulo_material, tipo_material, autor, editorial, codigo_L):
        Material.__init__(self, titulo_material, tipo_material, autor)
        self.editorial=editorial
        self.__codigo_L=codigo_L
        
    def getEditorial(self):
        return self.editorial
    
    def setEditorial(self, editorial):
        self.editorial=editorial
        return self.editorial
    
    def getCodigo_L(self):
        return self.__codigo_L
    
    def setCodigo_L(self):
        self.__codigo_L+=1
        return self.__codigo_L
    
    def getAll(self):
        print(Material.getTitulo_M(self), Material.getTipo_M(self), Material.getAutor(self), self.editorial, self.__codigo_L, sep=(', '))
        

#Esta es la clase Libro, una clase hija de la anteriormente redactada clase Material. Esta clase va a heredar claramente...
#... todos los atributos de la clase superior y por lo tanto, el uso de sus metodos.
#Cabe aclarar que de nuevo para indicar que es clase hija, al lado del nombre de la clase entre parentesis...
#... va el nombre de la clase padre para indicar esta relacion.

#De primeras esta obviamente el constructor el cual tiene el constructor de la clase como tal y en la siguiente linea...
#... el constructor de la clase padre para indicar que se puedan usar los atributos de esa clase padre.
#Ya luego se establece el valor de los unicos 2 atributos de la subclase como tal que son...
#... la editorial del libro y el codigo del libro. En el diagrama base, este codigo de libro no se encontraba...
#... asi que esta es una modificacion hecha para agregar por asi decirlo un atributo que identifique el libro.

#Mas adelante solo se encuentran metodos getters y setters de cada dato y el getter general que como ya vimos...
#... al ser clase hija, los atributos que se quieran ver de la clase padre tienen que invocarse de una forma especial...
#... nombre de la clase padre, un punto y el getter o funcion que se quiera usar de esta clase padre seguida de los parentesis...
#... ingresando los argumentos correspondientes. Recordar que si el metodo no trae argumentos, si o si tiene que ir el self.


class Revista(Material):
    def __init__ (self, titulo_material, tipo_material, autor, edicion, codigo_R):
        Material.__init__(self, titulo_material, tipo_material, autor)
        self.edicion=edicion
        self.__codigo_R=codigo_R
        
    def getEdicion(self):
        return self.edicion
    
    def setEdicion(self,edicion):
        self.edicion=edicion
        return self.edicion
    
    def getCodigo_R(self):
        return self.__codigo_R
    
    def setCodigo_R(self):
        self.__codigo_R+=1
        return self.__codigo_R
    
    def getAll(self):
        print(Material.getTitulo_M(self), Material.getTipo_M(self), Material.getAutor(self), self.edicion, sep=(', '))
    

#Casi finalizando tenemos la clase Revista, la otra clase hija de la clase padre Material. Realmente no hay mucho cambio...
#... de la forma en que esta escrita la clase Libro, ya que al ser clases hijas de la misma clase padre, su forma...
#... de escritura es muy parecida. Para empezar el nombre de la clase padre entre parentesis al lado del nombre de la clase.

#Dentro de la clase ya esta el constructor: Uno de la clase como tal con todos los atributos que se van a usar...
#... y en la linea que sigue el constructor de la clase padre para indicar el uso de los datos.
#Luego se establecen los dos atributos propios de la subclase: Edicion y codigo de la revista. Recordar que el codigo...
#... es una modificacion hecha al diagrama principal.

#Luego metodos getters y setters para cada dato y el getter general con la forma de invocacion especial al ser clase hija.


class Bibliotecario:
    def __init__ (self, nombre, ID_personal):
        self.__ID_personal=ID_personal
        self.__nombre=nombre
        
    def getNombre(self):
        return self.__nombre
    
    def getID_P(self):
        return self.__ID_personal
    

#Por ultimo esta la clase Bibliotecario. Esta clase cumple como funcion el pasar el pedido al lector...
#... al momento de que se haya realizado la reserva y cuando el lector entrega ya el material al finalizar el tiempo.

#Esta clase tendra como atributos el nombre y el ID de personal. El nombre es una modificacion al diagrama base.

#Luego va el constructor en donde se establece que va a tener cada dato y su caracter publico o privado

#Dos metodos para obtener el nombre del pedido y la ID del empleado


lec=Lector('Roberto','Calle 65B',32422434)
est=Estudiante('Andres','Calle 57C',3005455,1)
doc=Docente('Pablo','Calle 80A',34535322,1)
lib=Libro('Pepe el grillo','Infantil','Pepe','Atenea',1)
rev=Revista('51 minutos','Moda','Pepe','Quinta',1)
Biblio=Bibliotecario('Pedro',1)


#Finalmente esto no va en el programa final pero es una prueba para establecer un objeto para cada clase y ver si todo...
#... se ejecuta como deberia


est.getAll()
doc.getAll()
est.agregarPedido(est.getCodigo_E(),lib.getTitulo_M(), lib.getCodigo_L())
est.getPedido()
lib.getAll()
rev.getAll()
print(Biblio.getID_P())

#Aqui ya es el uso de metodos para obtener o renombrar datos de las clases, la mayoria siendo el uso de los getters generales...
#... de cada clase.

#Lo unico que comentar aqui es que los getters generales es mejor tenerlos en la clase con prints mas que con return ya que...
#... al ser varios datos, en la impresion se ve mal y en uno de los codigos, en la linea 322, se hace algo muy curioso.

#Como nombre al principio del codigo, hay una relacion de composicion entre Lector y Pedido, lo que hace que el Pedido dependa...
#... del Lector ya que este es quien lo compone, asi que el metodo para gregar pedido se hace dentro de la clase del Lector.
#Como se puede ver, por medio de un objeto para Estudiante, se llama el metodo de agregar pedido y se ingresa como argumentos...
#... el ID del usuario (ID del estudiante), titulo del material (Titulo de un libro) y el codigo del material (Codigo de un libro)
#Debido a la forma en como se ajustan los datos dentro de la clase de Lector, se ingresan como argumento datos de otras clases...
#... para el pedido. Asi se hace un tipo de relacion entre todos los datos y clases.

#Por ultimo, como se puede ver, se ponen los datos de un libro en el pedido pero no el de una revista y al ser manual...
#... el proceso es tedioso de andar cambiando los datos cada vez. Esto a la final se arregla con un menu con opciones y...
#... lo que en el fututo se vera llamado procesamiento de archivos. Asi que este programa mas que ser ahora mismo un programa completo...
#... es mas, un modulo. 