'''4.Se necesita un programa el cual permite ingresar el nombre de un jugador famoso y este imprima el club al que pertenece.'''

jugador=input('Ingrese el nombre de un jugador: ')

def club(J):
    try:
        if J=='Cristiano Ronaldo':
            return('Portugal')
        elif J=='Kylian Mbappe':
            return('Francia')
        elif J=='Lionel Messi':
            return('Argentina')
        else:
            return('Lo siento, el jugador escrito no está en el programa :(')
    except:
        print('El dato ingresado no es valido')
    
print(club(jugador))