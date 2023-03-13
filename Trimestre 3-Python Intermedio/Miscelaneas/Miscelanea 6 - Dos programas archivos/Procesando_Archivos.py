import errno
from os import strerror 

#Programa 1

try:
    stream=open("G:/Repositorio-Python\Trimestre 3-Python Intermedio/Miscelaneas/Miscelanea 6 - Dos programas archivos\Archivo.txt", "rt")   #Ruta absoluta. Barras diagonales mezcladas
    print('Hola')   #Probar si funciona el programa
    stream.close   #Cerrar stream
except Exception as exc:   #Except con sterror
    print('Error al abrir el archivo :/',strerror(exc.errno))   #Forma de escribirlo, errno
    

#Programa 2

try:
    stream=open("G:\Repositorio-Python\Trimestre 3-Python Intermedio\Miscelaneas\Miscelanea 6 - Dos programas archivos\Archivo,txt", "rt")   #Open con error a proposito
    print('Hola')   #Texto
    stream.close   #Close
except Exception as exc:   #Excepciones
    if exc.errno == errno.ENOENT:   #Metodo de excepciones una por una. No existe el archivo
        print('El archivo no existe aaa')
    elif exc.errno == errno.ENOSPC: #No hay espacio de almacenamiento
        print('No queda espacio libre :c')
    elif exc.errno == errno.EMFILE: #Muchos archivos abiertos
        print('Hay muchos archivos abiertos. Cierralos')
    elif exc.errno == errno.EFBIG:  #Archivo muy grande
        print('El archivo es muy grande y no puede ser ejecutado')
    else:     #Fusion del otro metodo except
        print('Hubo un error al abrir el archivo D:',strerror(exc.errno))