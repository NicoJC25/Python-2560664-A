'''1.Solicitar 2 números al usuario e imprimir el cociente y el residuo del mayor en el menor.'''

N1=int(input('Ingrese el primer numero: '))
N2=int(input('Ingrese el segundo numero: '))

def division(N1,N2):
    if N2>N1:
        N1,N2=N2,N1
        
    cociente=N1/N2
    residuo=N1%N2
    print ('El cociente de la division es:',cociente,'y el residuo es:',residuo)

division(N1,N2)