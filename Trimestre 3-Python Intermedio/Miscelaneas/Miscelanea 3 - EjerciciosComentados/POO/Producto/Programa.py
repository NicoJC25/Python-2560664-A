#Intendo de menu

'''from Modulo import *
from os import system as interfaz

try: 
    while True: 
        interfaz ("cls")
        print('Bienvenido al menu\n Presione 1 para ver los datos del producto\n Presione 2 para cambiar los datos del producto\n Presione 3 para ver el IVA del producto \n Presione 4 para salir del programa \n')
        pedir=int(input(' '))
        match pedir:
            case 1:'''
                
from Modulo import *
Prod1=Producto('Harina',10000)
print(Prod1.getNombre)
print(Prod1.getPrecio)