#Self a profundidad

'''class Classy:
    def method(self):
        print("método")


obj = Classy()
obj.method()'''


#Self a produndidad V2

'''class Classy:
    def method(self, par):
        print("método:", par)


obj = Classy()
obj.method(1)
obj.method(2)
obj.method(3)'''


#Acceder a la instancia de un objeto y variables de clase con self

'''class Classy:
    varia=2
    def method(self):
        print(self.varia, self.var)


obj = Classy()
obj.var = 3
obj.method()'''


#Invocar otros metodos de la clase con self

'''class Classy:
    def other(self):
        print("otro")

    def method(self):
        print("método")
        self.other()


obj=Classy()
obj.method()'''


#Constructor

'''class Classy:
    def __init__(self, value):
        self.var = value


obj_1=Classy("objeto")

print(obj_1.var)'''


#None en un constructor

'''class Classy:
    def __init__(self, value = None):
        self.var = value


obj_1=Classy("objeto")
obj_2=Classy()

print(obj_1.var)
print(obj_2.var)'''


#Metodos ocultos

'''class Classy:
    def visible(self):
        print("visible")
    
    def __hidden(self):
        print("oculto")

obj=Classy()
obj.visible()

try:
    obj.__hidden()
except:
    print("fallido")

obj._Classy__hidden()'''


#__dict__ con metodos

'''class Classy:
    varia=1
    def __init__(self):
        self.var = 2

    def method(self):
        pass

    def __hidden(self):
        pass


obj=Classy()

print(obj.__dict__)
print(Classy.__dict__)'''


#__name__ con metodos

'''class Classy:
    pass

print(Classy.__name__)
obj = Classy()
print(type(obj).__name__)'''


#__module__ con metodos

'''class Classy:
    pass


print(Classy.__module__)
obj = Classy()
print(obj.__module__)'''


#__bases__ con metodos

'''class SuperOne:
    pass

class SuperTwo:
    pass

class Sub(SuperOne, SuperTwo):
    pass

def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')

printBases(SuperOne)
printBases(SuperTwo)
printBases(Sub)'''


