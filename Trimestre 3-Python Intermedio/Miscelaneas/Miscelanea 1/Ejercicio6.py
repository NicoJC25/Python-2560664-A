'''Determinar que tipo de palabra es: aguda, grave, esdrujula o sobre esdrujula'''

def aguda(cad):
    for i in cad:
        if cad[-1]==chr(225) or cad[-1]==chr(233) or cad[-1]==chr(237) or cad[-1]==chr(243) or cad[-1]==chr(250):
            print('Es aguda')
        elif cad[-2]==chr(255) or cad[-2]==chr(233) or cad[-2]==chr(237) or cad[-2]==chr(243) or cad[-2]==chr(250):
            print('Es aguda')
'''        else:
            print('No es aguda')'''
            
def grave(cad):
    for i in cad:
        if cad[-4]==chr(225) or cad[-4]==chr(233) or cad[-4]==chr(237) or cad[-4]==chr(243) or cad[-4]==chr(250):
            print('Es grave')
        elif cad[-5]==chr(225) or cad[-5]==chr(233) or cad[-5]==chr(237) or cad[-5]==chr(243) or cad[-5]==chr(250):
            print('Es grave')

'''def esdrujula(cad):
    for i in cad:
        if cad[-4]==chr(225) or cad[-4]==chr(233) or cad[-4]==chr(237) or cad[-4]==chr(243) or cad[-4]==chr(250):'''
