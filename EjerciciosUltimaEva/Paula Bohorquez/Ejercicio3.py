'''El usuario ingresará una edad y se define si es niño, joven, adulto o anciano'''

edad=int(input('Ingrese una edad: '))

if edad<18:
    print('La persona es un/a niño/a')
elif edad>=18 and edad <30:
    print('La persona es un/a joven')
else:
    print('La persona es un/a adulto/a mayor')