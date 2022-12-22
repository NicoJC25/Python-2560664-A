'''15. Diseñar e implementar un programa que solicite a su
usuario un valor no negativo n y visualice la siguiente salida:
1 2 3 ........ n-1 n
1 2 3 ........ n-1
.........
1 2 3
1 2
1'''
#Pedir valor
Cifra = int(input('Ingrese un valor positivo: '))
#Mientras que la cifra sea mayor a 0, una nueva variable llamada number y un for
while Cifra>0:
    number=''
    for i in range (0,Cifra+1): #Para i en el rango desde 0 hasta la cifra insertada, los numeros seran acumulados en numero
        number+=str(i) #En forma de str para que no se sobrepongan
    print (number)
    Cifra-=1 #Se resta 1 para que aparezca el 0