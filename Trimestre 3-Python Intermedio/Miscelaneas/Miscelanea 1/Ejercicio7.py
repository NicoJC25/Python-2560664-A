'''Determinar en que tiempo esta conjugado un verbo'''

def tiempo_v(verbo):
    verbo.lower()
    if verbo[-2:]=='ar' or verbo[-2:]=='er' or verbo[-2:]=='ir':
        print('Esta en tiempo presente')
    elif verbo[-2:]=='ar' or verbo[-2:]=='er' or verbo[-2:]=='ir':
        print('Esta en tiempo pasado')
    elif verbo[-2:]=='ré':
        print('Esta en tiempo futuro')
    else:
        print('La palabra no es un verbo')
    
palabra=input('Ingrese un verbo en cualquier tiempo: ')

tiempo_v(palabra)