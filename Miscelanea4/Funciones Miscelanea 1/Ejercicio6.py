def medio(numero1,numero2,numero3): #Definimos la funcion
    if numero1<numero3 and numero1>numero2: #Intervalos de acuerdo a la condicion
        return numero1
    elif numero1>numero3 and numero1<numero2:
        return numero1
    elif numero2<numero3 and numero2>numero1:
        return numero2
    elif numero2>numero3 and numero2<numero1:
        return numero2
    else:
        return numero3

numero1 = int(input('Ingrese el primer numero: ')) #Creamos una variable donde pedir el primer numero
numero2 = int(input('Ingrese el segundo numero: ')) #Creamos una variable donde pedir el segundo numero
numero3 = int(input('Ingrese el tercer numero: ')) #Creamos una variable donde pedir el tercer numero

print('El valor del medio es',medio(numero1,numero2,numero3)) #Imprimimos la funcion en la que dentro van las 3 variables