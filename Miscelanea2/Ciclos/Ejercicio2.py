'''Determinar si un numero es o no es primo'''
#Pedir numero y establecer variables
n=int(input("introduzca un numero para determinar si es primo o no: "))
i=1
c=0#Contador
while(n>i): #Mientras que i no sea mayor al numero, se imprimiran los valores que den la condicion de division y se sumara 1 al contador y a i
 if n%i==0:
  c+=1
 i+=1
if c>2 or n<=1: #Si el contador reconoce que se uso mas de 2 veces (mas de 2 divisores) o el numero es igual o menor a 1, no es primo
 print("el numero NO es primo")
else: 
 print("el numero ES primo")