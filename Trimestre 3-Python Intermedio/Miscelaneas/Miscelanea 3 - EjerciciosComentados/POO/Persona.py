class Persona:
    def __init__(self,nombre,documento):
        self.__nombre=nombre
        self.__documento=documento   

    def getNombre(self):
        return self.__nombre

    def setNombre(self,nombre):
        self.__nombre=nombre
    
    def getDocumento(self):
        return self.__documento

    def setDocumento(self,documento):
        self.__documento=documento

ob=Persona('Maria',1023370333)
print(ob.getNombre())
print(ob.getDocumento())
ob.setNombre('Ana')
ob.setDocumento(79965731)
print(ob.getNombre())
print(ob.getDocumento())

class Aprendiz(Persona):
    def __init__(self,nombre,documento,ficha):
        Persona.__init__(self,nombre,documento)
        self.__ficha=ficha

    def getFicha(self):
        return self.__ficha
    
    def getAll(self):
        print(Persona.getNombre(self), Persona.getDocumento(self), self.__ficha, sep='\n')

app=Aprendiz('Pedro',1023370333,12345)
app.getAll()