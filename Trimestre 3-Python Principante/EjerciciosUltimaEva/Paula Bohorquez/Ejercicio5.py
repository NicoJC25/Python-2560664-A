'''Ingresar edad y define si el usuario obtendrá apoyo económico, rango edad de: 5 a 16 años'''

edad=int(input('Ingrese una edad: '))
if edad>=5 and edad <=16:
    print('Felicidades, cuenta con apoyo economico')
else:
    print('Lo sentimos, no cuenta con apoyo economico')