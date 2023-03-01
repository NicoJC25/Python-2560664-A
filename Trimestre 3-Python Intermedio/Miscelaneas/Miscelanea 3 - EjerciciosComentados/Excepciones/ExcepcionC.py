def try_syntax(numerator, denominator):                             #Definimos la funcion donde hay 2 parametros
    try:                                                            #Intenta el siguiente bloque de codigo:
        print(f'In the try block: {numerator}/{denominator}')       #Imprima el mensaje junto con la operacion a realizar
        #quiero ver el resultado de la operacion en el print
        result = numerator / denominator                            #Se va a crear una variable donde se hace la operacion
    except ZeroDivisionError as zde:                                #Si ocurre un error ZeroDivision, se va a importar como zde
        print(zde)                                                  #Y se imprime este mismo
    else:                                                           #Si no ocurre error
        print('The result is:', result)                             #Imprime el mensaje de cual es el resultado de la operacion
        return result                                               #Retorna el resultado
    finally:                                                        #Esta parte del codigo lo que hace es que, al finalizar el proceso de try, siempre se imprima el mensaje dentro
        print('Exiting')                                            #Imprime "Exiting"
        #return "Fallo por zero"                                    #Prueba del finally
#print(try_syntax(12, 4))                                           #Imprime la funcion haciendola funcionar de forma correcta
print(try_syntax(11, 'a'))                                          #Invoca la funcion