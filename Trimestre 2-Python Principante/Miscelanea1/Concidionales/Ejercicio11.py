'''Escribir un algoritmo que pida un valor entero que equivale a una cantidad de
DINERO y calcule a cuantos billetes de 50.000, 20.000, 10.000, 5.000, 2.000, y
1.000 equivalen. Si el usuario digita 282000 el programa debe responder cinco
billetes de 50.000, un billete de veinte mil, un billete de diez mil, un billete de
dos mil.'''
#Pedir Dinero
Dinero=int(input('Escoja una cantidad de dinero: '))
#Asignar variables para cada tipo de billete
Cincu=0
Veinte=0
Diez=0
Cinco=0
Dos=0
Mil=0
#Condiciones de acuerdo al valor ingresado, ademas de funciones para guardar el restante y restarle lo del siguiente billete
if Dinero>=50000:
    Cincu=Dinero//50000
    Dinero%=50000
if Dinero>=20000:
    Veinte=Dinero//20000
    Dinero%=20000
if Dinero>=10000:
    Diez=Dinero//10000
    Dinero%=10000
if Dinero>=5000:
    Cinco=Dinero//5000
    Dinero%=5000
if Dinero>=2000:
    Dos=Dinero//2000
    Dinero%=2000
if Dinero>=1000:
    Mil=Dinero//1000
    Dinero&=1000
print ('Se usaron',Cincu,'billetes de 50000,',Veinte,'billetes de 20000,',Diez,'billetes de 10000,',Cinco,'billetes de 5000,',Dos,'billetes de 2000 y',Mil,'billetes de 1000')