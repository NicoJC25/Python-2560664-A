'''El programa mas complicado hasta el momento, toca crear un diccionario intentando recrear el funcionamiento de spotify, hay 2 formas de hacerlo:
1. Agregando una cancion y a esa cancion agregar artista, duracion y genero (Que es el caso de este codigo)
2. Agregando un artista y dentro el genero, la cancion y dentro de la cancion otro diccionario en donde vaya como tal el nombre de la cancion y su respectiva duracion
    Sin importar el metodo, hay que agregar funciones para que el usuario inserte:
La cancion o artista, la info de la cancion o el artista, que pueda buscar un artista, que pueda buscar una cancion, que pueda eliminar un artista
o cancion dependiendo de la forma elegida para hacer, mostrar la cancion mas corta y mostrar la cancion mas larga
    A continuacion, el programa "Spotify"'''
import os #Importamos os (os es una libreria que importa funciones dependientes del sistema operativo)

spotify={} #Spotify sera un diccionario vacio
def cancion(spotify): #Definimos primero para agregar una cancion
    cancion=input('Ingrese el nombre de la cancion: ') #Input
    spotify.update({cancion:{}}) #Se actualiza el diccionario con la clave cancion de la variable input
    return spotify #Retorna

def agregar_info_cancion(spotify): #Definimos para agregar la info a una cancion ya existente
    cancion=input('Ingrese el nombre de la cancion: ') #Ingresa el nombre de la cancion
    if cancion not in spotify: #Revisa si la cancion no esta, si no:
        print('La cancion no se encuentra, agreguela primero') #Soltara un mensaje de que hay que agregarla primero
        return spotify #Retorna para volver al menu principal
    artista=input('Ingrese el nombre del artista: ') #Si si esta la cancion, pide el artista
    genero=input('Ingrese el genero musical: ') #El genero musical
    duracion=input('Ingrese la duracion en formato xx(mm):xx(ss): ') #Y la duracion

    if cancion in spotify: #Si la cancion esta en spotify
        spotify.update({cancion:{'artista':artista,'genero':genero,'duracion':duracion}}) #Se actualizara el diccionario de cancion -->
    return spotify #Con las nuevas claves de artista, genero y duracion y retorna
    
def buscar_artista(spotify): #Definimos para buscar un artista 
    buscar=input('¿Que artista desea buscar?: ') #Input
    for a in (spotify.values()): #a va a revisar cada valor del diccionario
        if buscar==a['artista']: #Si la palabra ingresada es igual a un valor de la clave artista
            print('El artista',buscar,'se encuentra en spotify y su genero es:',a['genero']) #Imprime el nombre encontrado y su genero musical
            return None #Retorna None
    print('El artista no se encuentra, ingrese la cancion con el artista') #Si el artista no se encuentra, imprime este mensaje
    
def buscar_cancion(spotify): #Definimos para buscar una cancion
    buscar=input('¿Que cancion desea buscar?: ') #Input
    for i in sorted(spotify.keys()): #i va a buscar en las claves de spotify
        if buscar==i: #Si la palabra ingresada es igual a alguna cancion agregada
            print('La cancion',buscar,'se encuentra en spotify y su duracion es:',spotify[i]['duracion']) #Imprime la cancion y su duracion
            return None #Retorna None
    print('La cancion no se encuentra, ingrese el nombre primero') #Si la cancion no se encuentra, imprime este mensaje

def eliminar_cancion(spotify): #Definimos para eliminar una cancion
    buscar=input('¿Que cancion desde elminiar?: ') #Input
    for i in sorted(spotify.keys()): #i va a buscar en todas las claves de spotify
        if buscar==i: #Si la palabra ingresada es igual a alguna cancion agregada
            del spotify[i] #Elimina esa cancion junto con sus datos (ya que la cancion es un diccionario)
            print('La cancion',buscar,'fue eliminada correctamente') #Imprime que se realizo correctamente el proceso
            return None #Retorna None
    print('La cancion no se encuentra, ingrese el nombre primero') #Si la cancion no se encuentra, imprime este mensaje
    
def mayor(spotify): #Definimos para buscar la cancion mas larga
    mayor=dict #mayor sera un diccionario
    mayor_valor=0 #mayor valor sera igual a 0
    for a in (spotify.keys()): #a buscara entre todas las claves (canciones)
        minutos=spotify[a]['duracion'][0] #La variable minutos sera el primer numero ingresado en la duracion (primer minuto)
        minutos+=spotify[a]['duracion'][1] #La variable minutos sera tanto el primer numero ingresado anteriormente como el segundo (ambos minutos)
        segundos=spotify[a]['duracion'][3] #La variable segundos sera el tercer numero ingresado en la duracion (primer segundo)
        segundos+=spotify[a]['duracion'][4] #La variable segundos sera tanto el tercer numero ingresado anteriormente como el cuarto (ambos segundos)
        segundos= int(segundos)+int(minutos)*60 #Los segundos seran los numeros enteros de los segundos mas los enteros de los minutos multiplicados por 60
        if mayor_valor<=segundos: #Si la variable mayor valor es menor o igual a segundos (que es asi)
            mayor_valor=segundos #Mayor valor tomara el valor de los segundos
            mayor=a #Y la variable mayor sera igual a "a"
