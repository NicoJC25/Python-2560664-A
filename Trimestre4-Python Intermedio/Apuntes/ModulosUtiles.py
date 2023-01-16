#Luego de importar un modulo de la forma tradicional "import module", existe una funcion llamada "dir". 
#De esta forma, se puede saber los nombres del modulo importado:

'''import math
print(dir(math))'''

#Tambien se pueden usar ciclos con esta funcion:

import math

for name in dir(math):
    print(name, end="\t")

#Ahora, vamos a ver varios modulos que pueden resultar bastantes utiles en muchos programas.
