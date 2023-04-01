#En estos operadores, vemos combinaciones de otros predicados con los operadores logicos AND, OR y NOT

#Ejemplo:

#Los aprendices de Bogota que no tengan registrada alguna direccion
#SELECT * FROM Aprendiz
#WHERE Ciudad="Bogota" AND Direccion IS NULL


#Luego tenemos la Clausula ORDER BY que se utiliza para organizar las filas de manera ascendente o descendente. Por defecto, este es ascendente

#Sintaxis:

#SELECT <Nombre de la columna> o <Lista de columnas>
#FROM <Nombre de la tabla>
#WHERE <Condicion>
#ORDER BY <Nombre columna> o <Numero de columnas>

#Ejemplo:

#Ordenar la lista de nombres de aprendices alfabeticamente
#SELECT Nombres, Apellidos
#FROM Aprendiz
#ORDER by Nombres;

#Ordernas la misma lista pero tomando en cuenta los apellidos
#SELECT Nombres, Apellidos
#FROM Aprendiz
#ORDER by Apellidos;

#Ordenar los datos de los aprendices por medio del documento de identidad
#SELECT *
#FROM Aprendiz
#ORDER by Num_Identificacion asc;