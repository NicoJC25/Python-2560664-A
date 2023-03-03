#Metodo "__str__()"

#Este metodo lo que hace es retornar el significado de un objeto en forma de cadena. Ejemplo:

'''class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

    def __str__(self):
        return self.name + ' en ' + self.galaxy


sun = Star("Sol", "Vía Láctea")
print(sun) #Resultado: Sol en Vía Láctea'''



#Metodo issubclass()

#Este metodo lo que hace es, al ponerle un argumento, identifica si eso es una subclase o no. Ejemplo:

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

#Nota: Cada clase se considera sub-clase de si misma



#Metodo isinstance()

#Este metodo lo que hace es identificar de acuerdo a un objeto y una clase especificados, si el objeto pertenece a esa clase...
#...o subclase. Ejemplo:

'''class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class TrackedVehicle(LandVehicle):
    pass

my_vehicle = Vehicle()                  #Se crean 3 objetos, cada uno siendo de cada clase hecha
my_land_vehicle = LandVehicle()
my_tracked_vehicle = TrackedVehicle()

for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
    for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        print(isinstance(obj, cls), end="\t")
    print()'''

#Nota: Al igual que con el metodo anterior, cada clase se considera una instancia de si misma y cada subclase instancia de su clase superior



#Operador "is"

#Con este operador, podemos comprobar si un objeto es igual al otro. Recordar que una variable no almacena el objeto en si...
#...sino que almacena los identificadores que apuntan a la memoria interna de Python. Ejemplo:

'''class SampleClass:
    def __init__(self, val):
        self.val = val


object_1 = SampleClass(0) 
object_2 = SampleClass(2)
object_3 = object_1
object_3.val += 1

print(object_1 is object_2) #False
print(object_2 is object_3) #False 
print(object_3 is object_1) #True
print(object_1.val, object_2.val, object_3.val) #1, 2, 1

string_1 = "Mary tenía un "
string_2 = "Mary tenía un corderito"
string_1 += "corderito"

print(string_1 == string_2, string_1 is string_2) #True, False'''

#Como se puede ver, como tal aunque dos variables tengan el mismo valor, no son lo mismo si ambas no tienen el mismo origen



