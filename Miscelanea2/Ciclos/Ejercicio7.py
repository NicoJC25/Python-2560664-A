'''Encontrar un número natural n más pequeño tal que la suma
de los n primeros números naturales (1 + 2 + 3 + 4.....)
exceda de una cantidad (máximo) introducida por el teclado.
Es decir cuantos números de la serie de los naturales debo
sumar para superar el dato máximo.'''
#Pedir numero maximo y asignar otro numero, un contador y la suma
data_max=int(input('Introduzca el numero del dato maximo: '))
n=0
contador=0
suma=0
while(suma<=data_max): #Mientras que la suma sea menor o igual al numero insetado, n sumara 1, suma sera re asignada
    n+=1
    suma=0
    for i in range(0,n+1): #Para i en el rango de 0 hasta el numero mas 1, suma sumara su valor con i
        suma+=i
 
print(n,"es el numero natural minimo requerido para superar el dato maximo") #Imprime n