'''Archivo que recrea el juego de ahorcado, primero que un usuario ponga una palabra y luego que otro la adivine'''

palabra=[] #Palabra a poner
palabra_encontrada=[] #Donde evaluar la palabra

def llenar_palabra(palabra): #Definimos funcion para poner la palabra
    while True: #Bucle infinito
        llenar=input('Ingrese la palabra a encontrar(letra por letra y presione enter sin nada escrito para dejar de agregar letras): ') #Poner letra por letra de la palabra
        if len(llenar)>1: #Si intenta poner mas de 1 letra
            print('Ingrese solo una letra') #Que imprima esto
        else:
            palabra.append(llenar) #Si no, append que vaya incluyendo cada letra
        if llenar=='': #Si pone un enter sin alguna cosa mas
            palabra.pop(-1) #Va a eliminar ese enter de la lista
            break #Break
    return palabra #Y retorna


def buscar_palabra(palabra): #Definimos funcion para buscar la palabra
    oportunidades=5 #Variable para la cantidad de intentos
    aux=bool #Aux para mas adelante
    for i in range(len(palabra)): #En el rango de la palabra que estamos buscando
        palabra_encontrada.append('-') #La segunda lista va a agregar la misma cantidad de letras en guiones
    while True: #Bucle infinito
        aux=False #Aux sera falso
        buscar=input('Inserte una letra para buscar: ') #Para buscar letra por letra
        for i in range(len(palabra)): #Otro for en la longitud de la palabra que estamos buscando
            if buscar == palabra[i]: #Si la letra insertada esta en la palabra
                aux=True #Aux sera verdadero
                if buscar in palabra_encontrada: #Ahora, si antes ya se habia agregado esta letra
                    print('La letra ya fue encontrada') #Saldra este mensaje
                else:
                    palabra_encontrada[i]=palabra[i] #Si no, se reemplazara el guion donde va posicionada esa letra
                    print('Felicidades, encontro una de las letras, asi es como se ve la palabra con la letra encontrada:',palabra_encontrada) #Print con como quedo la palabra luego de haber encontrado esa letra
        if aux==False: #Si auxiliar permanese falso
            oportunidades-=1 #Se restara un intento
            print('Lo siento, no está esta letra en la palabra, tiene',oportunidades,'oportunidades mas') #Saldra este mensaje
        if oportunidades<=0: #Si el jugador se queda sin oportunidades
            print('¡Perdiste!') #Imprime mensaje
            break #Break
        if palabra_encontrada==palabra: #Si encontro toda la palabra
            print('Felicidades, gano el juego, la palabra completa es:',palabra) #Mensaje de felicitaciones :D
            break #Y break
    return palabra_encontrada #Retorna la palabra encontrada


llenar_palabra(palabra) #Invocamos primera funcion
buscar_palabra(palabra) #Invocamos segunda funcion