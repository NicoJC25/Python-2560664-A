
def base():
    try:
        pedir=int(input('Elija el primer numero para dividir: '))
        pedir2=int(input('Elija el segundo numero para dividir: '))
        division=pedir/pedir2
    except BaseException:
        print('Lo siento, lo que hiciste no es valido')
        base()
    else:
        print('El resultado de la division es:',division)
    finally:
        print('Fin del bloque try')
    
base()