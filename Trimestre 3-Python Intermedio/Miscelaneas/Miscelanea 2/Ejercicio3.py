'''Ejemplo con el error "BaseException"'''

try:
    pedir=int(input('Elija el primer numero para dividir: '))
    pedir2=int(input('Elija el segundo numero para dividir: '))
    division=pedir/pedir2
except BaseException:
    print('Lo siento, lo que hiciste no es valido')
    
    



