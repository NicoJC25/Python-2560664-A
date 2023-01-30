'''Calcular la operación x n sin utilizar la función pow'''
#Pedir base y exponente, ademas de agregar variable i y pontencia que sera igual a la base
x=int(input('Ponga la base : '))
y=int(input('Ponga el exponente : '))
i=1
potent=x
while(i<y): #Mientras i sea menor al exponente, se ira sumando de 1 en 1 y potencia sera el mismo valor de x multiplicado por si mismo
    i+=1
    potent*=x
if y<=0: #Si el exponente es igual o menor a 0, el resultado de la potencia sera 1
  potent=1
print(potent)