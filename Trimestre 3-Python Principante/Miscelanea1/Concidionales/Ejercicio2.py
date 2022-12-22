#Escribe un programa que pida tres números y que escriba si son los tres iguales, si hay dos iguales o si son los tres distintos
#Pedir los 3 numeros
numero1 = int(input('Ingrese el primer numero:' ))
numero2 = int(input('Ingrese el segundo numero:' ))
numero3 = int(input('Ingrese el tercer numero:' ))
#Condiciones e impresiones para cada situacion
if numero1 == numero2 and numero2 == numero3:
    print ('Los 3 numeros son iguales')
elif numero1 == numero2 and numero2 != numero3:
    print ('Solo hay 2 numeros iguales')
elif numero1 != numero2 and numero2 == numero3:
    print ('Solo hay 2 numeros iguales')
elif numero1 != numero3 and numero2 == numero3:
    print ('Solo hay 2 numeros iguales')
elif numero1 == numero3 and numero2 != numero3:
    print ('Solo hay 2 numeros iguales')
else:
    print ('Los 3 numeros son diferentes')