'''El usuario deberá ingresar un numero y se defina si está en el rango de 10 a 20, o es mayor a 20'''

numero=int(input('Ingrese un numero: '))
if numero<0:
    print('El numero es negativo')
elif numero==0:
    print('El numero es 0')
elif numero<10:
    print('El numero es menor a 10')
elif numero>=10 and numero<=20:
    print('El numero esta entre 10 y 20')
else:
    print('El numero es mayor a 20')