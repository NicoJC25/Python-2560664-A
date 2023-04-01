#1. Saber en que sistema operativo tiene el computador en el que esta trabajando

from os import *
from platform import *

print(name)
print(uname())

#2. Crear un directorio

"""mkdir("Directorio1")
print(listdir())"""

#3. Crear un directorio recursivo en el directorio creado anteriormente

#makedirs("Directorio2\holaxd")
chdir("Directorio2")
print(listdir())

#4. Crear otro directorio que su nombre sea "vocales" y dentro tenga directorios con todas las vocales, cuando la liste aparezcan las vocales en orden

mkdir("Vocales")
chdir("Vocales")
print(listdir())
