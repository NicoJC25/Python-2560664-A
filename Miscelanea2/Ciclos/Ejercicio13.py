'''Solicitar al usuario un número de hasta 9 dígitos e
imprimirlo en orden contrario. Ej. digito 6754 imprimo 4576'''
#Pedir numero y asignar la variable del reverso
Numero=int(input('Ingrese un numero de nueve cifras: '))
Reverso=0
while Numero>0:#Mientras el numero no sea 0, restante sera la ultima cifra del numero, que luego se sumara al reverso
    Restante=Numero%10
    Reverso=Reverso*10+Restante #Reverso sera su propio valor por 10, sumado del restante
    Numero//=10 #El numero se ira dividiendo en 10 por cada vuelta
print(Reverso)