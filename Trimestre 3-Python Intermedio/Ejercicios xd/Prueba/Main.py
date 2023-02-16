from sys import path as ruta
from os import system as Interfaz
ruta.append('E:\Repositorio\Trimestre 3-Python Intermedio\Ejercicios xd\Paquetes') #Ruta absoluta

import Idiomas.Traductores.InglesEspañol as IaE, Idiomas.Traductores.EspañolFrances as EaF, Idiomas.Traductores.EspañolPortugues as EaP, Idiomas.Traductores.EspañolIngles as EaI
import Idiomas.Tipos_P.TipodePalabra as TipoP
import Idiomas.Extensiones.ExtensionEsp as ExtEsp, Idiomas.Extensiones.ExtentionIng as ExtIng, Idiomas.Extensiones.ExtensãoPor as ExtPor, Idiomas.Extensiones.ExtensionFra as ExtFra
try:
    while True:
        Interfaz('cls')
        print('Bienvenido al menú, elija una opcion:\n 1. Traducir una palabra de Ingles a Español y viceversa\n 2. Traducir una palabra de Frances a Español y vicerversa\n 3. Traducir una palabra de Portugues a Español y viceversa\n 4. Buscar si una palabra es sustantivo, adjetivo o verbo\n 5. Escribir la cantidad de letras que tiene una palabra\n 6. Finalizar el programa')
        Menu=int(input('Elija una opcion: '))
        match Menu:
            case 1:
                IaE.buscar_palabra(), EaI.buscar_palabra()
            case 2:
                EaF.search_word()
            case 3:
                EaP.buscar_palabra()
            case 4:
                TipoP.Esp(), TipoP.Ing(), TipoP.Por(), TipoP.Fran()
            case 5:
                ExtEsp.Extension(), ExtIng.Extention(), ExtPor.Portuguese(), ExtFra.France()
            case 6:
                break
            case _:
                print('El numero no es valido')
        Interfaz('pause')
except:
    print('Ocurrio un error desconocido, lo lamento :c')