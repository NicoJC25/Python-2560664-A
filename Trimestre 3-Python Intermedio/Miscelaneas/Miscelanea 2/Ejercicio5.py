#Aqui se encuentra el ejercicio correspondiente a la excepcion NameError en el cual se invoca la funcion
#mal  tras la cual en la terminal aparecera un mensaje indicando esto ultimo.

try:
 def sumasimple():
     dig1=int(input("ingrese el primer digito: "))
     dig2=int(input("ingrese el sefungo digito: "))
     sum=(dig1+dig2)
     print ("el resultado es: ",sum)

 sumasimpl()
except NameError:
    print("No se invoco a la funcion correctamente") 