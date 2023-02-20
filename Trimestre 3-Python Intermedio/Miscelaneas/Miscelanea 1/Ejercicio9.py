'''Invente un cifrado de texto tipo murcielago o César. Puede utilizar alguna formula matemática para este fin.'''

def cifrado_j(cad):
    code=''
    for i in cad:
        if not i.isalpha(): 
            continue 
        i=i.lower()
        if ord(i)==ord('w'):
            cifr=ord('a')
        elif ord(i)==ord('x'):
            cifr=ord('b')
        elif ord(i)==ord('y'):
            cifr=ord('c')
        elif ord(i)==ord('z'):
            cifr=ord('d')
        else:
            cifr=ord(i)+5
        code+=chr(cifr)
    return(code)

cadena=input('Escriba una frase: ')
print('El codigo con el cifrado "J" es:',cifrado_j(cadena))
            