#Pedir un número entre 0 y 9.999 y decir cuantas cifras tiene. Cuando el número exceda los límites emita un mensaje y finalice el programa
#Pedir el numero
numero = int(input('Ponga un numero: '))
#Condiciones en intervalos de acuerdo al valor ingresado
if numero >=0 and numero <=9:
    print ("El numero tiene 1 cifra")
elif numero >=10 and numero <=99:
    print ("El numero tiene 2 cifras")
elif numero >=100 and numero <=999:
    print ('El numero tiene 3 cifras')
elif numero >=1000 and numero <=9999:
    print ('El numero tiene 4 cifras')
else:
    print ('El numero no es valido')