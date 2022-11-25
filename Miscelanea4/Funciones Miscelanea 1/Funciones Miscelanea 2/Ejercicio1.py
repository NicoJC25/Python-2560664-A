def inverso(Numero):#Definimos la funcion "inverso"
    Reverso=0
    while Numero>0:#Mientras el numero no sea 0, restante sera la ultima cifra del numero, que luego se sumara al reverso
        Restante=Numero%10
        Reverso=Reverso*10+Restante #Reverso sera su propio valor por 10, sumado del restante
        Numero//=10 #El numero se ira dividiendo en 10 por cada vuelta
    return Reverso

Numero=int(input('Ingrese el numero a revertir: '))#Creamos una variable donde pedir el numero
print(inverso(Numero))#Imprimimos la funcion con la variable "Numero"