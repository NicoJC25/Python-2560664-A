#En todo lenguaje de programacion vemos que hay errores, es normal despues de todo que los programadores se les pase algunas cosas
#Por suerte o al menos en Python, se ofrece una solucion que puede resultar muy util para estos problemas:
#Tenemos un ejercicio donde por medio de un input pedimos un numero para transformarlo en su reciproco
'''num=int(input('Ingrese el numero: '))
print('El reciproco del numero',num,'es:',1/num)'''

#Todo bien hasta ahi, pero que pasa si ¿insertamos un valor que no es un numero?. Esto va a sacar un error que se puede probar -->
#Aqui mismo si se quiere comprobar, pero a lo que voy es que es normal que en algunos programas las personas pongan cosas -->
#Que se supone el programa no puede aceptar, pero no podemos dejar que el cliente vea el mensaje de error y ya, hay que encontrar una forma de arreglarlo.

#Aqui entran 2 palabras reservadas muy utiles llamadas "try" y "except". Funcionan de la siguiente manera:
'''try: #Primero ponemos la plabra try con dos puntos, esto lo que va a hacer es evaluar lo que se pone dentro
    num=input('Ingrese el numero: ') #Numero pedido
    print('El reciproco del numero',num,'es:',1/num) #Mensaje si el proceso es exitoso
except: #Pero si por alguna razon, sale un error en el momento de la ejecucion, except sera el que invoque lo que se mostrara si ocurre este error
    print('Lo siento, el valor',num,'no concuerda con lo solicitado') #Imprimira un mensaje que indica que el valor no concuerda'''

#Como se puede ver si se ejecuta el codigo, si se inserta una letra o palabra, utilizara el mensaje del except para indicar que hubo un error
#De igual forma, si una parte del codigo tuvo error, no hara un break instantaneo sino que si mas adelante faltan funciones por invocar -->
#Las ejecutara sin problema alguno

#Ahora bien, se pueden especificar tipos de errores en los except para que suelte un mensaje en especifico para ese error. Ejemplo:
'''try:
    num=input('Ingrese el numero: ')
    print('El reciproco del numero',num,'es:',1/num)
except ValueError: #En este except vemos que se especifica el error, osea si el valor insertado no puede modificarse con esta funcion
    print('Lo siento, el valor',num,'no concuerda con lo solicitado') #Mensaje especifico
except ZeroDivisionError: #En este except vemos otro error que ocurre cuando se inten'ta dividir un numero entre 0
    print('No se puede dividir un numero entre 0') #Mensaje especifico'''

#Como se puede ver, tambien se pueden poner varios except para un try, ya que a veces es necesario poner un mensaje en especifico -->
#Para ciertos errores
#Por ultimo, al igual que en el primer ejercicio de prueba del try y except, se puede incluir un except sin ningun error en especifico:
'''try:
    num=input('Ingrese el numero: ')
    print('El reciproco del numero',num,'es:',1/num)
except ValueError: 
    print('Lo siento, el valor',num,'no concuerda con lo solicitado')
except ZeroDivisionError: 
    print('No se puede dividir un numero entre 0')
except:
    print('Lo siento, algo extraño ocurrió, verifica que los datos esten correctos') #Un mensaje si el error no concuerda con los demas'''

#Este es llamado el "except por defecto", el cual se usa siempre al final de todos los except si es que se ponen mas

#Algunos de los errores a los que se les puede hacer una excepcion util son los siguientes:
#ZeroDivisionError: Cuando se intenta dividir un numero entre 0
#ValueError: Cuando el dato insertado no tiene un uso apropiado en el contexto en el que esta
#TypeError: Cuando se intenta aplicar un dato cuyo tipo no se puede aceptar en ese contexto
#AttributeError: Cuando se esta implementando un metodo que no funciona o no existe con el elemento en cuestion
#SyntaxError: Cuando por alguna razon, se viola la gramatica de Python

