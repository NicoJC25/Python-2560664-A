#Hay un punto muy importante y es la manipulacion de datos por medio de las consultas
#Esta manipulacion tiene diferentes niveles de complejidad y varios tipos de consulta enlazados con estos

#Para empezar vamos a ver la forma de obtener varios datos que provengan de diferentes tablas, especialmente los datos con llaves foraneas.
#Aqui un tema muy importante a resaltar son los Alias, ya que se usan para nombrar tablas en general que mejora bastante...
#... la legibilidad en las secuencias de comandos, la escritura de combinaciones complejas es mas facil y simplifica el mantenimiento de estas consultas.

#Ejemplo sintaxis:

#SELECT *
#FROM <Nombre tabla1> AS <Alias tabla1> INNER JOIN
#<Nombre tabla2> AS <Alias Tabla2>
#ON <Alias tabla1>.<Campo llave foranea>
#<Alias tabla2>.<Campo llave foranea>

#Ejemplo real:

#SELECT PacNombres, PacApellidos, PacSexo, MedNombres,
#MedApellidos
#FROM Tblpacientes INNER JOIN TblMedicos
#ON TblMedicos.MedIdentificacion = Tblpacientes.
#PacMedIdentifica

#Ejemplo usando el Alias:
#SELECT PacNombres, PacApellidos, PacSexo, MedNombres,
#MedApellidos
#FROM Tblpacientes as TP INNER JOIN TblMedicos as TM
#ON TM.MedIdentificacion = TP. PacMedIdentifica


