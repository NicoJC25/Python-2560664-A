def edad():                                                     #Definimos funcion sin parametros
    try:                                                        #Intenta el siguiente bloque de codigo:
        tuedad=int(input("introduce tu edad"))                  #Input donde se ingresa una edad
        print(f'tu edad es  {tuedad}')                          #Se imprime la edad si todo salio bien
        #print('Tu edad es ',tuedad)
    except ValueError as e:                                     #Si ocurre un error tipo "ValueError", se va a agregar su informacion de error en la variable e
        print(e)                                                #Se imprime e
        print("La edad debe ser un valor numerico...")          #Otro mensaje acerca de que es lo que se hizo mal
        edad()                                                  #Y se reinicia la funcion haciendo qe la unica forma de que se detenga el bucle, sea poniendo el tipo de valor correcto
    
edad()                                                          #Invocamos la funcion