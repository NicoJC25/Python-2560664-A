'''class Hotel:
    pass

Cliente=Hotel()'''

class ExampleClass:
    def __init__(self, val = 1):
        self.__first = val                  #Variable de instancia

    def set_second(self, val = 2):
        self.__second = val                 #Otra variable de instancia


example_object_1 = ExampleClass()           #Va a tomar el valor de la primer funcion al ser la constructora
example_object_2 = ExampleClass(2)          #Para este, se renombra y se indic que la primer variable de instancia ya no valdra 1, sino 2

example_object_2.set_second(3)              #Ahora se le va a poner que en el segundo metodo, va a tener el valor de 3

example_object_3 = ExampleClass(4)          #Para este, se renombra que la primer variable de instancia tendra como valor 4
example_object_3.__third = 5                #Y ahora se crea una tercer variable de instancia fuera de la clase que tendra como valor 5


print(example_object_1.__dict__)            #Con dict, imprimimos en forma de diccionario la variable y su valor
print(example_object_2.__dict__)
print(example_object_3.__dict__)