#Los codigos necesitan ser probados para evaluar si estan funcionando bien o no, pero en este caso siempre es preferible que lo haga alguien externo
#El hecho es que al evaluar uno mismo su codigo, normalmente solo se evalua algunas cosas que el mismo programador sabe
#Mientras que alguien externo puede que le ocurra algo mas alla y pueda encontrar un error
#Algo asi como los escritores necesitan un editor, el programador necesita un tester

#Siempre es necesario evaluar el codigo en el mas minimo detalle, un ejemplo el siguiente codigo:
'''temperature = float(input('Ingresa la temperatura actual: '))
if temperature > 0:
    print("Por encima de cero")
elif temperature < 0:
    prin("Por debajo de cero") #Si se pudo notar, aqui hay un error con un print
else:
    print("Cero")'''

#Pero, ¿Que pasa si se ejecuta este codigo y se pone por ejemplo 0? Bueno, como puedes ver se ejecuta a la perfeccion
#El programa pasa por alto el error, probablemente por el hecho de que como no se esta utilizando ese elif en especifico -->
#No saca el error necesario

#Cuando uno termina de mirar su propio codigo, es mejor pasarlo a los probadores ya que lo mas probable y lo mejor que puede pasar -->
#Es que encuentren errores en el codigo, lo cual es bueno para poder depurar al 100% el codigo y evitar malas experiencias del usuario
#Hablando de depuracion, existen unos programas especificos para esta funcion, que vienen integrados en IDE o IDLE:
#Un depurador es un programa que evalua el codigo y cuando ocurre un error, muestra especificamente su posicion, el error e incluso -->
#Puede este mismo programa arreglar el error

#Una tecnica de depuracion manual es por impresion, es una tecnica simple y antigüa pero util, donde se utiliza la funcion print -->
#En varias partes del codigo para encontrar en que punto es que el programa falla o no hace el trabajo esperado
#Claramente estas impresiones son solo de confirmacion del programa, lo ideal no seria que se vieran al publico, asi que al finalizar -->
#Se pueden dejar como comentarios o eliminarlas

#Recomendaciones basicas para depurar un codigo:
#1. Solicitar a algun amigo o compañero que lo pruebe, explicandole que debe hacer el programa con todos los detalles
#2. Extraer la parte del codigo donde esta el error y comprobarlo por aparte
#3. Si el error es reciente, revisar en los cambios recientes ya que lo mas probable es que el error se haya generado ahi
#4. Si se ha estado mucho tiempo expuesto/a al programa, descansar haciendo alguna otra actividad para despejar la mente
#5. Ser optimista :)

#Otra forma es una tecnica mas compleja pero que es necesaria implementarla tarde o temprano: Prueba Unitaria (La describiria pero no la entendi xd)

#Se pueden anidar varios errores especificos en un except, ejemplo:
'''while True:
    try:
        number = int(input("Ingresa un número entero: "))
        print(5/number)
        break
    except (ValueError, ZeroDivisionError): #Se hace el uso de 2 errores en un except
        print("Valor incorrecto o se ha roto la regla de división entre cero.")
    except:
        print("Lo siento, algo salió mal...")'''




#EJERCICIOS
'''def divisores(num):
    try:        
        for i in range(num+1):
            if num%i==0:
                print(i,' es divisor')
    except ZeroDivisionError:
        print('indeterminacion')
    except TypeError:
        print(type(num),'Tipo de dato no soportado')
    except ValueError:
        print('Valor no admitido')
var=int(input('ingrese numero: '))
divisores(var)
print('El programa continua en esta linea')'''

def divisores(num):
    try:        
        for i in range(num+1):
            if num%i==0:
                print(i,' es divisor')
    except ZeroDivisionError:
        print('indeterminacion')
    except TypeError:
        print(type(num),'Tipo de dato no soportado')
    except:
        print('Lo siento, hay un error')
        
while True:
    try:
        var=int(input('Ingrese numero: '))
        divisores(var)
        if var==0:
            break
    except ValueError:
        print('Valor no admitido')
    except:
        print('Lo siento, ocurrio un error')