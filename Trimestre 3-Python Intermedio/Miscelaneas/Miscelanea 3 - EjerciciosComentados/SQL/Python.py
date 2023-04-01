import sqlite3                                                              #Importa un paquete que trae las funcions de sqlite
#con=sqlite3.connect('C:\\padilla\\sqlite-tools\\db\\pythondb.db')          #Una ruta absoluta para conectar el archivo de Python con el de sqlite
con=sqlite3.connect('pythonsqlite/pythondb.db')                             #Otro ejemplo de ruta pero en este caso con relativa, que la va a llevar la variable "con"
print(type(con))                                                            #Aqui imprime el tipo de dato que es "con"
micursor=con.cursor()                                                       #La variable micursor va a ser por asi decirlo la que permita manipular la base de datos gracias a la funcion "cursor"
print(type(micursor))                                                       #Imprime el tipo de dato que es micursor
new_sql="SELECT * from Persona;"                                            #La variable new_sql va a almacenar una sentencia SQL
micursor.execute(new_sql)                                                   #Y la variable micursor usara la funcion execute haciendo que envie la instruccion a la base de datos y se impriman todos los datos de la tabla "Persona"
lista=micursor.fetchall()                                                   #La variable lista va a almacenar todos los datos de la busqueda gracias a la funcion "fetchall"
for fila in lista:                                                          #Abre una iteracion
    print(fila[0])                                                          #Imprime fila por fila cada dato adquirido
    print(fila[1])
    print(fila[2])
    print(fila[3])
    print('*'*50)                                                           #Se usa como separador de cada dato

