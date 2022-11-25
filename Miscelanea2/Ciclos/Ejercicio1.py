'''Determinar los divisores de un número introducido por
teclado'''
#Pedir numero
n=int(input("introduzca un numero para determinar sus divisores: "))
i=1
print("Los divisores son: ")
while(n >= i):#Mientras que el numero siga siendo mayor que i, imprimira el numero si es divisor y se sumara 1 a el mismo, re evaluara y asi
 if n%i == 0:
  print(i)
 i+=1