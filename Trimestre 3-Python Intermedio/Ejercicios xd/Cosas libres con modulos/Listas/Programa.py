from Modulo import *
from os import system as interfaz
lista=lista_random(list)

try:
    while True:
        interfaz ('cls')
        print ('Bienvenido al menú, elija una opcion:\n 1. Crear una lista aleatoria\n 2. Sumar los datos de la lista\n 3. Mostrar los pares de la lista \n 4. Mostrar los impares de la lista \n 5. Mostrar el promedio de los elementos \n 6. Finalizar el programa \n')
        pedir=int(input(' '))
        
        match pedir:
            case 1:
                print(sumar_lista(lista))
                
print(lista)


print(par(lista))
print(impar(lista))
print(promedio(lista))