class Producto:
    __counter=0
    def __init__(self,nombre,precio):
        self.__nombre=nombre
        self.__precio=precio
        Producto.__counter+=1

    def getNombre(self):
        print('Nombre del producto:',self.__nombre)
    
    def setNombre(self,nombre):
        self.__nombre=nombre

    def getPrecio(self):
        print('Precio del producto:',self.__precio)
    
    def setPrecio(self,precio):
        self.__precio=precio

    
    def CalcularIva(self):
        try:
            Iva=self.__precio*0.19  
            return Iva
        except (TypeError) as e:
            print(type(e), 'Coloca un valor numerico',sep='\n')