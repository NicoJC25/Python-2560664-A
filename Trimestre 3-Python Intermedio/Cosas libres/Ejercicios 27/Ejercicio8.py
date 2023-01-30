'''8. Se requiere un programa que llene un diccionario y muestre sus valores.'''

diccio={'Pollo':'Chicken',
        'Perro':'Dog',
        'Gato':'Cat',
        'Caballo':'Horse',
        'Conejo':'Rabbit'}

def imp_valores(dict):
    for v in diccio.keys():
        print(dict[v],end='-')

imp_valores(diccio)