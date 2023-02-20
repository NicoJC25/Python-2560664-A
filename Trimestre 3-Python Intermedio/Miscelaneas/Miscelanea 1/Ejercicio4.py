'''Cuantas veces se repite un caracter dado'''

def repetido(cad,caracter):
    cont=0
    for i in cad:
        if i==caracter:
            cont+=1
    if cont==1:
        print('La letra',letra,'esta repetida',cont,'vez')
    elif cont>1:
        print('La letra',letra,'esta repetida',cont,'veces')
    else:
        print('La letra',letra,'no se encuentra en esta frase')

cadena=input(('Ingrese una frase: '))
letra=input(('Ingrese la letra a buscar: '))
repetido(cadena,letra)

