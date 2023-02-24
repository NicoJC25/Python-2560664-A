try:
    numero1=int(input('ingresa primer numero a sumar:'))
    numero2=int(input('ingresa segundo numero:'))
    a=numero1+numero2
    print(a)
except ValueError:
    print('ingrese un numero valido')
