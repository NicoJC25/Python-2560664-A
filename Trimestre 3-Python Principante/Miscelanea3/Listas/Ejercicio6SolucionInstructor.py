import random
aux=True
vec=[0,1]
while aux:
    tam=int(input('Pida un rango entre 5 a 20: '))
    if tam>=5 and tam<=20:
        aux=False
    else:
        print('El numero no es valido')
for i in range(2,tam):
    vec.append(vec[i-1]+vec[i-2])
print (vec)