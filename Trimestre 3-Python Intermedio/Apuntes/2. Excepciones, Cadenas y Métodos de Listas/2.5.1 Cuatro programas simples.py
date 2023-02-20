#Cifrado César

#Este cifrado convierte cada letra de la cadena ingresada en su consecuente.
#Solo funciona con letras latinas y en el caso de la z, para a ser la a

#Ejemplo:


'''text = input("Ingresa tu mensaje: ") 
cipher = '' 
for char in text: 
    if not char.isalpha(): 
        continue 
    char = char.upper() 
    code = ord(char) + 1 
    if code > ord('Z'): 
        code = ord('A') 
    cipher += chr(code) 

print(cipher)'''

'''
Linea 1: #El mensaje a pasar a cifrado
Linea 2: #Donde va a ir el cifrado
Linea 3: #Para char en texto
Linea 4: #Si el caracter actual no es alfabetico
Linea 5: #Ignoralo
Linea 6: #Convierte todo el texto a mayusculas
Linea 7: #En la variable code, transforma los caracteres a su codigo ASCII y sumale 1 
Linea 8: #Si el codigo es mayor al codigo de la letra Z
Linea 9: #Conviertelo en el codigo de la letra A
Linea 10: #Agrega uno a uno los codigos convertidos en caracteres a la variable cipher
Linea 12: #Imprime el codigo final
'''


#Cifrado César inverso

#Este programa es lo mismo que el anterior solo que en vez de la letra que sigue al caracter identificado -->
#es el anterior. Ejemplo:

'''cipher = input('Ingresa tu criptograma: ')
text = ''
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)'''

'''
Linea 7: En la variable code, transforma los caracteres a su codigo ASCII y restale 1 
Linea 8: Si el codigo es menor al codigo de la letra A
Linea 9: Conviertelo en el codigo de la letra Z
'''


#El procesador de numeros

#Este programa, tiene como objetivo que al ingresar varios numeros en forma de cadena, se puedan sumar
#Ejemplo:

'''line = input("Ingresa una línea de números, sepáralos con espacios: ")
strings = line.split()
total = 0
try:
    for substr in strings:
        total += float(substr)
    print("El total es:", total)
except:
    print(substr, "no es un numero.")'''


'''
Linea 1: Ingresar los numeros
Linea 2: Divide los numeros y los agrega a una nueva lista
Linea 3: Variable del total
Linea 4: Agregamos try
Linea 5: Para los elementos de la lista
Linea 6: El total es la suma de los numeros convertidos en flotantes
Linea 7: Imprimir el total de la suma
Linea 8: Si ocurre un error
Linea 9: Imprimir el mensaje
'''


#Validador IBAN


'''iban = input("Ingresa un IBAN, por favor: ")
iban = iban.replace(' ','')

if not iban.isalnum():
    print("Has introducido caracteres no válidos.")
elif len(iban) < 15:
    print("El IBAN ingresado es demasiado corto.")
elif len(iban) > 31:
    print("El IBAN ingresado es demasiado largo.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    iban = int(iban2)
    if iban % 97 == 1:
        print("El IBAN ingresado es válido.")
    else:
        print("El IBAN ingresado no es válido.")'''


