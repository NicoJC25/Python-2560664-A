#Herencia multiple

'''class SuperA:
    var_a = 10
    def fun_a(self):
        return 11

class SuperB:
    var_b = 20
    def fun_b(self):
        return 21

class Sub(SuperA, SuperB):
    pass

obj = Sub()

print(obj.var_a, obj.fun_a())
print(obj.var_b, obj.fun_b())'''


#Que pasa si dos superclases tienen el mismo nombre de variables

'''class SuperA:
    var_a = 10
    def fun_a(self):
        return 11

class SuperB:
    var_b = 20
    def fun_b(self):
        return 21

class Sub(SuperA, SuperB):
    pass

obj = Sub()

print(obj.var_a, obj.fun_a())
print(obj.var_b, obj.fun_b())'''


#Superclases con variables con el mismo nombre

'''class Left:
    var = "L"
    var_left = "LL"
    def fun(self):
        return "Left"

class Right:
    var = "R"
    var_right = "RR"
    def fun(self):
        return "Right"

class Sub(Left, Right):
    pass

obj=Sub()
print(obj.var, obj.var_left, obj.var_right, obj.fun())'''


#Clases con el mismo nombre de metodos

'''class One:
    def do_it(self):
        print("do_it de One")

    def doanything(self):
        self.do_it()

class Two(One):
    def do_it(self):
        print("do_it de Two")

one=One()
two=Two()

one.doanything()
two.doanything()'''


#Problema con nombres

import time

'''class TrackedVehicle:
    def control_track(left, stop):
        pass
    def turn(left):
        control_track(left, True)
        time.sleep(0.25)
        control_track(left, False)

class WheeledVehicle:
    def turn_front_wheels(left, on):
        pass
    def turn(left):
        turn_front_wheels(left, True)
        time.sleep(0.25)
        turn_front_wheels(left, False)'''
        
        
        
#Polimorfismo

'''import time

class Vehicle:
    def change_direction(left, on):
        pass
    def turn(left):
        change_direction(left, True)
        time.sleep(0.25)
        change_direction(left, False)

class TrackedVehicle(Vehicle):
    def control_track(left, stop):
        pass
    def change_direction(left, on):
        control_track(left, on)

class WheeledVehicle(Vehicle):
    def turn_front_wheels(left, on):
        pass
    def change_direction(left, on):
        turn_front_wheels(left, on)'''


#MRO bien aplicado

'''class Top:
    def m_top(self):
        print("top")

class Middle(Top):
    def m_middle(self):
        print("middle")

class Bottom(Middle, Top):
    def m_bottom(self):
        print("bottom")

object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()'''


#MRO mal aplicado

'''class Top:
    def m_top(self):
        print("top")

class Middle(Top):
    def m_middle(self):
        print("middle")

class Bottom(Top, Middle):
    def m_bottom(self):
        print("bottom")

object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()'''


#Metodo diamante

'''class Top:
    def m_top(self):
        print("top")

class Middle_Left(Top):
    def m_middle(self):
        print("middle_left")

class Middle_Right(Top):
    def m_middle(self):
        print("middle_right")

class Bottom(Middle_Left, Middle_Right):
    def m_bottom(self):
        print("bottom")

object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()'''