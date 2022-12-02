'''El usuario deberá ingresar un número y se define si es positivo, negativo o cero'''

numero=int(input('Ingrese un numero: '))
if numero<0:
    print('El numero es negativo')
elif numero==0:
    print('El numero es 0')
else:
    print('El numero es positivo')