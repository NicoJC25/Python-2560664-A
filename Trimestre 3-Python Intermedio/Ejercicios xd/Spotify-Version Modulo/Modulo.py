#!/usr/bin/env python3 


spotify={} 

def cancion(spotify): 
    cancion=input('Ingrese el nombre de la cancion: ') 
    spotify.update({cancion:{}}) 
    return spotify 

def agregar_info_cancion(spotify): 
    cancion=input('Ingrese el nombre de la cancion: ') 
    if cancion not in spotify: 
        print('La cancion no se encuentra, agreguela primero') 
        return spotify 
    artista=input('Ingrese el nombre del artista: ') 
    genero=input('Ingrese el genero musical: ') 
    duracion=input('Ingrese la duracion en formato xx(mm):xx(ss): ') 
    
    if cancion in spotify: 
        spotify.update({cancion:{'artista':artista,'genero':genero,'duracion':duracion}}) 
    return spotify

def buscar_artista(spotify):  
    buscar=input('¿Que artista desea buscar?: ') 
    for a in (spotify.values()): 
        if buscar==a['artista']: 
            print('El artista',buscar,'se encuentra en spotify y su genero es:',a['genero']) 
            return None 
    print('El artista no se encuentra, ingrese la cancion con el artista') 
    
def buscar_cancion(spotify): 
    buscar=input('¿Que cancion desea buscar?: ') 
    for i in sorted(spotify.keys()): 
        if buscar==i: 
            print('La cancion',buscar,'se encuentra en spotify y su duracion es:',spotify[i]['duracion']) 
            return None 
    print('La cancion no se encuentra, ingrese el nombre primero') 
    
def eliminar_cancion(spotify): 
    buscar=input('¿Que cancion desde elminiar?: ') 
    for i in sorted(spotify.keys()): 
        if buscar==i: 
            del spotify[i] 
            print('La cancion',buscar,'fue eliminada correctamente') 
            return None 
    print('La cancion no se encuentra, ingrese el nombre primero') 
    
def mayor(spotify): 
    mayor=dict 
    mayor_valor=0 
    for a in (spotify.keys()): 
        minutos=spotify[a]['duracion'][0] 
        minutos+=spotify[a]['duracion'][1] 
        segundos=spotify[a]['duracion'][3] 
        segundos+=spotify[a]['duracion'][4] 
        segundos= int(segundos)+int(minutos)*60 
        if mayor_valor<=segundos: 
            mayor_valor=segundos 
            mayor=a 
    print('La cancion mas larga es',mayor) 

def menor(spotify): 
    menor=dict 
    menor_valor=9e99999 
    for a in (spotify.keys()): 
        minutos=spotify[a]['duracion'][0] 
        minutos+=spotify[a]['duracion'][1] 
        segundos=spotify[a]['duracion'][3] 
        segundos+=spotify[a]['duracion'][4] 
        segundos= int(segundos)+int(minutos)*60 
        if menor_valor>=segundos: 
            menor_valor=segundos 
            menor=a 
    print('La cancion mas corta es',menor) 
    
