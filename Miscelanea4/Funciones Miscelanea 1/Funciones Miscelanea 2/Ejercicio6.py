n=0 #Variable definida desde antes para que la funcion haga su labor

def numeros_puestos(n): #Definimos la funcion "numeros_puestos"
    contador=0 #Contador
    while(n>=0): #Mientras n sea igual o mayor a 0
        n=int(input("introduzca numeros.... ")) #Va a pedir numeros
        if n>=0: #Si n es igual o mayor a 0
            contador+=1 #El contador ira aumentando
        else:
            print("Esta fue la cantidad de numeros positivos registrados",contador) #Cuando se introduzca el negativo, se acaba


numeros_puestos(n) #Invocamos funcion