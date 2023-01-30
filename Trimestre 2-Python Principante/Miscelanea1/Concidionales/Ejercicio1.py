#Pedir 3 numeros e indicar cual de ellos es el valor del medio. Ej 11, 2 1000, el valor del medio es 11. No use operadores lógicos
#Pedir los 3 numeros
numero1 = int(input('Ingrese el primer numero: '))
numero2 = int(input('Ingrese el segundo numero: '))
numero3 = int(input('Ingrese el tercer numero: '))
#Intervalos e impresion de acuerdo a la condicion correcta
if numero1<numero3 and numero1>numero2:
    print ('El valor del medio es',numero1)
elif numero1>numero3 and numero1<numero2:
    print ('El valor del medio es',numero1)
elif numero2<numero3 and numero2>numero1:
    print ('El valor del medio es',numero2)
elif numero2>numero3 and numero2<numero1:
    print ('El valor del medio es',numero2)
else:
    print ('El valor del medio es',numero3)