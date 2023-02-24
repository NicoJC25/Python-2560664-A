#la excepcion AritmeticError es similar a zerodivisionerror por lo tanto se recomienda al usuario si quiere verificar la 
#funcionalidad de la excepcion que use la funcion de division y divida un digito cualquiera entre zero
#aunque las otras tambien estan disponibles.

menu1=print("presione 1 para dividir dos numeros")
menu2=print("presione 2 para pasar sumar dos numeros")
menu3=print("presione 3 para restar dos numeros")
try:
    number=(int(input("presione el numero correspondiente a la opcion que desea usar: ")))
except ValueError:
    print("el dato ingresado no esta soportado reinicie el programa")

def div():
 try:
     v1=int(input("ingrese el primer digito: "))
     v2=int(input("ingrese el segundo digito: "))
     total=(v1/v2)
     print(total)
 except ArithmeticError:
     print("su division a provocado un aritmetic error por favor reinicie el programa")
 except ValueError:
     print("el digito que ingreso no es un numero reinicie el programa")

def sum():
 try:
     s1=int(input("ingrese el primer digito: "))
     s2=int(input("ingrese el segundo digito:  "))
     totalsum=(s1+s2)
     print(totalsum)
 except ArithmeticError:
     print("su suma a provocado un aritmetic error por favor reinicie el programa")
 except ValueError:
     print("el digito que ingreso no es un numero reinicie el programa")


def res():
  try:
     n1=int(input("ingrese el primer digito: "))
     n2=int(input("ingrese el segundo digito"))
     totalres=(n1-n1)
     print(totalres)
  except ArithmeticError:
      print("su resta a provocado un aritmetic error por favor reinicie el programa")
  except ValueError:
     print("el digito que ingreso no es un numero reinicie el programa")

def multi():
 try:
      x1=int(input("ingrese el  primer digito: "))
      x2=int(input("ingrese el segundo digito: "))
      totalmulti=(x1*x2)
      print(totalmulti)
 except ArithmeticError:
     print("su multiplicacion a provocado un aritmetic error por favor reinicie el programa")
 except ValueError:
     print("el digito que ingreso no es un numero reinicie el programa")

try:
 if number==1:
     div()
 elif number==2:
     sum()
 if number==3:
     res()
 elif number==4:
     multi()
except NameError:
    print("") 
       
