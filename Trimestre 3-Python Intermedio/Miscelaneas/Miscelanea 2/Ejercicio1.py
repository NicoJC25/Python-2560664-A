'''Programa con el error "AttributeError"'''



def attribute(cad):
    try:
        cad.append('Tengo 19 años')
    except AttributeError:
        print('No puedes usar esta funcion o metodo con este tipo de datos D:')
    except:
        print('Algo ocurrió')


attribute(cad=('Hola me llamo Pedro')) 

