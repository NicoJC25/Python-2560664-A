'''Solicite un Angulo al usuario en grados. Diga en que cuadrante está. Diga
además en que vuelta está sabiendo que cada 360 grados se completa una
vuelta a la circunferencia. Además diga el resultado en radianes.'''
#Pedir el valor
Angulo=int(input('Ingrese el angulo en forma de grados: '))
Radianes=3.1416*Angulo/180 #Ecuacion a radianes
vuelta=0
#Definir la cantidad de vueltas
if Angulo>=360:
    vuelta=Angulo//360
    Angulo%=360
    if vuelta==1:
        print('Se realizo',vuelta,'vuelta a la circunferencia') #Si es igual a 1, cambiar el mensaje para que tenga sentido
    else:
        print('Se realizaron',vuelta,'vuelta a la circunferencia')
#Definir los rangos de las cuadrantes y la conversion ponerla
if Angulo>=0 and Angulo<=90:
    print('Cuadrante 1,',Radianes,'convertida a radianes')
elif Angulo>90 and Angulo<=180:
    print('Cuadrante 2,',Radianes,'convertida a radianes')
elif Angulo>180 and Angulo<=270:
    print('Cuadrante 3,',Radianes,'convertida a radianes')
elif Angulo>270 and Angulo<=360:
    print('Cuadrante 4,',Radianes,'convertida a radianes')