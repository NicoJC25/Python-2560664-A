import random
def llenar_lista(lista):#Definimos una funcion para llenar una lista con numeros aleatorios entre 1 y 100 en un rango aleatorio de 10 a 25 numeros
    lista=[round(random.randrange(100))for i in range(random.randint(10,25))]
    return lista

lista=llenar_lista(list)#La variable lista sera igual a la de la funcion anterior
lista.sort()#Se organizara la lista
rango=len(lista)#El rango es la longitud de la lista

def promedio(lista):#Definimos una funcion para sacar el promedio de la lista
    suma=0
    for i in range(rango):#Para i en el rango de la lista, se sumaran todos sus valores
        suma+=lista[i]
    promedio=suma//rango#El promedio es la suma de los valores sobre el rango de la lista
    return promedio

print('El rango de la lista es:',rango)#Imprimimos la longitud de la lista
print('Los valores de la lista son:',lista)#Imprimimos los valores de la lista
print('El promedio de los valores es:',promedio(lista))#Imprimimos el promedio de la lista

for n in lista:#Indicamos por cada valor de la lista cual es mayor, menor o igual al promedio
    if n<promedio(lista):
        print('El numero',n,'es menor al promedio')
    elif n>promedio(lista):
        print('El numero',n,'es mayor al promedio')
    elif n==promedio(lista):
        print('El numero',n,'es igual al promedio')