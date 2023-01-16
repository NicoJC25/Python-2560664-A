def multiplo_5(numero):#Definimos la funcion "multiplo_5"
    i=0
    while i<numero: #Mientras i sea menor al numero, se ira sumando de 5 en 5 hasta el multiplo antes del numero puesto
        if numero%5!=0:#Si no es multiplo de 5, no es valido
            print('El numero no es valido')
        else:
            i+=5
            print(i)
numero=int(input('Escriba el multiplo de 5: '))#Creamos una variable donde pedir el numero
print (multiplo_5(numero))#Imprimimos la funcion con la variable "numero"