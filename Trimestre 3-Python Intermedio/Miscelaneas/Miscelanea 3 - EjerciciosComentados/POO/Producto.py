class Producto:
    __counter=0
    def __init__(self,nombre,precio):
        self.__nombre=nombre
        self.__precio=precio
        Producto.__counter+=1

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self,nombre):
        self.__nombre=nombre

    def getPrecio(self):
        return self.__precio
    
    def setPrecio(self,precio):
        self.__precio=precio

    def CalcularIva(self):
        Iva=self.__precio*0.19  
        return Iva
    
Prod1=Producto('Arroz',10000)
Prod2=Producto('Azucar',15000)

print(f'Nombre del primer producto: {Prod1.getNombre()}')
print(f'Precio del primer producto: {Prod1.getPrecio()}')
Prod1.setNombre('Harina')
Prod1.setPrecio(5000)
print(f'Nombre del primer producto cambiado: {Prod1.getNombre()}')
print(f'Precio del primer producto cambiado: {Prod1.getPrecio()}')

print(f'Nombre del segundo producto: {Prod2.getNombre()}')
print(f'Precio del segundo producto: {Prod2.getPrecio()}')
Prod2.setNombre('Huevos')
Prod2.setPrecio(7000)
print(f'Nombre del segundo producto cambiado: {Prod2.getNombre()}')
print(f'Precio del segundo producto cambiado: {Prod2.getPrecio()}')

print(f'IVA del primer producto: {Prod1.CalcularIva()}')
print(f'IVA del segundo producto: {Prod2.CalcularIva()}')

print(f'Contador: {Prod1._Producto__counter}')