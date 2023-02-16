#Ahora, veremos algunos metodos utiles de cadenas.

#El metodo "capitalize".

#Este metodo, lo que hace es de una cadena de caracteres, que la primera posicion de la cadena este en mayuscula y el resto de la cadena en minuscula.
#Esto lo hace creando una cadena diferente con estos elementos ya que las cadenas al ser inmutables, no se puede editar la original. Ejemplo:

'''print("Alpha".capitalize()) #Arroja como resultado el mismo ya que ya esta en las condiciones del mismo metodo
print('ALPHA'.capitalize()) #Arroja "Alpha"
print(' Alpha'.capitalize()) #Arroja todo en minusculas ya que pone en mayuscula la primera posicion pero, al ser un espacio en blanco, no lo puede realizar
print('123'.capitalize()) #Arroja lo mismo ya que no son letras
print("αβγδ".capitalize()) #Arroja la primera en mayuscula y el resto de la misma forma'''


#El metodo "center"

#Este metodo, centra una cadena de caracteres de acuerdo al campo de ancho especificado
#Si la cantidad de campo de ancho especificado es menor o igual a la cantidad de caracteres de la cadena, no ocurrira nada -->
#ya que la misma funcion cuenta esta cantidad de caracteres como parte del ancho especificado. Ejemplo:

'''print('[' + 'Beta'.center(2) + ']') #No ocurre nada ya que el ancho especificado es menor a la cantidad de elementos en la cadena
print('[' + 'Beta'.center(4) + ']') #No ocurre nada ya que el ancho especificado es igual a la cantidad de elementos en la cadena
print('[' + 'Beta'.center(6) + ']') #Ocurre ancho de 2 espacios'''


#El metodo "endswitch"

#Este metodo, indica si de acuerdo al argumento ingresado, si esa parte especifica de codigo está al final de la cadena, tanto con un elemento como con varios. Ejemplo:

'''t = "zeta"
print(t.endswith("a")) #True debido a que esta el ultimo elemento
print(t.endswith("A")) #False debido a que esta en minuscula
print(t.endswith("et")) #False debido a que aunque son elementos, no estan en los ultimos
print(t.endswith("eta")) #True debido a que son los 3 ultimos elementos'''


#El metodo "find"

#Este metodo, al igual que con "index", arroja la posicion en la que esta un elemento de una cadena.
#La diferencia es que al no aparecer ningun elemento, imprime el numero "-1" y, que solo aplica para cadenas. Ejemplo:

'''t = 'theta'
print(t.find('eta')) #Imprime "2" ya que el primer elemento por buscar esta en la tercera posicion
print(t.find('et')) #Imprime "2" por la misma razon que el anterior
print(t.find('the')) #Imprime "0" ya que el primer elemento por buscar esta en la primera posicion
print(t.find('ha')) #Imprime "-1" ya que los elementos no está en la cadena'''

#Tambien se puede hacer que busque un elemento desde una posicion en especifico. Ejemplo:

'''print('kappa'.find('a', 2))''' #El segundo numero indica desde donde se va a iniciar la busqueda

#Una forma de aplicarlo en un texto largo puede ser asi:

'''the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the') #"fnd" va a ser una variable donde se almacene la posicion del elemento "the"
while fnd != -1: #Mientras fnd sea diferente de -1
    print(fnd) #Imprime fnd
    fnd = the_text.find('the', fnd + 1) #en fnd, se iran agregando cada posicion de cada vez que se imprime el elemento "the"''' 

#Tambien se pueden agregar 3 parametros para el metodo find:
'''print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))'''

#El tercer parametro indica que posicion se va a omitir para la busqueda


#El metodo "isalnum"

#Este metodo, hace que al agregar una cadena, si esta tiene solo letras o digitos, imprima True. Pero si no, imprime False. Ejemplo:

'''print('lambda30'.isalnum()) #True
print('lambda'.isalnum()) #True
print('30'.isalnum()) #True
print('@'.isalnum()) #False
print('lambda_30'.isalnum()) #False
print(''.isalnum())''' #False


#El metodo "isalpha"

#Este metodo, hace lo mismo que el anterior pero solo con letras. Ejemplo:

'''print("Moooo".isalpha()) #True
print('Mu40'.isalpha()) #False'''


