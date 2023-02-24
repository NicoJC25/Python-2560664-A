def look():
    try:
        num1=int(input('Que posicion de la lista quiere ver: '))
        list=[1,2,3,4,5,6,7,8,9]
        hola=list[num1]
    except LookupError:
        print('No existe esta posicion en la lista')
        look()
    else:
        print(hola)
    finally:
        print('Fin del programa')
    
look()

