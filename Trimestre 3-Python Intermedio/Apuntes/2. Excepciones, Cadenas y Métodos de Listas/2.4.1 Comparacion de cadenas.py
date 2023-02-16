#Para comparar cadenas, tambien se usa el mismo conjunto de operadores que con otro tipo de elementos:

'''==
!=
>
>=
<
<='''

#El tema con estas comparaciones es que son diferentes a otras que hemos visto anteriormente. Las cadenas se comparan -->
#mediante los puntos de codigo de cada caracter. Ejemplo:

"""'alpha' == 'alpha' #True
'alpha' != 'Alpha' #True"""

#Cuando ambas cadenas de caracteres empiezan por los mismos caracteres pero luego una de las cadenas tiene mas longitud que la otra -->
#la cadena mas larga es mayor. Ejemplo:

"""'alpha' < 'alphabet' #True"""

#Al momento de comparar, las letras mayusculas se consideran menores en comparacion con las minusculas. Ejemplo:

"""'beta' > 'Beta' #True"""


#Cuando una cadena tiene soo digitos, hay que recordar que un no es un numero, por lo cual la forma de comparar es diferente. Ejemplo:

"""'10' == '010' #False
'10' > '010' #True
'10' > '8' #False
'20' < '8' #True
'20' < '80' #True"""

#Nota: Recordar que la comparacion de cadenas es por el primer caracter, por lo cual en el tercer ejemplo -->
#no estamos diciendo si 10 es mayor a 8, sino si 1 es mayor a 8, al igual que en la cuarta, no estamos comparando si 20 es menor a 8 -->
#sino si 2 es menor a 8.

#Comparar numeros con cadenas de numeros es mala idea ya que al usar un comparador diferente a "==" o "!=", generara un error. Ejemplo:

''''10' == 10 #False
'10' != 10 #True
'10' == 1 #False
'10' != 1 #True
'10' > 10 #TypeError exception'''