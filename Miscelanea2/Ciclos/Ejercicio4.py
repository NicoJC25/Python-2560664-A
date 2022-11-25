'''Determinar cuales y cuantos números perfectos hay entre 1 y
1000?'''
#Para el numero en rango de 1 a 1000, creamos i y contador
for n in range(1,1000+1):
  i=1
  contador=0
  while(n>i): #Mientras que el numero siga siendo mayor a i, solo se contaran los que cumplan la division aumentan 1 en el contador y la i
   if n%i ==0:
    contador+=i 
   i+=1
  if n==contador: #Si el contador tiene el mismo valor que el numero, el numero es perfecto
    print("El numero ", n, " es perfecto")