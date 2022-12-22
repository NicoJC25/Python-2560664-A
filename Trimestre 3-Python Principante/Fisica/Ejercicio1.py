'''Realice un programa que dados ciertos datos por el usuario, calcule la energia potencial de una
pelota en una mesa'''




def masa():
    masai=int(input('Ingrese la masa de la pelota: '))
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


def altura():
    alturai=int(input('Ingrese la altura de la mesa: '))
    tipodato_altura=input('Ingrese el tipo de dato de la altura (en formato simplificado ej: m(metros)): ')
    if tipodato_altura=='km':
        alturai=alturai*1000
        return alturai
    elif tipodato_altura=='hm':
        alturai=alturai*100
        return alturai
    elif tipodato_altura=='dam':
        alturai=alturai*10
        return alturai
    elif tipodato_altura=='m':
        return alturai
    elif tipodato_altura=='dm':
        alturai=alturai/10
        return alturai
    elif tipodato_altura=='cm':
        alturai=alturai/100
        return alturai
    elif tipodato_altura=='mm':
        alturai=alturai/1000
        return alturai

masa_final=masa()
altura_final=altura()

EnergiaPotencial= (masa_final * 9.8 * altura_final)
print('la energia potencial es igual a:',EnergiaPotencial,'Jules')