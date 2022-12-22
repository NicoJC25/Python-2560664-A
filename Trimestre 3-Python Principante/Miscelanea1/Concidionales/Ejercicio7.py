'''Un obrero necesita calcular su salario semanal, el cual se obtiene de la sig.
manera:
Si trabaja 40 horas o menos se le paga $2600 por hora
Si trabaja más de 40 horas se le paga $2600 por cada una de las primeras 40
horas y $5000 por cada hora extra'''
#Pedir horas
horas = int(input('Ingrese la cantidad de horas: '))
#Establecer ecuacion cuando las horas superen 40
h2 = horas - 40
#Condicion cuando sea menos o mas de 40
if horas < 40:
    horas *= 2600
    print ('El salario semanal es:' ,horas)
elif horas > 40:
    horas = 40
    horas *= 2600
    h2 *= 5000 #Aqui estan guardadas las horas restantes luego de 40
    print ('El salario semanal es:' ,horas + h2)