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
    
    #def Reservar(self,material):
    
    #def Entregar(self,material):
    
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



class Estudiante(Lector):
    def __init__(self, nombre, direccion, telefono, codigo_estudiante):
        Lector.__init__(self, nombre, direccion, telefono)
        self.__codigo_estudiante=codigo_estudiante
        
    #def Reservar(self,libro):
    
    #def Entregar (self,libro):
    
    def getCodigo_E(self):
        return self.__codigo_estudiante
    
    def setCodigo_E(self):
        self.__codigo_estudiante+=1
        return self.__codigo_estudiante
    
    def getAll(self):
        print(Estudiante.getNombre(self), Estudiante.getDireccion(self), Estudiante.getTelefono(self), self.__codigo_estudiante, sep=(', '))


class Docente(Lector):
    def __init__(self, nombre, direccion, telefono, codigo_docente):
        Lector.__init__(self, nombre, direccion, telefono)
        self.__codigo_docente=codigo_docente
        
    #def Reservar(self,libro):
    
    #def Entregar(self,libro):
    
    def getCodigo_D(self):
        return self.__codigo_docente
    
    def setCodigo_D(self):
        self.__codigo_docente+=1
        return self.__codigo_docente
    
    def getAll(self):
        print(Estudiante.getNombre(self), Estudiante.getDireccion(self), Estudiante.getTelefono(self), self.__codigo_docente, sep=(', '))


class Pedido:
    def __init__ (self, ID_usuario, titulo_material, codigo_material):
        self.__ID_usuario=ID_usuario
        self.titulo_material=titulo_material
        self.__codigo_material=codigo_material
        
    #def Reservar(self, fecha):
    
    #def Entregar(self, fecha):
    
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


class Libro(Material):
    def __init__ (self, titulo_material, tipo_material, autor, editorial, codigo_L):
        Material.__init__(self, titulo_material, tipo_material, autor)
        self.editorial=editorial
        self.__codigo_L=codigo_L
        
    #def Reservar(self, fecha):
    
    #def Entregar(self, fecha):
    
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
        
        
class Revista(Material):
    def __init__ (self, titulo_material, tipo_material, autor, edicion, codigo_R):
        Material.__init__(self, titulo_material, tipo_material, autor)
        self.edicion=edicion
        self.__codigo_R=codigo_R
        
    #def Reservar(self, fecha):
    
    #def Entregar(self, fecha):
    
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
    

class Bibliotecario:
    def __init__ (self, nombre, ID_personal):
        self.__ID_personal=ID_personal
        self.__nombre=nombre
        
    #def Reservar(self, libro):
    
    #def Entregar(self, libro):
    
    def getNombre(self):
        return self.__nombre
    
    def getID_P(self):
        return self.__ID_personal
    
    

lec=Lector('Roberto','Calle 65B',32422434)
est=Estudiante('Andres','Calle 57C',3005455,1)
doc=Docente('Pablo','Calle 80A',34535322,1)
lib=Libro('Pepe el grillo','Infantil','Pepe','Atenea',1)
rev=Revista('51 minutos','Moda','Pepe','Quinta',1)
Biblio=Bibliotecario('Pedro',1)


est.getAll()
doc.getAll()
lec.agregarPedido(est.getCodigo_E(),lib.getTitulo_M(), lib.getCodigo_L())
lec.getPedido()
lib.getAll()
rev.getAll()
print(Biblio.getID_P())