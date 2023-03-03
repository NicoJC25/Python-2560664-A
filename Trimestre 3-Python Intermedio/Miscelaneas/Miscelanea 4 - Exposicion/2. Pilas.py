#Enfoque procedimental

'''pila = []

def push(val):
    pila.append(val)

def pop():
    val=pila[-1]
    del pila[-1]
    return val

push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())'''


#Enfoque orientado a objetos
#Primer ejemplo - Como hacer el constructor

'''class Pila:  # Definiendo la clase de la pila.
    def __init__(self):  # Definiendo la función del constructor.
        print("¡Hola!")


stack_object=Pila()  # Instanciando el objeto.'''


#Segundo ejemplo - Ingresando a un metodo

'''class Pila:
    def __init__(self):
        self.stack_lista=[]


stack_object = Pila()
print(len(stack_object.stack_lista))'''


#Tercer ejemplo - Objetos privados

'''class Pila:
    def __init__(self):
        self.__stack_lista=[]


stack_object = Pila()
print(len(stack_object.__stack_lista))'''


#Cuarto ejemplo - La pila

'''class Pila:
    def __init__(self):
        self.__stack_lista=[]


    def push(self, val):
        self.__stack_lista.append(val)


    def pop(self):
        val = self.__stack_lista[-1]
        del self.__stack_lista[-1]
        return val


stack_object = Pila()

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())'''


#Quinto ejemplo - Varios objetos de una clase

'''class Pila:
    def __init__(self):
        self.__stack_lista=[]

    def push(self, val):
        self.__stack_lista.append(val)

    def pop(self):
        val = self.__stack_lista[-1]
        del self.__stack_lista[-1]
        return val


stack_object_1 = Pila()
stack_object_2 = Pila()

stack_object_1.push(3)
stack_object_2.push(stack_object_1.pop())

print(stack_object_2.pop())'''


#Sexto ejemplo - Subclases

class Pila:
    def __init__(self):
        self.__stack_lista=[]

    def push(self, val):
        self.__stack_lista.append(val)

    def pop(self):
        val = self.__stack_lista[-1]
        del self.__stack_lista[-1]
        return val


class AdicionarPila(Pila):
    def __init__(self):
        Pila.__init__(self)
        self.__sum = 0
        

#Septimo ejemplo - Push +

class Pila:
    def __init__(self):
        self.__stackLista=[]

    def push(self, val):
        self.__stackLista.append(val)

    def pop(self):
        val = self.__stackLista[-1]
        del self.__stackLista[-1]
        return val


class AddingStack(Pila):
    def __init__(self):
        Pila.__init__(self)
        self.__sum = 0

    def push(self, val):
        self.__sum+=val
        Pila.push(self, val)


#Octavo ejemplo - Pila completa

class Pila:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


class AddingStack(Pila):
    def __init__(self):
        Pila.__init__(self)
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Pila.push(self, val)

    def pop(self):
        val=Pila.pop(self)
        self.__sum-=val
        return val


stack_object=AddingStack()

for i in range(5):
    stack_object.push(i)
print(stack_object.get_sum())

for i in range(5):
    print(stack_object.pop())


