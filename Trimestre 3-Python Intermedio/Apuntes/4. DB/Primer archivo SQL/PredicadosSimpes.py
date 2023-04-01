#Predicados simples

#En estos predicados se encuentran los operadores de comparacion. Estos son los signos con sus significados:
# "=" Igual a
# ">" Mayor que
# "<" Menor que
# ">=" Mayor o igual que
# "<=" Menor o igual que
# "<>" "Distinto a"
# "!<" No menor que
# "!>" No mayor que

#Tambien se encuentra la comparacion de caracteres. Para esto se usa el predicado LIKE. 
#Se hace uso de este cuando se requiere precisar la busqueda de campos que contengan combinaciones de caracteres con ciertas condiciones.

#Uso del LIKE:
#<Nombre de la columna> [NOT] LIKE <constante alfanumerico>
#En este caso, el nombre de la columna debe de ser de tipo alfanumerico

#En este caso, las constantes alfanumericas pueden ser caracteres normales, con significado especial, comodines o wildcards.
#A continuacion, algunos comodines a usar:

#"%" = Cadena de longitud aleatoria
#"_" = Caracter no nulo (1 caracter)
#"[x-y]" = Caracter en el rango x hasta y
#"[^x-y]" = Caracter fuera del rango x hasta y

#Ejemplos:

#Ciudades que empiecen por S
#SELECT... FROM...
#WHERE ciudad LIKE "S%"

#Las referencias que no tengan un 4
#SELECT... FROM...
#WHERE referencia LIKE "%[^4]%"

#Las referencias que no tengan un 4,5 o 6
#SELECT... FROM...
#WHERE ciudad LIKE "%[^4-6]%"


#Ahora hay una forma de derectar valores nulos, ya que a veces es necesario para resaltar estas filas. Se hace de la siguiente forma:

#<Nombre columna> IS [NOT] NULL

#Ejemplo:

#Listar los aprendices a los que no se le haya registrado direccion
#SELECT * FROM Aprendiz
#WHERE Direccion is NULL


#Tambien esta el predicado BETWEEN el cual sirve para determinar si un valor esta comprendido o no entre dor valores o ambos inclusive:

#<Nombre de la columna> [NOT] BETWEEN <valor1> AND <valor2>

#Ejemplo:

#Los pacientes entre un estrato 1 y 3
#SELECT * FROM Pacientes
#WHERE Estrato BETWEEN 1 AND 3


#Esta el predicado IN que sirve para averiguar si el resultado de una expresion esta incluido en la lista de valores espcificados:

#<Nombre de la columna> [NOT] IN (variable1, variable2, ...)
#<Nombre de la columna> [NOT] IN (Subconsulta)

#Ejemplo:

#Todos los aprendices de Bogota y Cundinamarca
#SELECT * FROM Aprendiz
#WHERE Ciudad IN ("Bogota", "Cundinamarca")

