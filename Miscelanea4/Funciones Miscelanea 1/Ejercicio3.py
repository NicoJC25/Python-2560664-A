def dias_calendario(dia):#Definimos la funcion "dias_calendario"
    if dia >0 and dia <=31:#Intervalos con if
        return "El mes es Enero"
    elif dia >=32 and dia <=59:
        return "El mes es Febrero"
    elif dia >=60 and dia <=90:
        return "El mes es Marzo"
    elif dia >=91 and dia <=120:
        return "El mes es Abril"
    elif dia >=121 and dia <=151:
        return "El mes es Mayo"
    elif dia >=152 and dia <=181:
        return "El mes es Junio"
    elif dia >=182 and dia <=212:
        return "El mes es Julio"
    elif dia >=213 and dia <=243:
        return "El mes es Agosto"
    elif dia >=244 and dia <=273:
        return "El mes es Septiembre"
    elif dia >=274 and dia <=304:
        return "El mes es Octubre"
    elif dia >=305 and dia <=334:
        return "El mes es Noviembre"
    elif dia >=335 and dia <=365:
        return "El mes es Diciembre"
    else:
        return 'El numero no es valido'

dia=int(input('Escriba el numero de días: '))#Creamos una variable donde pedir el numero
print(dias_calendario(dia))#Imprimimos la funcion y dentro la variable "dia"