'''El usuario ingresará un precio, si el precio es menor a 10000 no tendrá descuento, 
si es menor a 25000 tendrá un descuento del 5% y si es mayor que 26000 tendrá el 10% de descuento sobre la compra'''

precio=int(input('Ingrese un precio: '))

if precio<10000:
    print('El precio no tiene descuento, por lo cual queda en',precio,'pesos')
elif precio>=10000 and precio<25000:
    print('El precio tiene un descuento del 5%, por lo cual su valor total queda en:',precio+precio*5//100,'pesos')
else:
    print('El precio tiene un descuento del 10%, por lo cual su valor total queda en:',precio+precio*10//100,'pesos')