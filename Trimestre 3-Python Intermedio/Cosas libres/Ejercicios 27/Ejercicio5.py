'''5.Se requiere un programa que al ingresar el nombre y las horas trabajadas muestre su salario correspondiente.'''

nombre=input('Ingrese el nombre de una persona: ')
horas=int(input('Ingrese las horas trabajadas de esa persona: '))

def salario_h(ht):
  salario=horas*5000
  return salario

print('El salario de la persona',nombre,'de acuerdo a las',horas,'trabajadas es de',salario_h(horas),'pesos')
