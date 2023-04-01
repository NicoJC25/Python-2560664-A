#Sentencias del DDL

#CREATE: Como dice su nombre, se usa para crear algun tipo de dato. Ejemplo:

#CREATE DATABASE Persona          Se usa para crear la base de datos

#CREATE TABLE Aprendiz              Se usa para crear las tablas en la base de datos


#USE: Se implementa para usar la base de datos y asi, editar los datos dentro de la misma. Ejemplo:

#use Persona


#Dentro de la tabla, se definen ya las columnas con sus datos correspondientes. Estas son las caracteristicas:

#NOTNULL: Se indica cuando si o si debe de ir un valor en esa tabka
#PRIMARY KEY: Es un dato unico y que ademas es el identificador de esa tabla
#UNIQUE: Es para identificar un dato que no se repite
#DEFAULT: Si no se rellena el valor de esa columna, un valor por predeterminado y especificado anteriormente sera puesto en reemplazo
#CHECK: Se especifica una condicion para aceptar el dato
#FOREIGN KEY: Es un dato que hace enlace con otras tablas ya que esta tanto en esta como en las otras para generar una relacion

#Ejemplo general de como se puede construir la tabla:

# Create table Aprendiz{
# Nombres Char(20) not null,   
# Apellidos Varchar(20) not null,
# Num_Identificacion Int(15) primary key not null
# }



#Modificar tablas

#Para esto, tenemos tres sentencias muy utiles:
#ADD (columna o restriccion): Para agregar columnas o restricciones
#DROP (columna o restriccion): Para eliminar columnas o restricciones
#ALTER/MODIFY: Para modificar columnas existentes

#Ejemplo ADD:

#Alter Table Aprendiz
#Add Column Tipo_Documento varchar(20)

#Alter table Aprendiz
#Add Constraint UNIQUE ( MedRegistro)


#Ejemplo DROP:
#DROP Aprendiz