
#Combinaciones

#Es una forma de obtener los datos de las tablas a partir de diferentes tipos de combinaciones, que se cumplen por medio de...
#... una condicion entre dos de sus columnas. Se usa FROM para especificar estos datos y se identifica con la palabra JOIN


#Combinacion interna - INNER JOIN
#Estas combinaciones internas se hacen mediante la comparacion de los valores de las columnas que son comunes en ambas tablas.
#Solo se retornan las filas que cumplan las condiciones de la combinacion

#La union se hace por medio de un metodo de interseccion donde se enlazan por medio de las llaves.

#Sintaxis:

#SELECT *
#FROM <Nombre tabla1> AS <Alias Tabla1> INNER JOIN <Nombre tabla2> AS <Alias Tabla2>
#ON <AliasTabla1>.<Campo llaveprimaria> = <AliasTabla2>.<Campo llaveforanea>


#Combinaciones externas - OUTER JOIN

#Para este tipo de combinaciones, una de las tablas es por asi decirlo dominante y las demas subordinadas
#Todos los registros de la tabla dominante seran agregados a la tabla final mientras que las demas solo las interescciones entre las tablas

#En este caso, al ser en formato "OUTER" o los datos externos de la tabla, toma estos datos externos comparando una llave foranea...
#... que si o si, debe estar. Entonces todos los datos de la tabla dominante seran puestos en la tabla nueva y los datos enlazados...
#... de la otra tabla 

#Sintaxis:

#SELECT *
#FROM <Nombre tabla1> AS <alias1> RIGHT/LEFT JOIN
#<Nombre tabla2> AS <alias2>
#ON <Alias tabla1>.<Campo llaveprimaria> = <aliasTabla2>.<Campo llaveforanea>


#Autocombinaciones - SELF JOIN

#Cuando se necesita combinar una tabla consigo misma, se utiliza este metodo "SELF JOIN".
#Se suele usar por ejemplo cuando se desea comparar valores de una columna con otra de la misma tabla.
#Para utilizarlo se implementa el alias a la tabla como si se tratara de 2 tablas diferentes y usar la estructura join que se considere necesaria

#Sintaxis:
#SELECT *
#FROM <Nombre tabla1> AS <alias1> INNER JOIN <Nombre tabla2> AS <alias2>
#ON <alias1>.<campo> = <alias2>.<campo>

#En el caso de las autocombinaciones, cada fila y parejas que coincidan consigo mismas van a repetirse y por lo tanto, duplicarse...
#... asi que se debe usar una clausula WHERE para eliminar dichos duplicados.


#Combinar mas de dos tablas

#A veces, se realizan combinaciones con mas de dos tablas, por lo cual hay que adaptar la sintaxis para esto mismo
