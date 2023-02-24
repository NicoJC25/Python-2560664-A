'''Invente un cifrado de texto tipo murcielago o César. Puede utilizar alguna formula matemática para este fin.'''

'''def cifrado_j(cad):
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
print('El codigo con el cifrado "J" es:',cifrado_j(cadena))'''
            
            
def cifrado_j(cad):
    cifrado=24
    codigo_f=''
    for i in cad:
        if (ord(i))>97 and ord(i)<110:
            cifrado-=1
            cifrado1=cifrado+ord(i)
            print(cifrado1)
            codigo_f+=chr(cifrado1)
            cifrado1=0
    print(codigo_f)

cifrado_j('bcdefghijklm')
            
            
            