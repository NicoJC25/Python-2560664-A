'''Solicite al usuario una cantidad numérica que expresa segundos (medida de
tiempo). Exprésela (conviértala) en horas minutos y segundos. Según el caso'''
#Pedir segundos y crear variables
Pedir_segundos=int(input('¿Cuantos segundos quiere convertir?: '))
Minutos=0
Horas=0
#Asignar condiciones para sacar horas y minutos
if Pedir_segundos>=3600:
    Horas=Pedir_segundos//3600
    Pedir_segundos%=3600
if Pedir_segundos>=60:
    Minutos=Pedir_segundos//60
    Pedir_segundos%=60
#Cuando alguno de los valores sea 1 para que no salga en plural la palabra
if Horas==1:
    print('La cantidad de segundos son',Horas,'hora,',Minutos,'minutos y ',Pedir_segundos,'segundos')
elif Minutos==1:
    print ('La cantidad de segundos son',Horas,'horas,',Minutos,'minuto y ',Pedir_segundos,'segundos')
elif Pedir_segundos==1:
    print ('La cantidad de segundos son',Horas,'horas,',Minutos,'minutos y ',Pedir_segundos,'segundo')
else:
    print ('La cantidad de segundos son',Horas,'horas,',Minutos,'minutos y ',Pedir_segundos,'segundos')