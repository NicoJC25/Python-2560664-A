#Aqui un ejemplo del la  Excepcion ModuleNotFoundError la cual solo aparece si el modulo que se  ha importado en
#un programa no existe o no se importo de manera correcta al programa
try:
  import pinzon
  from pinzon import sumasimple
  sumasimple(23,45)
except ModuleNotFoundError:
     print("El modulo que desea usar no existe o no esta didsponible ")
