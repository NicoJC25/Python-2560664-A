#Funciones y tuplas
'''
"""1. Ejercicio de un ahorcado donde se inserta la palabra a buscar y otro usuario hace el intento de encontrar la misma."""
def ahorcado():
    palabra_secreta=str(input("ingresa la palabra secreta:\n"))
    lista = []
    for i in range(len(palabra_secreta)):
        lista.append(palabra_secreta[i])
    lista2=[]
    for k in range(len(palabra_secreta)):
        lista2.append("-")
    print(lista2)
    cont=0
    while cont <6:
        letra=input("Letra que esta en la palabra:\n")
        if letra in lista:
            print("La letra si estaba en la palabra")
            for j in range(len(lista)):
                if letra == lista[j]:
                    lista2.insert(j,letra)
                    del lista2 [j+1]
                    print(lista2)
            if lista2 == lista:
                print("!Ganaste¡")
                break
        else:
            print("No estaban en la palabra:")
            cont+=1
            if cont ==1:
                print(" *\n"*4,"******")
            elif cont==2:
                print(" *       *****\n"*4,"******  *****")
            elif cont==3:
                print(" *       ***** *****\n"*4,"******  ***** *****")
            elif cont==4:
                print(" *       ***** ***** *****\n *       ***** ***** *\n *       ***** ***** *****\n *       ***** *****      *\n *       ***** *****      *\n","******  ***** ***** *****")
            elif cont==5:
                print(" *       ***** ***** *****  *****\n *       ***** *****  *     *\n *       ***** ***** *****  *\n *       ***** *****      * *****\n *       ***** *****      * *\n","******  ***** ***** *****  *****")
            elif cont==6:
                print(" *       ***** ***** ***** *****  *****\n *       ***** ***** *      *     *   *\n *       ***** ***** *****  *     *   *\n *       ***** *****      * ***** *  *\n *       ***** *****      * *     * *\n","******  ***** ***** ***** *****  *  *")
                print('¡Perdiste!')
ahorcado()
'''


#a=input("ponga"())
"""
pais2={'colombia ':'bogota', "mexico":"cdmx" }
try:
    def buscacap(pais2):
        capital=input('Ponga el nombre del pais: ')
        for c in pais2.keys():
            if c==capital:
                print(pais2[c])
            else:
                print('No se encontró el pais escrito')
except:
    print('Lo siento, hay un error en el codigo')

buscacap(pais2)"""





my_tuple = (1,)


def tri(Mt):
    for i in range(1,11):
        t2 = my_tuple * i
        print (t2)

print(tri(my_tuple))
