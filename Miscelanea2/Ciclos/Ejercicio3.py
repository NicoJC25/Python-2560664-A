'''Determinar si un número es o no es perfecto. Un numero es
perfecto si la suma de sus divisores sin incluir el propio
número es igual a este'''
#Asignar variables y pedir numero
i=1
conter=0
suma=0
n=int(input("introduzca un numero para determinar si es perfecto: "))
#Mientras que el numero siga siendo mayor a 1, se cuentan los que cumplan la division y contador va a tener el mismo valor que i, el cual se suma por cada vuelta 1
while(n > i):
 if n%i ==0:
  conter=i
 i+=1
#Para i en el rango de contador mas 1, el valor suma se sumara 1 por 1 hasta cumplir este rango
for i in range(conter + 1):
 suma+=i
#Si la suma termina siendo igual que el numero original, es perfecto
if n == suma:
 print("El numero ", n, " es perfecto")
else:
 print("El numero ", n, " NO es perfecto")