from Nicolas import *
from os import system as interfaz
lista=lista_random(list)

try:
    while True:
        interfaz ('cls')
        print ('Bienvenido al menú, elija una opcion:\n 1. Crear una lista aleatoria\n 2. Sumar los datos de la lista\n 3. Mostrar los pares de la lista \n 4. Mostrar los impares de la lista \n 5. Mostrar el promedio de los elementos \n 6. Mostrar la lista \n 7. Finalizar el programa')
        pedir=int(input(' '))
        match pedir:
            case 1:
                print(lista_random(lista))
            case 2:
                print(sumar_lista(lista))
            case 3:
                print(par(lista))
            case 4:
                print(impar(lista))
            case 5:
                print(promedio(lista))
            case 6:
                print(lista)
            case 7:
                break
            case _:
                print('El numero no es valido')
        interfaz ('pause')
except:
    print('Hubo un error desconocido, vuelve a intentarlo')
                


