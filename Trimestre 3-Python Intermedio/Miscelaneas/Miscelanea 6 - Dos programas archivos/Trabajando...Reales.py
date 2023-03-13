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
