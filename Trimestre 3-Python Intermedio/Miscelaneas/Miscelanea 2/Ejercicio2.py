'''Ejemplo con el error "KeyError"'''

animales={'Leon':'Terrestre','Aguila':'Aereo','Tiburon':'Acuatico'}

try:
    animales['Gacela']
except KeyError:
    print('Lo siento, esta palabra no esta en el diccionario :c')
except:
    print('Lo siento, ocurrio algo que hizo el programa fallara D:')