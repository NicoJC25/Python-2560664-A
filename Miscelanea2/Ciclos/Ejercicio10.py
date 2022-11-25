'''Algoritmo para hallar el m.c.d de dos números m y n por
el algoritmo de Euclides.'''
#Pedir los dos numeros
n=int(input('Ponga el primer numero : '))
m=int(input('Ponga el segundo numero : '))
while not(m==0): #Mientras m no sea cero, a tendra el valor de n y b el de m
    a=n
    b=m
    if n<0: #Si n es menor a 0, n se restara con a y m=b
        n=-a
        m=b
    if m<0: #Si m es menor a 0, n sera igual a 'a' y m se restara con b
        n=a
        m=-b
    else: #Si no, n sera igual a b y m sera igual a a mod con b
        n=b
        m=a%b
print(n)