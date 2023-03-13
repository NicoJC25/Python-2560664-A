from os import strerror

try:
    cont_letra= cont_linea=0
    stream = open("G:\Repositorio-Python\Trimestre 3-Python Intermedio\Miscelaneas\Miscelanea 6 - Dos programas archivos\Archivo.txt", 'rt', encoding='utf-8') #UTF-8 para especificar el idioma
    '''letra=stream.read()   #Se puede poner tanto con o sin argumentos'''
    '''linea=stream.readline()'''
    lineas=stream.readlines(5)   #Se especifica la cantidad por si el archivo es grande
    while len(lineas) != 0:
        for linea in lineas:
            cont_linea += 1
            for letra in linea:
                print(letra, end='')
                cont_letra+= 1
        lineas = stream.readlines(5)
    stream.close()
    print("\nCaracteres en el archivo:", cont_letra)
    print("Líneas en el archivo:", cont_linea)
except IOError as e:
    print("Se produjo un error :/:", strerror(e.errno))



'''from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    binary_file = open('file.bin', 'wb')
    binary_file.write(data)
    binary_file.close()
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))

from os import strerror

data = bytearray(10)

try:
    binary_file = open('file.bin', 'rb')
    binary_file.readinto(data)
    binary_file.close()

    for b in data:
        print(hex(b), end=' ')
except IOError as e:
print("Se produjo un error de E/S:", strerror(e.errno))'''

from os import strerror

nombre_archivo_fuente = input("Ingresa el texto del archivo fuente: ")
try:
    archivo_fuente = open('G:\Repositorio-Python\Trimestre 3-Python Intermedio\Miscelaneas\Miscelanea 6 - Dos programas archivos/Archivo_fuente', 'a')
    texto_archivo_fuente= input('Ingresa un texto para el archivo fuente: ')
except IOError as e:
    print("No se puede crear archivo fuente: ", strerror(e.errno))
    exit(e.errno)	

nombre_archivo_destino = input("Ingresa el nombre del archivo destino: ")
try:
    archivo_destino = open('G:\Repositorio-Python\Trimestre 3-Python Intermedio\Miscelaneas\Miscelanea 6 - Dos programas archivos\Archivo_destino', 'wb')
except Exception as e:
    print("No se puede crear el archivo de destino:", strerror(e.errno))
    archivo_fuente.close()
    exit(e.errno)	

bufer = bytearray(65536)
total  = 0
try:
    archivo_fuente.write(texto_archivo_fuente)
    lectura = archivo_fuente.readinto(bufer)
    while lectura > 0:
        total += written
        written = archivo_destino.write(total)
except IOError as e:
    print("No se puede crear el archivo de destino: ", strerror(e.errno))
    exit(e.errno)	
    
print('Cantidad de bytes pasada con exito')
archivo_fuente.close()
archivo_destino.close()
