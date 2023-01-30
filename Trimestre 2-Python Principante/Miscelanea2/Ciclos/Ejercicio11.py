'''Solicitar 2 números al usuario e imprimir el cociente y el
residuo del mayor en el menor sin utilizar la división ni el mod.'''
#Pedir ambos numeros y guardar el valor del primero en otra variable ademas de un contador
n = int(input('Ingrese el primer numero: '))
n2 = int(input('Ingrese el segundo numero: '))
n3 = n
conter=0
if n2>n: #Si el segundo numero es mayor, intercambiaran valores
    n=n2
    n2=n3
while n>=n2: #Mientras el primero es el mayor, el menor le ira restando al mayor mientras que el contador aumentara
    n-=n2
    conter+=1
print ('El cociente es:' ,conter, 'y el residuo es: ' ,n)