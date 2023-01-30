import random
rango=random.randint(2,5)
vector=[[round(random.random()*100)for filas in range (rango)]
        for columnas in range (rango)]
print(vector)
print(vector[0][0])







lista=[round(random.random()*100)for i in range (10)]
print(lista)

impar=[x for x in lista if x%2!=0]
print(impar)

par=[x for x in lista if x%2==0]
print(par)

parimpar=[0 if x%2==0 else x for x in lista]
print(parimpar)



board=[]
for i in range(5):
    row=[[]for i in range (3)]
    board.append([])
print (board)

board=[[]for i in range (3)]
print (board)


'''Ejercicio video 45'''
print('Lista vacia')
Lista_vacia=[]

print(Lista_vacia)

print('\nListas homogeneas')

vocales=['a','e','i','o','u']
print(vocales)

enteros=[1,2,3,4,5]
print(enteros)

decimales=[1.5,2.2,3.3,4.9,5.1]
print(decimales)

booleanos=[True,False,False,True]
print(booleanos)

print('\nListas heterogeneas')

Lista_heterogenea=['Carlos',20,1.7,True]
print(Lista_heterogenea)
'''Ejercicio video 62'''
lista=[1, 'a', True, [1, 2,['f', 'g', 'h']]]
print(lista[0])
print(lista[3][1])
print(lista[3][2][1])

'''Ejercicio video 63'''
matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]

print(f'{matrix[0]} \n{matrix[1]} \n{matrix[2]}')
print(matrix[0][0])#Mostrar el numero 1
print(matrix[1][0])#Mostrar el numero 4
print(matrix[2][1])#Mostrar el numero 8
print(matrix[0][2])#Mostrar el numero 3



'''Ejercicio video 64'''
matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]

print('Mostrar todos los elementos de la matriz fila por fila')
for row in matrix:
    print(row)

print('Mostrar todos los elementos de la matriz elemento a elemento en columna')
for row in matrix:
    for element in row:
        print(element)

print('Mostrar todos los elementos de una matriz en formato de matriz')
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()