#El metodo "isdigit"

#Este metodo, hace lo mismo que los anteriores pero solo con digitos. Ejemplo:

'''print('2018'.isdigit()) #True
print("Year2019".isdigit()) #False'''


#El metodo "islower"

#Este metodo, solo acepta letras minusculas. Ejemplo:

'''print("Moooo".islower()) #False
print('moooo'.islower()) #True'''


#El metodo "ispace"

#Este metodo, solo acepta espacios en blanco. Ejemplo:

'''print(' \n '.isspace()) #True
print(" ".isspace()) #True
print("mooo mooo mooo".isspace()) #False'''


#El metodo "isuper"

#Este metodo, solo acepta mayusculas. Ejemplo:

'''print("Moooo".isupper()) #False
print('moooo'.isupper()) #False
print('MOOOO'.isupper()) #True'''


#El metodo "join"

#Este metodo, pide como argumento una lista con varios elementos de solo tipo cadena. Luego, juntara todos los elementos en una cadena nueva. Ejemplo

'''print(",".join(["omicron", "pi", "rho"]))'''

#Nota: La coma ingresada al principio es el separador entre cada cadena puesta en la lista al momento de imprimirse. Osea su resultado es el siguiente:
"omicron,pi,rho"
#(Esta coma puede ser cambiada por un espacio en blanco o por cualquier otro caracter)


#El metodo "lower"

#Este metodo, imprime una copia de una cadena con todos sus caracteres en minuscula. Ejemplo:

'''print("SiGmA=60".lower())'''


#El metodo "lstrip"

#Este metodo, imprime una copia de una cadena eliminando los espacios en blanco iniciales. Ejemplo:

'''print("[" + " tau ".lstrip() + "]")''' 

#Tambien se puede poner como argumento una parte de texto en especifico y lo eliminará. Ejemplo:

'''print("www.cisco.com".lstrip("w.")) #Resultado: "cisco.com"'''

#Nota: Recordar que esto solo aplica con lo que esta al inicio de la cadena, por lo cual el siguiente ejemplo no aplica para este metodo:

'''print("pythoninstitute.org".lstrip(".org")) #Imprimira la misma cadena'''


#El metodo "replace"

#Este metodo, reemplaza un texto puesto en una cadena por otro especificado en el metodo. Ejemplo:

'''print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))'''

#El primer argumento ingresado es el texto que se quiere reemplazar y el segundo ingresado es el texto por el cual se va a reemplazar

#Con un tercer argumento, se puede limitar la cantidad de veces que se puede reemplazar este texto. Ejemplo:

'''print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))'''


#El metodo "rfind"

#Este metodo, hace lo mismo que su contraparte "find" pero busca los elementos en reversa ; osea desde el final. Ejemplo:

'''print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))'''


#El metodo "rstrip"

#Este metodo, hace lo mismo que su contraparte "lstrip" pero elimina los espacios o el elemento especificado del final. Ejemplo:

'''print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))'''


#El metodo "split"

#Este metodo, divide una cadena y esos elementos divididos los imprime en forma de lista.
#La forma en que el metodo reconoce las subcadenas, es por medio de los espacios en blanco. Ejemplo:

'''print("phi       chi\npsi".split())'''


#El metodo "startswitch"

#Este metodo, hace lo contrario a "endswitch": Identificar si una cadena empieza con los caracteres especificados. Ejemplo:

'''print("omega".startswith("meg")) #False
print("omega".startswith("om")) #True'''


#El metodo "strip"

#Este metodo, combina "rstrip" y "lstrip" e imprime una cadena eliminando los espacios en blanco del principio y el final de una cadena ingresada. Ejemplo:

'''print("[" + "   aleph   ".strip() + "]")'''


#El metodo "swapcase"

#Este metodo, cambia las mayusculas por minusculas y viceversa. Ejemplo:

'''print("Yo sé que no sé nada.".swapcase())'''


#El metodo "title"

#Este metodo, pone todas las iniciales de las palabras de una cadena en mayuscula. Ejemplo:

'''print("Yo sé que no sé nada. Part 1.".title())'''


#El metodo "upper"

#Este metodo, convierte todas las letras de una cadena en mayuscula. Ejemplo:

'''print("Yo sé que no sé nada. Part 2.".upper())'''

