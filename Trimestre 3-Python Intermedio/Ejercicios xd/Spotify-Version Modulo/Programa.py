from os import system as interfaz
from Modulo import *

try: 
    while True: 
        interfaz ("cls") 
        print ('Bienvenido al menu \n Presione 1 para agregar una cancion \n Presione 2 para agregar informacion detallada a una cancion ya agregada \n Presione 3 para buscar un artista \n Presione 4 para buscar una cancion \n Presione 5 para eliminar una cancion \n Presione 6 para mostrar todo lo agregado \n Presione 7 para mostrar la cancion mas larga \n Presione 8 para mostrar la cancion mas corta \n Presione 9 para finalizar el programa: ')
        pedir=int(input(' '))
        match pedir:
            case 1: 
                (cancion(spotify)) 
            case 2: 
                (agregar_info_cancion(spotify)) 
            case 3: 
                (buscar_artista(spotify)) 
            case 4: 
                (buscar_cancion(spotify)) 
            case 5: 
                (eliminar_cancion(spotify)) 
            case 6: 
                for i in sorted(spotify.keys()):
                    None
                print('Todas las canciones con su informacion respectiva agregada son las siguientes:',spotify) 
            case 7: 
                mayor(spotify) 
            case 8: 
                menor(spotify) 
            case 9: 
                break 
            case _:
                print('El numero no es valido') 
        interfaz('pause') 
        print('Escoja un numero valido')
except (TypeError, ValueError ) as e:
    print(type(e), e)
    
        #Besto programa in the world <3