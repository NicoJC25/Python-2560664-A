'''Telefónica realiza los cálculos del costo de una llamada de teléfono siguiendo
los cálculos así:
Cuando se descuelga el teléfono los primeros 3 minutos (banderazo) cuestan
200 pesos y cada minuto adicional cuesta 50 pesos. Escriba un programa que
permita calcular el costo de una llamada dados los minutos de duración.'''
#Pedir minutos
Minutos=int(input('Ingrese la cantidad de minutos que dura la llamada: '))
Tres_minutos=200 #Establecer cuando sean los primeros 3 minutos
#Condicion cuando ocurra cada situacion
if Minutos<=3 and Minutos>0:
    print ('La llamada costó 200 pesos')
elif Minutos>3:
    Minutos=((Minutos-3)*50)+200 #Ecuacion para determinar el resto de los minutos
    print ('La llamada costó',Minutos)
else:
    print ('El numero ingresado no es valido')