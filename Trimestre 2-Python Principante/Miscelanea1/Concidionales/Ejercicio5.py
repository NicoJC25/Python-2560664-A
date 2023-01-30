'''En un juego de preguntas a las que se responde “Si” o “No” gana quien responda correctamente las tres preguntas. Si se responde mal a cualquiera de
ellas ya no se pregunta la siguiente y termina el juego. Las preguntas son:
1. Colon descubrió América?
2. La independencia de Colombia fue en el año 1810?
3. The Doors fue un grupo de rock Americano?'''
#Pedir primera pregunta
colon=input('¿Colon descubrió América?: ')
#Anidar varios if ya que al no usar ciclos, no hay una funcion especifica para parar el programa al instante
#Entonces se deja el "si no pasa" en vario para que no suelte nada y finalice
if colon=='si':
    print('Correcto, siguiente pregunta')
    independencia=input('¿La independencia de Colombia fue en el año 1810?: ')
    if independencia=='si':
        print('Correcto, siguiente pregunta')
        the_doors=input('¿The Doors fue un grupo de rock Americano?: ')
        if the_doors=='si':
            print('Felicidades, respondio correctamente')