#Pequeño parentesis para explicar esta parte, aqui evalua la primera cancion, luego va a dar la vuelta debido a que tiene que recorrer -->
#Todas las canciones y sus duraciones y realizara la comparativa con cada cancion, y mayor siempre tendra el valor de la cancion mas larga por cada vuelta
    print('La cancion mas larga es',mayor) #Imprime la cancion mas larga
        
def menor(spotify): #Definimos para buscar la cancion mas corta
    menor=dict #menor sera un diccionario
    menor_valor=9e99999 #menor valor sera un numero lo suficientemente grande como para que ninguna duracion supere su valor
    for a in (spotify.keys()): #a buscara entre todas las claves (canciones)
        minutos=spotify[a]['duracion'][0] #La variable minutos sera el primer numero ingresado en la duracion (primer minuto)
        minutos+=spotify[a]['duracion'][1] #La variable minutos sera tanto el primer numero ingresado anteriormente como el segundo (ambos minutos)
        segundos=spotify[a]['duracion'][3] #La variable segundos sera el tercer numero ingresado en la duracion (primer segundo)
        segundos+=spotify[a]['duracion'][4] #La variable segundos sera tanto el tercer numero ingresado anteriormente como el cuarto (ambos segundos)
        segundos= int(segundos)+int(minutos)*60 #Los segundos seran los numeros enteros de los segundos mas los enteros de los minutos multiplicados por 60
        if menor_valor>=segundos: #Si la variable menor valor es mayor o igual a segundos (que es asi)
            menor_valor=segundos #Menor valor tomara el valor de los segundos
            menor=a #Menor sera igual a "a"
#Para entender el funcionamiento de este algoritmo, revisar la documentacion de la funcion anterior, es lo mismo pero en reversa
    print('La cancion mas corta es',menor) #Imprime la cancion mas corta


try: 
    while True: #Mientras sea verdad (bucle infinito)
        os.system ("cls") #Creamos un metodo con os para que al hacer cada vuelta, haga un "clear" de la informacion que ya no es necesaria
        print ('Bienvenido al menu \n Presione 1 para agregar una cancion \n Presione 2 para agregar informacion detallada a una cancion ya agregada \n Presione 3 para buscar un artista \n Preione 4 para buscar una cancion \n Presione 5 para eliminar una cancion \n Presione 6 para mostrar todo lo agregado \n Presione 7 para mostrar la cancion mas larga \n Presione 8 para mostrar la cancion mas corta \n Presione 9 para finalizar el programa: ')
        pedir=int(input(' '))
        #La variable anterior de "pedir" sera in input con un menu que traiga las opciones a elegir para seleccionar que hacer en el programa
        
        match pedir:
            case 1: #Si pedir es igual a 1
                (cancion(spotify)) #Funcion de agregar cancion
            case 2: #Si pedir es igual a 2
                (agregar_info_cancion(spotify)) #Funcion de agregar info de cancion
            case 3: #Si pedir es igual a 3
                (buscar_artista(spotify)) #Funcion de buscar un artista
            case 4: #Si pedir es igual a 4
                (buscar_cancion(spotify)) #Funcion de buscar una cancion
            case 5: #Si pedir es igual a 5
                (eliminar_cancion(spotify)) #Funcion de eliminar una cancion
            case 6: #Si pedir es igual a 6
                for i in sorted(spotify.keys()):
                    None
                print('Todas las canciones con su informacion respectiva agregada son las siguientes:',spotify) #Imprime el diccionario
            case 7: #Si pedir es igual a 7
                mayor(spotify) #Funcion de la cancion mas larga
            case 8: #Si pedir es igual a 8
                menor(spotify) #Funcion de la cancion mas corta
            case 9: #Si pedir es igual a 9
                break #Finaliza con un break el programa
            case _:
                print('El numero no es valido') #Si no se inserta alguno de estos numeros, el programa saca este mensaje y vuelve a pedir
        os.system('pause') #Se invoca de nuevo "os" para que al final de cada proceso realizado, inserte el siguiente mensaje: 
            #Presione una tecla para continuar . . .
        print('Escoja un numero valido')
except:
    print('Ingrese un valor numerico')
        #Besto programa in the world <3