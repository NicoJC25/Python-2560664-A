#Las cadenas de caracteres tambien pueden ser tratadas como listas en muchos casos.
#Por ejemplo, para acceder a cualquiera de los caracteres, se puede aplicar indexacion de la siguiente forma:

'''the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end=' ')

print()'''

#Nota: Tambien funciona con indices negativos

#Tambien se puede iterar una cadena de caracteres de la siguiente forma:

'''the_string = 'silly walks'

for character in the_string:
    print(character, end=' ')

print()'''


#Al igual que con las listas, lo que conocemos de rebanadas se pueden aplicar en las cadenas. Ejemplo:

'''alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])'''



