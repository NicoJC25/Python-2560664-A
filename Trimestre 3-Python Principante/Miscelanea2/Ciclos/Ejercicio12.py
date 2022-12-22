'''Escribir un programa que visualice la siguiente figura,
utilizando ciclos. El usuario decide cuantas líneas quiere
imprimir
*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
* * * * * * * *
* * * * * * * * *'''
#Pedir la altura de la figura
n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(n): #Para i en el rango de la altura
    for j in range(i+1): #Para j en el rango de i mas 1 imprimir un asterisco al y separar los renglones
        print("*", end="")
    print("")