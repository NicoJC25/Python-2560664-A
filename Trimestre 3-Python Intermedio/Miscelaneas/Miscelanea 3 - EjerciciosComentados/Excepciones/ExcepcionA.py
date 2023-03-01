try:                                                    #Intenta el siguiente bloque de codigo
    #print(1/1))                                        #El print con error de sintaxis se pone en comentario ya que de esa forma...
    raise SyntaxError                                   #... el raise pueda lanzar el error de forma manuals
except SyntaxError as e:                                #Y poder aplicacr la excepcion de ese mismo error. Syntax es importado como e ya que de esta forma...
    print(e)                                            #... al imprimir "e", imprime el mensaje pre establecido del error como tal
    print('Cierra el parentesis')                       #Y un prin adicional de cual fue la accion en especifico que falló
    
try:                                                    #Intenta el siguiente bloque de codigo
    #raise ZeroDivisionError
    print(1/0)                                          #Imprime uno sobre cero
#except (ZeroDivisionError) as e:
except ZeroDivisionError as zde:                        #ZeroDivisionError va a ser ejecutado como zde
    print(zde)                                          #Imprimimos zde, el mensaje pre establecido de ZeroDivision
    #print('prueba error')                              #Mensaje adicional