def look():
    try:
        num1=int(input('que posicion de la lista quiere ver:'))
        list=[1,2,3,4,5,6,7,8,9]
        return(list[num1])
    except LookupError:
        return('no existe esta posicion en la lista')
print(look())