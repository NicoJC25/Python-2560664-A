'''Pida una cadena por teclado y diga cual es su valor al sumar sus codigos'''

cadena=input('Ingrese una frase: ')

def suma(cad):
    total=0
    for cod in cad:
        total += ord(cod)
    return total

print("El total es:", suma(cadena))


