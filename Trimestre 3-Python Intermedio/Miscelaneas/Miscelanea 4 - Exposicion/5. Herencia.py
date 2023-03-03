#Como el objeto se representa a si mismo

'''class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy
        
sun=Star("Sol", "Vía Láctea")
print(sun)'''


#__str__ para representar metodos en cadena

'''class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

    def __str__(self):
        return self.name + ' en ' + self.galaxy

sun=Star("Sol", "Vía Láctea")
print(sun)'''


#Funcion issubclass()

'''class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class TrackedVehicle(LandVehicle):
    pass

for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
    for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
        print(issubclass(cls1, cls2), end="\t")
    print()'''


#Funcion isinstance()

'''class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class TrackedVehicle(LandVehicle):
    pass

my_vehicle = Vehicle()
my_land_vehicle = LandVehicle()
my_tracked_vehicle = TrackedVehicle()

for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
    for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        print(isinstance(obj, cls), end="\t")
    print()'''


#Operador is

'''class SampleClass:
    def __init__(self, val):
        self.val = val
    def getVal(self):
        return self.val

object_1 = SampleClass(0)

print(object_1.getVal())

object_2 = SampleClass(2)
object_3 = object_1
object_3.val += 1

print(object_1.getVal())
print(object_3.getVal())

print(object_1 is object_2)
print(object_2 is object_3)
print(object_3 is object_1)
print(object_1.val, object_2.val, object_3.val)

string_1 = "Mary tenía un "
string_2 = "Mary tenía un corderito"
string_1 += "corderito"

print(string_1 == string_2, string_1 is string_2)'''


#Como python encuentra propiedades y metodos

'''class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Mi nombre es " + self.name + "."

class Sub(Super):
    def __init__(self, name):
        Super.__init__(self, name)

obj = Sub("Andy")

print(obj)'''


#Funcion super

'''class Superior:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Mi nombre es " + self.name + "."

class Sub(Superior):
    def __init__(self, name):
        super().__init__(name)

obj = Sub("Andy")
print(obj)'''


#Acceder a una variable de clase de una superclase desde una subclase

'''class Super:
    supVar = 1

class Sub(Super):
    subVar = 2

obj = Sub()

print(obj.subVar)
print(obj.supVar)'''


#Acceder a una variable de instancia de una superclase desde una subclase

'''class Super:
    def __init__(self):
        self.supVar = 11


class Sub(Super):
    def __init__(self):
        super().__init__()
        self.subVar = 12


obj = Sub()

print(obj.subVar)
print(obj.supVar)'''


#Ejemplo completo de herencia unica

'''class Level1:
    variable_1 = 100
    def __init__(self):
        self.var_1 = 101

    def fun_1(self):
        return 102


class Level2(Level1):
    variable_2 = 200
    def __init__(self):
        super().__init__()
        self.var_2 = 201
    
    def fun_2(self):
        return 202


class Level3(Level2):
    variable_3 = 300
    def __init__(self):
        super().__init__()
        self.var_3 = 301

    def fun_3(self):
        return 302


obj = Level3()

print(obj.variable_1, obj.var_1, obj.fun_1())
print(obj.variable_2, obj.var_2, obj.fun_2())
print(obj.variable_3, obj.var_3, obj.fun_3())'''

