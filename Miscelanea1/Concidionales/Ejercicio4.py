
#Pedir una nota de 0 a 10 y mostrarla de la forma: Insuficiente, Suficiente, Bien, etc. Use la escala que prefiera, pero cerciórese que tiene 5 valores
#Pedir nota
nota = float(input('Ingrese la nota: '))
#Condiciones en forma de intervalo de acuerdo al valor ingresado
if nota >=0 and nota <=3:
    print ("RECUPERACION")
elif nota >=4 and nota <=6:
    print ("INSUFICIENTE")
elif nota >=7 and nota <=7.9:
    print ('NOTABLE')
elif nota >=8 and nota <=8.9:
    print ('BIEN')
elif nota >=9 and nota <=10:
    print ('SOBRESALIENTE')
else:
    print ('El numero no es valido')