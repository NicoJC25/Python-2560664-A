#Enfoque Procedimental

'''pila=[]

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
print(pop())

#Imprime cada valor elminado

print(pila)'''



#Enfoque Orientado a Objetos
#Ejemplo 1

'''class pila:
    def __init__(self):
        self.__alm_lista=[]


obj_alm=pila()
print(len(obj_alm.__alm_lista))'''

#Ejemplo 2

class pila:
    def __init__(self):
        self.__lista_pila=[]
        
    def push(self, val):
        self.__lista_pila.append(val)
        
    def pop(self):
        val=self.__lista_pila[-1]
        del self.__lista_pila[-1]
        return val
    
    def ver_pila(self):
        return self.__lista_pila
    
obj_pila=pila()

obj_pila.push(3)
obj_pila.push(2)
obj_pila.push(1)

print(obj_pila.pop())
print(obj_pila.pop())
print(obj_pila.pop())

print(obj_pila.ver_pila())

#Ejemplo 3

'''class pila:
    def __init__(self):
        self.__lista_pila=[]
        
    def push(self, val):
        self.__lista_pila.append(val)
        
    def pop(self):
        val=self.__lista_pila[-1]
        del self.__lista_pila[-1]
        return val
    
    
obj1_pila=pila()
obj2_pila=pila()

obj1_pila.push(3)
obj2_pila.push(obj1_pila.pop())

print(obj2_pila.pop())'''

