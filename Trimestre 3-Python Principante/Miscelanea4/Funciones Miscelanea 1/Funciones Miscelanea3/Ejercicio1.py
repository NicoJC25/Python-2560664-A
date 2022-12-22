import random
def llenar_lista(lista):#Definimos una funcion para llenar una lista con numeros aleatorios entre 1 y 100 en un rango aleatorio de 10 a 25 numeros
    lista=[round(random.randrange(100))for i in range(random.randint(10,25))]
    return lista

lista=llenar_lista(list)#La variable lista sera igual a la de la funcion anterior
lista.sort()#Se organizara la lista
rango=len(lista)#El rango es la longitud de la lista

def mediana(lista):#Definimos una funcion para la mediana
    mitad=int(rango//2)#La mitad es el rango entre 2
    if rango%2==0:#Si el rango es divisible entre 2, se sumaran los dos valores mas cercanos a la mitad y se dividiran entre 2
        mediana=(lista[mitad-1]+lista[mitad])//2
    else:#Si no, solo tomar el valor central
        mediana=lista[mitad]
    return mediana

print(lista)#Imprimimos la lista
print('La longitud de la lista es:',rango)#Imprimimos el rango
print('La mediana de la lista es:',mediana(lista))#Imprimimos la funcion de mediana