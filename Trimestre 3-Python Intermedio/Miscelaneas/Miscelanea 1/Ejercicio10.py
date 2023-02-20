'''Imprima todas las subcadenas que salen de una cadena comenzando con las dos primeras letras
luego tres primeras y así sucesivamente hasta llegar a la última'''

cadena=input('Escriba las palabras que quiere dividir en subcadenas separadas por espacios: ')

def sub_c(cad):
    lista_subcadenas=(cad.split())
    letra=''
    for i in lista_subcadenas:
        for l in i:
            letra+=l
            print(letra)

sub_c(cadena)