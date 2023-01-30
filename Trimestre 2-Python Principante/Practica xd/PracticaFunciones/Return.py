'''def boring_function():
    print("'Modo aburrimiento' ON.")
    return 123
print("¡Esta lección es interesante!")
boring_function()
print("Esta lección es aburrida...")'''



'''value = None
if value is None:
    print("Lo siento, no contienes ningún valor")'''




'''def strange_function(n):
    if(n%2 == 0):
        return True
print(strange_function(2))
print(strange_function(1))'''



'''def list_sum(lst):
    s=0
    for elem in lst:
        s+=elem
    
    return s
print(list_sum([5, 4, 3]))'''



'''def strange_list_fun(n):
    strange_list=[]
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list
print(strange_list_fun(10))'''




'''def is_year_leap(year):
    if year%4!=0:#Si el año no es divisible entre 4, no es bisiesto
        return False
    elif year%4==0 and year%100!=0:#Si el año es divisible entre 4 pero no entre 100, es bisiesto
        return True
    elif year%4==0 and year%100==0 and year%400!=0:#Si el año es divisible entre 4 y 100 pero no entre 400, no es bisiesto
        return False 
    elif year%4==0 and year%100==0 and year%400==0:#Si el año es divisible entre 4, 100 y 400, es bisiesto
        return True
print(is_year_leap())'''



'''def par_impar(numero):
    if numero%2==0 and numero>=2:
        return 'Par'
    elif numero==0:
        return 'El numero es 0'
    else:
        return 'Impar'
    
print(par_impar(0))
import random
lista=[round(random.randrange(100))for i in range (10)]
print(lista)
for i in lista:
    print(par_impar(i))'''




def suma_divisores(numero):
    suma=0
    for i in range(1, numero):
        if numero%i==0:
            suma+=i
    return suma


def perfecto(numero_perfecto):
    suma=suma_divisores(numero_perfecto)
    if suma==numero_perfecto:
        return 'El numero es perfecto'
    else:
        return 'El numero no es perfecto'
    



def primo(numero):
    numero_primo=suma_divisores(numero)
    if numero_primo==1:
        return 'El numero es primo'
    else:
        return 'El numero no es primo'
print('El numero es 6')
print('La suma de los divisores es:',suma_divisores(6))
print(perfecto(6))
print(primo(6))


def numeros_amigos(numero_x,numero_y):
    x=suma_divisores(numero_x)
    y=suma_divisores(numero_y)
    if numero_x==y and numero_y==x:
        return 'Son numeros amigos'
    else:
        return 'No son numeros amigos'
    
print(numeros_amigos(220,284))