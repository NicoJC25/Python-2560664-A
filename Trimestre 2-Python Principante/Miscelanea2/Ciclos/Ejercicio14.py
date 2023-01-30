'''Calcular todos los números de 3 cifras tales que la suma
de los cubos de las cifras es igual al valor del número.'''
#Asignar variable valor
valor = 0
for n in range (100, 1000+1): #Para n en rango de 100 a 1000, valor sera igual a n, para guardar el primero valor
    valor = n
    u=n%10 #Las unidades se sacan usando el mod con la ultima cifra del numero, sacando este ultimo valor
    n=n//10 #Luego se quita el restante del numero para pasar a la siguiente cifra dividiendo entre 10
    d=n%10 #Y se repite el proceso con decenas y centenas
    n=n//10
    c=n%10
    u**=3 #Cada cifra se elevara a la 3
    d**=3
    c**=3
    suma = u+d+c #Y se sumaran
    if suma == valor: #Si la suma de las cifras es igual al valor principal, se imprime
        print (valor)