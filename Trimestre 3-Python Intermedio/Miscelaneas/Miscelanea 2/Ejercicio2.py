'''Ejemplo con el error "KeyError"'''


def key(dict):
    try:
        dict['Gacela']
    except KeyError:
        print('Lo siento, esta palabra no esta en el diccionario :c')
    except:
        print('Lo siento, ocurrio algo que hizo el programa fallara D:')

animales={'Leon':'Terrestre','Aguila':'Aereo','Tiburon':'Acuatico'}
key(animales)