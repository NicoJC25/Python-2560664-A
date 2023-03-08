from Sistema_Biblio import *
from os import system as Interfaz

lec=Lector('Roberto','Calle 65B',32422434)
est=Estudiante('Andres','Calle 57C',3005455,1)
doc=Docente('Pablo','Calle 80A',34535322,1)
lib=Libro('Pepe el grillo','Infantil','Pepe','Atenea',0)
rev=Revista('51 minutos','Moda','Pepe','Quinta',0)
Biblio=Bibliotecario('Pedro',1)

try:
    while True:
        Interfaz('cls')
        print('Bienvenido al menu\n Presione 1 para ver todos los datos de un estudiante o un profesor\n Presione 2 para ver un dato unico de un estudiante o un profesor\n Presione 3 para modificar los datos de un estudiante o un profesor\n Presione 4 para modificar un dato unico de un estudiante o un profesor\n Presione 5 para reservar un libro o revista\n Presione 6 para ver el pedido\n Presione 7 para salir del programa\n')
        pedir=int(input(' '))
        match pedir:
            case 1:
                pedir_1=int(input('Elija 1 si quiere ver los datos del estudiante, de lo contrario elija 2: '))
                if pedir_1==1:
                    est.getAll()
                elif pedir_1==2:
                    doc.getAll()
                else:
                    print('El numero no es valido')
            case 2:
                pedir_2=int(input('Elija 1 si quiere ver el dato del estudiante o 2 si es del docente: '))
                if pedir_2==1:
                    pedir_3=int(input('Elija 1 si quiere ver el nombre, 2 si quiere ver la direccion, 3 si quiere ver el telefono o 4 para ver su identificacion: '))
                    match pedir_3:
                        case 1:
                            print(est.getNombre())
                        case 2:
                            print(est.getDireccion())
                        case 3:
                            print(est.getTelefono())
                        case 4:
                            print(est.getCodigo_E())
                elif pedir_2==2:
                    pedir_4=int(input('Elija 1 si quiere ver el nombre, 2 si quiere ver la direccion, 3 si quiere ver el telefono o 4 para ver su identificacion: '))
                    match pedir_4:
                        case 1:
                            print(doc.getNombre())
                        case 2:
                            print(doc.getDireccion())
                        case 3:
                            print(doc.getTelefono())
                        case 4:
                            print(doc.getCodigoD())
                else:
                    print('El numero no es valido')
            case 3:
                pedir_5=int(input('Elija 1 si quiere modificar los datos del estudiante o 2 si quiere modificar los datos del docente: '))
                if pedir_5==1:
                    nombre_estudiante=input('Elija el nombre del estudiante nuevo: ')
                    direccion_estudiante=input('Elija la direccion del estudiante nuevo: ')
                    telefono_estudiante=int(input('Elija el telefono del estudiante nuevo: '))
                    est.setNombre(nombre_estudiante)
                    est.setDireccion(direccion_estudiante)
                    est.setTelefono(telefono_estudiante)
                    est.setCodigo_E()
                    print('¡Datos cambiados!')
                elif pedir_5==2:
                    nombre_docente=input('Elija el nombre del docente nuevo: ')
                    direccion_docente=input('Elija la direccion del docente nuevo: ')
                    telefono_estudiante=int(input('Elija el telefono del docente nuevo: '))
                    doc.setNombre(nombre_docente)
                    doc.setDireccion(direccion_docente)
                    doc.setTelefono(telefono_estudiante)
                    doc.setCodigo_D()
                    print('¡Datos cambiados!')
                else:
                    print('El numero no es valido')
                
            case 4:
                pedir_6=int(input('Elija 1 si quiere modificar un dato unico del estudiante o 2 si quiere modificar los datos del docente: '))
                if pedir_6==1:
                    pedir_7=int(input('Elija 1 si quiere cambiar el nombre, 2 si quiere cambiar la direccion, 3 si quiere cambiar el telefono o 4 si quiere actualizar el codigo: '))
                    match pedir_7:
                        case 1:
                            nombre_estudiante=input('Elija el nuevo nombre: ')
                            est.setNombre(nombre_estudiante)
                            print('¡Dato cambiado!')
                        case 2:
                            direccion_estudiante=input('Elija la nueva direccion: ')
                            est.setDireccion(direccion_estudiante)
                            print('¡Dato cambiado!')
                        case 3:
                            telefono_estudiante=int(input('Elija el nuevo telefono: '))
                            est.setTelefono(telefono_estudiante)
                            print('¡Dato cambiado!')
                        case 4:
                            est.setCodigo_E()
                            print('¡Dato cambiado!')
                elif pedir_6==2:
                    pedir_8=int(input('Elija 1 si quiere cambiar el nombre, 2 si quiere cambiar la direccion, 3 si quiere cambiar el telefono o 4 si quiere actualizar el codigo: '))
                    match pedir_8:
                        case 1:
                            nombre_docente=input('Elija el nuevo nombre: ')
                            doc.setNombre(nombre_docente)
                            print('¡Dato cambiado!')
                        case 2:
                            direccion_docente=input('Elija la nueva direccion: ')
                            doc.setDireccion(direccion_docente)
                            print('¡Dato cambiado!')
                        case 3:
                            telefono_estudiante=int(input('Elija el telefono del docente nuevo: '))
                            doc.setTelefono(telefono_estudiante)
                            print('¡Dato cambiado!')
                        case 4:
                            doc.setCodigo_D()
                            print('¡Dato cambiado!')
                else:
                    print('El numero no es valido')
            case 5:
                pedir_9=int(input('Elija 1 si quiere reservar un libro o 2 si quiere reservar una revista: '))
                if pedir_9==1:
                    titulo_libro=input('Ingrese el titulo del libro: ')
                    tipo_libro=input('Ingrese el tipo de libro: ')
                    autor=input('Ingrese el autor del libro: ')
                    editorial=input('Ingrese la editorial a la que pertenece: ')
                    lib.setTitulo_M(titulo_libro)
                    lib.setTipo_M(tipo_libro)
                    lib.setAutor(autor)
                    lib.setEditorial(editorial)
                    lib.setCodigo_L()
                    pedir_10=int(input('Elija 1 si quiere que la reserva se agregue al estudiante o 2 si quiere que se agregue al docente: '))
                    if pedir_10==1:
                        est.agregarPedido(est.getCodigo_E(),lib.getTitulo_M(),lib.getCodigo_L())
                        print('¡Datos agregados!')
                    elif pedir_10==2:
                        doc.agregarPedido(doc.getCodigo_D(),lib.getTitulo_M(),lib.getCodigo_L())
                        print('¡Datos agregados!')
                    else:
                        print('Elija un numero correcto')
                elif pedir_9==2:
                    titulo_revista=input('Ingrese el titulo de la revista: ')
                    tipo_revista=input('Ingrese el tipo de la revista: ')
                    autor=input('Ingrese el autor de la revista: ')
                    edicion=input('Ingrese la edicion de la revista: ')
                    rev.setTitulo_M(titulo_revista)
                    rev.setTipo_M(tipo_revista)
                    rev.setAutor(autor)
                    rev.setEdicion(edicion)
                    rev.setCodigo_R()
                    pedir_11=int(input('Elija 1 si quiere que la reserva se agregue al estudiante o 2 si quiere que se agregue al docente: '))
                    if pedir_11==1:
                        est.agregarPedido(est.getCodigo_E(),rev.getTitulo_M(),rev.getCodigo_R())
                        print('¡Datos agregados!')
                    elif pedir_11==2:
                        doc.agregarPedido(doc.getCodigo_D(),rev.getTitulo_M(),rev.getCodigo_R())
                        print('¡Datos agregados!')
                    else:
                        print('Elija un numero correcto')
            case 6:
                pedir_12=int(input('Ingrese 1 si quiere ver el pedido del estudiante o 2 si quiere ver el pedido del docente: '))
                if pedir_12==1:
                    est.getPedido()
                elif pedir_12==2:
                    doc.getPedido()
                else:
                    print('El numero no es valido')
            case 7:
                break
            case _:
                print('El numero no es valido')
        Interfaz('pause')
        print('Escoja un numero valido')
except (TypeError, ValueError ) as e:
    print(type(e), e)

            
                












                    
