import random
def llenar_lista(lista):#Definimos una funcion para llenar una lista con numeros aleatorios entre 1 y 100 en un rango aleatorio de 10 a 25 numeros
    lista=[round(random.randrange(100))for i in range(random.randint(10,25))]
    return lista

lista=llenar_lista(list)#La variable lista sera igual a la de la funcion anterior
lista.sort()#Se organizara la lista
rango=len(lista)#El rango es la longitud de la lista

def par(lista):#Definimos una funcion para los procesos relacionados con los numeros pares
    total_pares=0
    par=[x for x in lista if x%2==0]#Lista para sacar aparte los pares
    for x in range(len(par)):#Para x en el rango de la lista de los pares, todos los pares sumados seran igual a "total_pares + par[x]" (par [x] son todos los valores de la lista par)
         total_pares+=par[x]
    return total_pares

def impar(lista):#Definimos una funcion para los procesos relacionados con los numeros impares
    total_impares=0
    impar=[x for x in lista if x%2!=0]#Lista para sacar aparte los impares
    for x in range(len(impar)):#Mismo proceso de suma de impares
        total_impares+=impar[x]
    promedio_impares=(total_impares//len(impar))#El promedio es igual a todos los impares sumados sobre el rango de la lista impar
    return promedio_impares

print('La longitud de la lista es:',rango,'y los valores de la lista son:',lista)#Imprimimos la longitud de la lista principal y sus valores
print('La suma de los pares fue:',par(lista))#Imprimimos la suma de los pares
print ('El promedio de los impares es:',impar(lista))#Imprimimos la suma de los impares