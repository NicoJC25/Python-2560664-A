#Tambien son aplicables los operadores "in" y "not in" en las cadenas de la siguiente forma:

'''alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alphabet)
print("F" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyz" in alphabet)'''

#El ejemplo anterior con el uso de "in". Ahora un ejemplo con el operador "not in":

'''alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" not in alphabet)
print("F" not in alphabet)
print("1" not in alphabet)
print("ghi" not in alphabet)
print("Xyz" not in alphabet)'''


#A su vez, las cadenas de Python son inmutables como por ejemplo una tupla

#En este caso, no se puede usar la instruccion "del" para eliminar un elemento. Ejemplo:

'''alphabet = "abcdefghijklmnopqrstuvwxyz"
del alphabet[0]'''

#Tampoco se puede usar la instruccion "append" para agregar un elemento al final de la cadena. Ejemplo:

'''alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet.append("A")'''

#Y, debido a la ausencia de "append", tampoco es posible usar la instruccion "insert". Ejemplo:

'''alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet.insert(0, "A")'''

#De todas formas y, al igual que una tupla, tambien hay formas de agregar elementos en la cadena sin romper las reglas de Python. Ejemplo:

'''alphabet = "bcdefghijklmnopqrstuvwxy"

alphabet = "a" + alphabet
alphabet = alphabet + "z"

print(alphabet)'''

#De esta forma, usamos operadores aritmeticos para agregar elementos al inicio o al final de la cadena.


