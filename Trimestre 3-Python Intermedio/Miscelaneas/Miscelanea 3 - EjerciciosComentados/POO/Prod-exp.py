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
        try:
            Iva=self.__precio*0.19  
            return Iva
        except (TypeError) as e:
            print(type(e), 'Coloca un valor numerico',sep='\n')
    
Prod1=Producto('Arroz',10000)
Prod2=Producto('Azucar',15000)

print(f'Nombre del primer producto: {Prod1.getNombre()}')
print(f'Precio del primer producto: {Prod1.getPrecio()}')
Prod1.setNombre=input('Ingrese otro nombre para el primer producto: ')
Prod1.setPrecio=int(input('Ingrese otro valor para el primer producto: '))
print(f'Nombre del primer producto cambiado: {Prod1.getNombre()}')
print(f'Precio del primer producto cambiado: {Prod1.getPrecio()}')

print(f'Nombre del segundo producto: {Prod2.getNombre()}')
print(f'Precio del segundo producto: {Prod2.getPrecio()}')
Prod2.setNombre=input('Ingrese otro nombre para el segundo producto: ')
Prod2.setPrecio=int(input('Ingrese otro valor para el segundo producto: '))
print(f'Nombre del segundo producto cambiado: {Prod2.getNombre()}')
print(f'Precio del segundo producto cambiado: {Prod2.getPrecio()}')

print(f'IVA del primer producto: {Prod1.CalcularIva()}')
print(f'IVA del segundo producto: {Prod2.CalcularIva()}')

print(f'Contador: {Prod1._Producto__counter}')