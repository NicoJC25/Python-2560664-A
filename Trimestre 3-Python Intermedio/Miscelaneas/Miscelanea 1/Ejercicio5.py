'''Solicite cadena e imprimala en todas las formas posibles en cuanto a mayusculas y minusculas'''

cadena=input('Ingrese una o varias frases que quiera convertir: ')

print('Este es el texto en mayusculas: \n',cadena.upper())

print('Este es el texto en minusculas: \n',cadena.lower())

print('Este es el texto con las mayusuclas y minusculas invertidas: \n',cadena.swapcase())

print('Este es el texto con todas las iniciales en mayuscula: \n',cadena.title())