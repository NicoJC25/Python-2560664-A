'''Ejercicio donde hay que eliminar los valores repetidos de una lista'''
#Valores constantes de la lista y crear una lista vacia
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
temporal=[]

for i in my_list:#Para i en la lista principal
    if i not in temporal:#Si i no esta en la segunda lista, 
        temporal.append(i)#Se agregara ese numero
    
print("La lista con elementos únicos:")
print(temporal)




Beatles=[]# paso 1
print("Paso 1:", Beatles)
Pedir=''
Beatles.append('John Lennon')# paso 2
Beatles.append('Paul McCarteny')
Beatles.append('George Harrison')
print("Paso 2:", Beatles)

for i in range(len(Beatles),4+1):# paso 3
    Pedir=input('Inserte el nombre del integrante de la banda: ')
    Beatles.append(Pedir)
print("Paso 3:", Beatles)

del Beatles[3]
del Beatles[3]
print("Paso 4:", Beatles)

Beatles.insert(0,'Ringo Starr')# paso 5
print("Paso 5:", Beatles)

# probando la longitud de la lista
print("Los Fav", len(Beatles))