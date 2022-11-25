def maximo_numeros(numero_maximo):#Definimos la funcion "maximo_numeros"
    numero=0#Variable para guardar los numeros de cada vuelta
    suma=0#Variable para la suma
    while(suma<=numero_maximo): #Mientras que la suma sea menor o igual al numero insetado, numero sumara 1, suma sera re asignada
        numero+=1
        suma=0
        for i in range(0,numero+1): #Para i en el rango de 0 hasta el numero mas 1, suma sumara su valor con i
            suma+=i
    
    return numero

numero_maximo=int(input('Escriba el numero a superar en secuencia: '))#Creamos una variable donde pedir el numero
print('La cantidad de numeros en secuencia sumados necesarios para superar el numero ingresado es:',maximo_numeros(numero_maximo))#Imprimimos la funcion con la variable "numero_maximo"
