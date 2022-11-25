'''¿Cuáles y cuántos son los números primos comprendidos
entre 1 y 1000?'''
#Para el numero en el rango de 2 (ya que 1 no es primo pero igual lo cuenta el programa) y 1000, asignamos i y un contador
for n in range(2,1000):
  i=1
  c=0
#Dentro del rango, mientras que el numero sea mayor o igual a i, se cuenta solo los que cumpla la division y se aumenta 1 en el contador y en i
  while(n>=i):
   if n%i==0:
    c+=1
   i+=1
  if not c>2 or n <=1: #Si el numero no cumple ninguna de estas condiciones, es primo
   print("el numero ",n," es primo")