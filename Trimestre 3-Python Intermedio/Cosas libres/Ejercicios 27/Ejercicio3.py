'''3. se necesita un programa que permita ingresar 3 números y que muestre en la salida cuales son iguales y cuáles no.'''

N1=int(input('Ingrese un numero: '))
N2=int(input('Ingrese un numero: '))
N3=int(input('Ingrese un numero: '))

def compare(N1,N2,N3):
    if N1 == N2 and N2 == N3:
        return ('Los 3 numeros son iguales')
    elif N1 == N2 and N2 != N3:
        return ('Solo hay 2 numeros iguales')
    elif N1 != N2 and N2 == N3:
        return ('Solo hay 2 numeros iguales')
    elif N1 != N3 and N2 == N3:
        return ('Solo hay 2 numeros iguales')
    elif N1 == N3 and N2 != N3:
        return ('Solo hay 2 numeros iguales')
    else:
        return ('Los 3 numeros son diferentes')
    
print(compare(N1,N2,N3))