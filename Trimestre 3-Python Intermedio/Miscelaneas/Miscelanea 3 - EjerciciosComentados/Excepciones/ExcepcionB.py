values = (1, 'a')                                   #Establecemos la variable values con dos valores: Uno y cero
#x,y=10,12
#print(divmod(10,3))
try:                                                #Intenta el siguiente bloque de codigo:
    q, r = divmod(*values)                          #q y r van a tener los valores divididos de "values". Gracias a el asterisco puesto, de esta forma se dividen todos los valores de la variable...
    #print('valor de q=',q)
    print(f'q={q}')                                 #Y se agrega uno tanto en f
    print(f'r={r}')                                 #Como en r 

#Nota: La sintaxis de estas impresiones es diferente a las demas ya que al poner la "f" al principio, se establece...
#... que se puede intercalar entre variable y texto en vez de la clasica sintaxis con las comas de por medio.
#La unica condicion es que al momento de invocar una variable, se ponga entre llaves.

except (ZeroDivisionError, TypeError) as e:         #Ambos excepts van a ser invocados con la variable "e"
    print(type(e), e)                               #Dependiendo del error, imprima primero el tipo de error ejecutado y luego el mensaje por defecto de esa excepcion
