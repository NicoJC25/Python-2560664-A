'''Realice un programa que dados ciertos datos por el usuario, calcule la energia cinetica
de un carro en movimiento'''


def masa():
    masai=int(input('Ingrese la masa del carro: '))
    tipodato_masa=input('Ingrese el tipo de dato de la masa (formato simplificado ej: kg(kilogramos)): ')
    if tipodato_masa=='kg':
        return masai
    elif tipodato_masa=='hg':
        masai=masai/10
        return masai
    elif tipodato_masa=='dag':
        masai=masai/100
        return masai
    elif tipodato_masa=='g':
        masai=masai/1000
        return masai
    elif tipodato_masa=='dg':
        masai=masai/10000
        return masai
    elif tipodato_masa=='cg':
        masai=masai/100000
        return masai
    elif tipodato_masa=='mg':
        masai=masai/1000000
        return masai
    else:
        print('El tipo de dato ingresado no es correcto')


def velocidad():
    velocidad=float(input('Ingrese la velocidad del carro: '))
    return velocidad

masa_final=masa()
velocidad_final=velocidad()

EnergiaCinetica=(0.5*masa_final*velocidad_final)
print('La energia potencial es igual a:',EnergiaCinetica,'Jules')