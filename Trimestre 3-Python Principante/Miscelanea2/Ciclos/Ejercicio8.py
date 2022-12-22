'''Determinar cuales son los múltiplos de 5 comprendidos entre
1 y N.'''
#Pedir numero y crear i
n=int(input('Ponga el numero: '))
i=0
while i<n: #Mientras i sea menor al numero, se ira sumando de 5 en 5 hasta el multiplo antes del numero puesto
    i+=5
    print(i)