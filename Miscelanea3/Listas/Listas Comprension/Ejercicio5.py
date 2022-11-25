import random
'''Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. 
Llene la lista con números aleatorios. Solicite al usuario un número para buscar en la lista. 
Diga cuantas veces está y en que posiciones esta. Si no está agréguelo al final de la lista'''
#Crear una lista vacia y la cantidad de valores entre 10 y 25
cont=0
Posicion=''
rango=random.randint(10,25)
vector=[round(random.random()*100)for i in range(rango)]#Lista comprendida donde los numeros de la lista seran de 1 a 100 en el rango de rango
print(vector)
#Pedir el numero
Numero=int(input('Elija el numero: '))
#Para i en el rango de la ecucacion anterior, si el numero insertado es igual a alguno de los valores de la lista
for i in range(rango):
    if Numero==vector[i]:
        Posicion+=str(i)+' '#La posicion sera igual a esta misma mas el string de i ademas de un espacio entre cada valor de posicion si es que se repite el numero
        cont+=1#El contador aumentara 1
if cont==0:#Si el contador es igual a 0
    vector.append(Numero)#Se agregara el numero insertado al final de la lista
    print('El numero se agrego al final de la lista')
    print(vector)
else:#De lo contrario, si el contador es igual a 1, soltar el mensaje en singular
    if cont==1:
        print('El numero de la lista',Numero,'esta 1 vez y esta en la posicion',Posicion)
    else:#Si no, solarlo en plural
        print ('El numero de la lista',Numero,'esta',cont,'veces y esta en las posiciones',Posicion)