'''def ft_and_inch_to_m(ft, inch = 0.0): #Definimos una funcion para pasar pies y pulgadas a metros (decimos que las pulgadas tendran 0 como valor predeterminado)
    return ft * 0.3048 + inch * 0.0254 #Ecuacion para pies y metros
def lb_to_kg(lb): #Definimos una funcion que pase de libras a kilogramos
    return lb * 0.45359237 #Ecuacion correspondiente
def bmi(weight, height): #Definimos una funcion para el bmi
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200: #Verificamos que los datos sean correctos
        return None
    
    return weight / height ** 2 #Ecuacion correspondiente
print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7))) #Imprimimos funcion de bmi donde adentro para el peso invocamos tambien la de libras a kilogramos--
                                                                    #Y para la de altura invocamos la de pies y pulgadas a metros, a su vez ejecutando la ecuacion de bmi'''



'''def is_a_triangle(a, b, c): #Definimos una funcion que indica si puede ser un triangulo lo insertado
    if a + b <= c: #La condicion es que la suma de 2 lados debe ser un numero mayor al del tercer lado por si solo
        return False #Devuelve False si la suma es menor
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True #Devuelve True si la suma es mayor
print(is_a_triangle(1, 1, 1)) #Probar el codigo
print(is_a_triangle(1, 1, 3))'''




'''def is_a_triangle(a, b, c): #Version mas compactada del codigo anterior
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True
print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))'''



'''def is_a_triangle(a, b, c):#Version AUN MAS COMPACTADA
    return a + b > c and b + c > a and c + a > b
print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))'''



'''def is_a_triangle(a, b, c): #Version del codigo anterior donde se piden los 3 lados
    return a + b > c and b + c > a and c + a > b
a = float(input('Ingresa la longitud del primer lado: ')) #Pide el primer lado
b = float(input('Ingresa la longitud del segundo lado: ')) #Pide el segundo lado
c = float(input('Ingresa la longitud del tercer lado: ')) #Pide el tercer lado
if is_a_triangle(a, b, c): #Cambia la respuesta dependiendo si True o False
    print('Si, si puede ser un triángulo.')
else:
    print('No, no puede ser un triángulo.')'''




'''def is_a_triangle(a, b, c): #Mismo de triangulo de antes
    return a + b > c and b + c > a and c + a > b
def is_a_right_triangle(a, b, c): #Definimos funcion para saber si es un triangulo rectangulo con uso del Teorema de Pitagoras
    if not is_a_triangle(a, b, c): #Si la funcion de "is_a_triangle" no es verdad, regresa falso
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
print(is_a_right_triangle(5, 3, 4)) #Probar codigo
print(is_a_right_triangle(1, 3, 4))'''



'''def is_a_triangle(a, b, c): #Misma funcion de ver si es un triangulo o no
    return a + b > c and b + c > a and c + a > b
def heron(a, b, c): #Definimos una funcion de como se debe hacer la formula de Heron
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5
def area_of_triangle(a, b, c): #Definimos una funcion para sacar el area
    if not is_a_triangle(a, b, c): #Si no se cumple la funcion "is_a_trianngle", retorna falso
        return None
    return heron(a, b, c)
print(area_of_triangle(1., 1., 2. ** .5)) #Probar el codigo'''



'''def factorial_function(n): #Definimos la funcion de factoriales
    if n < 0: #Si n es menor a 0, retorna None
        return None
    if n < 2: #Si n es menor a 2, retorna 1
        return 1
    
    product = 1 #El producto sera igual a 1
    for i in range(2, n + 1): #Para i en el rango de 2 hasta n+1
        product *= i #El producto se multiplicara por i hasta finalizar el rango
    return product #Retorna producto
for n in range(1, 6):  #Implementamos un for que indique desde cual numero hasta que otro se realice el factorial (n tomara el valor de cada vuelta del for)
    print(n, factorial_function(n)) #Imprimimos el numero que esta pasando por el momento y el resultado de su factorial'''



'''def fib(n): #Definimos la funcion Fibonacci
    if n < 1: #Si n es menor a 1, retorna None
        return None
    if n < 3: #SI n es menor a 3, retorna 1 (ya que los dos primeros numeros de Fibonacci son 1)
        return 1
    elem_1 = elem_2 = 1 #Se define que elem_1 sera igual a elem_2 que sera igual a 1 (por lo cual ambos tienen como valor 1)
    the_sum = 0 #Se define una variable de suma
    for i in range(3, n + 1): #Para i en el rango de 3 hasta n+1
        the_sum = elem_1 + elem_2 #La suma sera igual a elem_1 y elem_2 sumados
        elem_1, elem_2 = elem_2, the_sum #Para luego indicar que elem_1 pasara a tener el valor de elem_2 y elem_2 pasara a tener el valor de la variable de la suma
    return the_sum #Retorna el valor de la suma
for n in range(1, 10):  #Para n en el rango de 1 hasta 9
    print(n, "->", fib(n)) #Indicar en cual numero de Fibonacci estamos y cual es su contenido'''



'''def fib(n): #Fibonacci mas reducido o en otras palabras, utilizando "recursividad"
    if n < 1: #Si n es menor a 1, retorna None
        return None
    if n < 3: #Si n es menor a 3, retorna 1
        return 1
    return fib(n - 1) + fib(n - 2) #Retornara la invocacion de si misma dentro de si misma, un poco confuso pero entendible. Se sumara n-1 y luego n-2
for n in range(1,10): #Probando la funcion
    print(n,'=',fib(n))'''



'''def factorial_function(n): #Factorial recursivo
    if n < 0: #Si n es menor a 0, retorna None
        return None
    if n < 2: #Si n es menor a 2, retorna 1
        return 1
    return n * factorial_function(n - 1) #Retorna n multiplicado con la misma funcion con "n-1" dentro
for n in range(1,6): #Probamos el codigo
    print(n,'=',factorial_function(n))'''