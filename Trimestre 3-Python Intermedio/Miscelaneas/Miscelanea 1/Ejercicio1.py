'''Cuantas letras del abecedario estan en la cadena, si estan repetidas cuentela solo una vez'''

abcdario=('aaaaabcdefghijklmnñopqrstuvwxyz')

def abc(cad):
    cantidad_abc=[]
    for letra in cad:
        if letra not in cantidad_abc:
            cantidad_abc.append(letra)
    return len(cantidad_abc)


print('La cantidad de letras en el abecedario es:',abc(abcdario))


'''#Linea 3: Cadena con la que se van a hacer las pruebas
#Linea 5: Definimos la funcion a la que tiene como parametro, la cadena con la que se van a hacer las pruebas
#Linea 6: Se crea una nueva lista donde vamos a agregar los elementos de la cadena sin repetir
#Linea 7: Para la letra en la cadena (buscamos letra por letra en la cadena principal)
#Linea 8: Si la letra no esta en la lista...
#Linea 9: Se va a agregar (con esto, solo agregamos los elementos que no estan en la lista por lo que si aparece uno repetido, no se agrega)
#Linea 10: Retornamos la longitud de la lista con los elementos ya agregados (el return se pone fuera del ciclo --->
#ya que queremos la longitud cuando se terminen de agregar todos los elementos, con eso retorna cuando el ciclo ya acabo su funcion )
#Linea 13: Imprimimos la funcion con un mensaje adjunto :D'''