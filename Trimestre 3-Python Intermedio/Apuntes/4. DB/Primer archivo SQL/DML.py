#Sentencias DML:

#INSERT: Se usa para insertar datos en la tabla
#UPDATE: Se usa para cambiar o actualizar datos ya existentes
#DELETE: Se usa para eliminar datos ya existentes en la tabla
#SELECT: Se usa para seleccionar datos y realizar algunas acciones con los mismos

#Ejemplo INSERT:

#INSERT INTO <Nombre de la tabla> (<Nombres de las columnas a editar>) VALUES (<Valores a ingresar>)

#INSERT INTO Aprendizb (Nombres, Apellidos, Num_Identificacion, Tipo_Identificacion) 
# VALUES ('Andres Felipe', 'Franco Tellez', 23424232, 'Cedula de Ciudadania')


#Ejemplo UPDATE:
#UPDATE <Nombre de la tabla>
#SET <Columna a cambiar el valor> = <Nuevo valor>
#WHERE <Condicion>

#UPDATE Aprendiz
#SET Num_Identificacion = 1000743287
#WHERE Nombres= "Andres Felipe" AND Apellidos="Franco Tellez"


#Ejemplo DELETE:
#DELETE
#FROM <Nombre de la tabla>
#WHERE <Condicion>

#DELETE
#FROM Aprendiz
#Where Nombres= "Andres Felipe" AND Apellidos= "Franco Tellez" AND Num_Identificacion=1000743287 AND Tipo_Identificacion="Cedula de Ciudadania"



#Consulta de datos - SELECT
#Con SELECT se visualizan los datos de la tabla. Ejemplo

#SELECT <Nombre columna> o <Varias columnas>
#FROM <Nombre de la tabla>

#SELECT Nombres
#FROM Aprendiz


#Esta instruccion puede ir acompañada de las siguientes clausulas:
#WHERE <condicion>
#GROUP BY <Nombre columna>
#HAVING <condicion>
#ORDER BY <Nombre columna> <Modo de ordenamiento>

#Tambien se puede usar una sentencia para seleccionar todos los datos de la tabla, el asterisco "*". Ejemplo:

#SELECT * FROM Aprendiz;

