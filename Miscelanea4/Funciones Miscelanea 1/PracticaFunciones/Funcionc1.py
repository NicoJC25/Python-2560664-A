def funcion_c(a,b,c):
    signo=input('Escoja el signo: ')
    if signo=='+':
        funcion_cuadratica=(-b+((b**2-(4*a*c))**0.5))//(2*a)
        return funcion_cuadratica
    elif signo=='-':
        funcion_cuadratica=(-b-((b**2-(4*a*c))**0.5))//(2*a)
        return funcion_cuadratica

while True:
    try:
        a=int(input('Ingrese el valor de a: '))
        b=int(input('Ingrese el valor de b: '))
        c=int(input('Ingrese el valor de c: '))
        if a==0 and b==0 and c==0:
            print('Programa finalizado')
            break
        print('La funcion cuadratica es:',funcion_c(a,b,c))
    except ZeroDivisionError:
        print('No se puede dividir entre 0')
    except ValueError:
        print('Solo numeros enteros')
    except:
        print('Hay un dato que no se puede poner, verifique nuevamente')
