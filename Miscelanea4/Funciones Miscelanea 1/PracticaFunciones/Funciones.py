'''def presentation(first_name, last_name):
    print('Mi nombre es',first_name,last_name)
    
presentation('Nicolas','Juez')'''



'''def presentation(first_name, last_name='Rodriguez'):
    print('Mi nombre es',first_name,last_name)
    
presentation('Nicolas')'''



'''def presentation(first_name='Juan', last_name='Rodriguez'):
    print('Mi nombre es',first_name,last_name)
    
presentation()'''



'''def presentation(first_name, last_name):
    print('Mi nombre es',first_name,last_name)
first_name=input('Ingrese Nombre: ')
last_name=input('Ingrese Apellido: ')
presentation(first_name, last_name)'''



'''def presentation(first_name, last_name):
    print('Mi nombre es',first_name,last_name)
    
presentation(last_name='Juez',first_name='Nicolas')'''


'''import random
def par_impar(numero):
    if numero%2==0:
        print('Par')
    else:
        print('Impar')
        
par_impar(1)
lista=[round(random.randrange(100))for i in range (10)]
print(lista)
for i in lista:
    par_impar(i)'''
    
    

def primo(numero):
    i=1
    contador=0
    while(numero>i):
        if numero%i==0:
            contador+=1
        i+=1
        print(i)
        print(contador)
    if contador>2 or numero<=1:
        print('El numero no es primo')
    else:
        print('El numero es primo')
        
primo(4)



def suma_divisores(numero):
    suma=0
    for i in range(1, numero+1):
        if numero%i==0:
            print(i)
            suma+=i
    print(suma)
suma_divisores(3)