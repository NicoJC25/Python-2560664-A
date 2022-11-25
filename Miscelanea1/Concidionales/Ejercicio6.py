'''6. Pida un numero al usuario que representa días del año. Diga a que mes del año
corresponde así. Si el número es menor o igual a 31 indica que esta en enero,
Pero si el número por ejemplo es 32 indica que es el 1 de febrero. No tenga en
cuenta si el año es bisiesto, es decir siempre febrero tiene 28 días.'''
#Pedir cantidad de dias
dia = int(input('Ingrese el dia del año: '))
#Utilizar condiciones en intervalor para cada valor
if dia >0 and dia <=31:
    print ("El mes es Enero")
elif dia >=32 and dia <=59:
    print ("El mes es Febrero")
elif dia >=60 and dia <=90:
    print ("El mes es Marzo")
elif dia >=91 and dia <=120:
    print ("El mes es Abril")
elif dia >=121 and dia <=151:
    print ("El mes es Mayo")
elif dia >=152 and dia <=181:
    print ("El mes es Junio")
elif dia >=182 and dia <=212:
    print ("El mes es Julio")
elif dia >=213 and dia <=243:
    print ("El mes es Agosto")
elif dia >=244 and dia <=273:
    print ("El mes es Septiembre")
elif dia >=274 and dia <=304:
    print ("El mes es Octubre")
elif dia >=305 and dia <=334:
    print ("El mes es Noviembre")
elif dia >=335 and dia <=365:
    print ("El mes es Diciembre")
else:
    print ('El numero no es valido')