'''De una cadena diga cuantas vocales tiene, cuantas consonantes,
cuantas vocales con tilde y cuantos caracteres especiales.'''

def caracter_esp(cad):
    cont=0
    for i in cad:
        for c in range(ord(' '),ord('/')):
            if ord(i)==c:
                cont+=1
    print(cont)

def vocal_mayus(cad):
    cont=0
    for i in cad:
        for c in range(ord('A'),ord('Z')):
            if ord(i)==c:
                if ord(i)==65 or ord(i)==69 or ord(i)==73 or ord(i)==79 or ord(i)==85:
                    cont+=1
                else:
                    continue
    print(cont)

frase=input('Ingrese una frase: ')

vocal_mayus(frase)

