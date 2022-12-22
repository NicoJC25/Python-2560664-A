import random
#Crear variables de suma y promedio
suma1,suma2,suma3,suma4,suma5=0,0,0,0,0
promedio1,promedio2,promedio3,promedio4,promedio5=0,0,0,0,0
#Lista vacia de dias
Dias=[]
for i in range(30):#Para i en el rango de 30 valores, la lista tendra valores aleatorios entre 4 y 30
    Dias.append(round(random.random()*30-4)+4)
print ('Grados del mes por cada dia:',Dias)
#Se van a hacer rebanadas por cada parte del codigo que se necesita
Dias1=Dias[:15]
Dias2=Dias[15:]
Dias3=Dias[0:10]
Dias4=Dias[10:20]
Dias5=Dias[20:]
#Para i en rango de 15 (para los 15 dias)
for i in range(15):
    suma1+=Dias1[i]#Ambos procesos de promediaran
    suma2+=Dias2[i]
    promedio2=suma2/15
    promedio1=suma1/15
#Para i en rango de 10 (Para los tercios)
for i in range(10):
    suma3+=Dias3[i]#Mismo proceso de suma y promedio
    promedio3=suma3/10
    suma4+=Dias4[i]
    promedio4=suma4/10
    suma5+=Dias5[i]
    promedio5=suma5/10
#Impresion de todos los valores necesarios para mostrar en pantalla
print ('Primera mitad:',Dias1)
print ('Segunda mitad:',Dias2)
print ('Primer tercio:',Dias3)
print ('Segundo tercio:',Dias4)
print ('Tercer tercio:',Dias5)
print ('Promedio de ambas mitades:',promedio1,'y',promedio2)
print ('Promedio de los tres tercios:',promedio3,',',promedio4,'y',promedio5)