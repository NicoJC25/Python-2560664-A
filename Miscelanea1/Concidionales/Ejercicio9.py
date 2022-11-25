#Solicite una fecha al usuario. en formato día, mes y año. Dígale cuanto tiempo ha pasado desde esa fecha hasta hoy o cuanto falta para llegar a esa fecha si es posterior
#Pedir la fecha actual
Dia_de_hoy=int(input('Indique en que dia estamos en numero: '))
Mes_de_hoy=int(input('Indique en que mes estamos en numero: '))
Año_de_hoy=int(input('Indique en que año estamos en numero: '))
#Pedir la fecha ya sea menor o mayor a la actual
Dia=int(input('Ingrese el dia en numero: '))
Mes= int(input('Ingrese el mes en numero: '))
Año=int(input('Ingrese el año en numero: '))
#Convertir tanto la fecha actual como la siguiente a dias
Total=(Año*365)+(Mes*30)+Dia
Total_actual=(Año_de_hoy*365)+(Mes_de_hoy*30)+Dia_de_hoy
#Evaluar si los valores ingresados son validos
if Año<=0:
    print('El valor ingresado no es valido')
elif not (Mes>0 and Mes<=12):
    print('El valor ingresado no es valido')
elif not (Dia>0 and Dia<=30):
    print('El valor ingresado no es valido')
elif Año_de_hoy<=0:
    print('El valor ingresado no es valido')
elif not (Mes_de_hoy>0 and Mes_de_hoy<=12):
    print('El valor ingresado no es valido')
elif not (Dia_de_hoy>0 and Dia_de_hoy<=30):
    print('El valor ingresado no es valido')
else: 
    if Año<Año_de_hoy:
        Total_definitivo=Total_actual-Total
        print ('Han pasado',Total_definitivo,'dias')#Cuando sea menor la fecha ingresada a la actual, restar primero la actual con esa
    elif Año>Año_de_hoy:
        Total_definitivo=Total-Total_actual
        print ('Faltan',Total_definitivo,'dias')#Cuando sea mayor, restar la ingresada con la actual