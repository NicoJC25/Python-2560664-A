spotify={}
def artista(spotify):
    artista=input('Ingrese el nombre del artista: ')
    spotify.update({artista:{}})
    return spotify

def agregar_cancion(spotify):
    artista=input('Ingrese el nombre del artista: ')
    if artista not in spotify:
        print('El artista no se encuentra, agreguelo primero')
        return spotify
    can=input('Ingrese una cancion del artista: ')
    genero=input('Ingrese el genero musical: ')
    duracion=input('Ingrese la duracion en formato xx(mm):xx(ss): ')
    if artista in spotify:
        spotify.update({artista:{'Canciones':{'Cancion':can,'Genero':genero,'Duracion':duracion}}})
    return spotify
    
def buscar_artista(spotify):
    buscar=input('¿Que artista desea buscar?: ')
    for a in sorted(spotify.keys()):
        if buscar==a:
            print('El artista',buscar,'se encuentra en spotify y su genero es:',spotify[a]['Canciones']['Genero'])
            return None
    print('El artista',buscar,'no se encuentra en spotify')
    
def buscar_cancion(spotify):
    buscar=input('¿Que cancion desea buscar?: ')
    for i in (spotify.values()):
        if buscar==i['Canciones']['Cancion']:
            print ('La cancion',buscar,'se encuentra en spotify')

def eliminar_artista(spotify):
    buscar=input('¿Que artista desde elminiar?: ')
    for i in sorted(spotify.keys()):
        if buscar==i:
            del spotify[i]
            print('El artista',buscar,'fue eliminado correctamente')

def mayor(spotify):
    mayor=dict
    mayor_valor=0
    for i in (spotify.keys()):
        cancion=spotify[i]
        for a in (cancion.values()):
            print(i)
            print(a)
            minutos=[spotify][i][a]['Duracion'][0]
    print(minutos)

while True:
    import os
    os.system ("cls")
    pedir=int(input('Bienvenido al menu \n Presione 1 para agregar un artista \n Presione 2 para agregar una cancion a un artista ya agregado \n Presione 3 para buscar un artista \n Presione 4 para buscar una cancion \n Presione 5 para eliminar el artista \n Presione 6 para mostrar todo el diccionario \n Presione 7 para mostrar la cancion mas larga \n Presione 8 para mostrar la cancion mas corta \n Presione 9 para finalizar el programa: '))
    if pedir==1:
        (artista(spotify))
    elif pedir==2:
        (agregar_cancion(spotify))
    elif pedir==3:
        (buscar_artista(spotify))
    elif pedir==4:
        (buscar_cancion(spotify))
    elif pedir==5:
        (eliminar_artista(spotify))
    elif pedir==6:
        print(spotify)
    elif pedir==7:
        mayor(spotify)
    elif pedir==9:
        break
    else:
        print('El numero no es valido')
    os.system('pause')