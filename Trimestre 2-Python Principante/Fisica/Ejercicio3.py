from math import cos, radians

'''Hallar la potencia de un objeto con x masa elevado por un ascensor con x distancia de desplazamiento ejerciendo x fuerza
con un angulo de x grados que tarda x tiempo'''

def trabajo():
    trabajo=fuerza*(desplazamiento*cos(angulo))
    return trabajo

fuerza=int(input('Ingrese la fuerza ejercida: '))
desplazamiento=int(input('Ingrese la distancia de desplazamiento: '))

angulo=int(input('Ingrese el angulo: '))
angulo=radians(angulo)

tiempo=int(input('Ingrese la cantidad de segundos que tarda el proceso: '))
trabajo_total=trabajo()

def potencia(trabajo_total,tiempo):
    potencia=trabajo_total/tiempo
    return potencia

print('La potencia del objeto es de:',potencia(trabajo_total,tiempo),'Watts')