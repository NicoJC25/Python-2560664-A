'''Calcular el máximo de números positivos introducidos por
teclado, sabiendo que metemos números hasta que
introduzcamos uno negativo. El negativo no cuenta.'''
#Asignar variables
n=0
c=0
while(n>=0): #Mientras que el numero sea mayor o igual a 0, va a pedir los numeros y va a aumentar el contador en 1 por cada vuelta
    n=int(input("introduzca numeros.... "))
    if n>=0:
        c+=1
    else:
        print("esta fue la cantidad de numeros positivos registrados",c) #El programa se detiene cuando se inserte un valor negativo