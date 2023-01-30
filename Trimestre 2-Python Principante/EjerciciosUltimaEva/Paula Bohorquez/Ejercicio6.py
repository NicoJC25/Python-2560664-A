'''Ingresar 5 caracteres e indicar cuantas veces se repite el carácter "a"'''

cont=0
for i in range(5):
    pedir=input('Escriba un caracter: ')
    if pedir=='a':
        cont+=1

if cont==1:
    print('El caracter "a" se repitió',cont,'vez')
else:
    print('El caracter "a" se repitió',cont,'veces')