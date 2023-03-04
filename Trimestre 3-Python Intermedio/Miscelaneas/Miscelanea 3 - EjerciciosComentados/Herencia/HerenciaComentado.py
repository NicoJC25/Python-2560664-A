class Vehiculo:                                                      #Definimos clase vehiculo
    def __init__(self,tipo):                                         #Constructor de la clase con un parametro de tipo de vehiculo
        self.tipo=tipo                                               #Tipo sera igual al tipo ingresado en un argumento
    def descripcion(self):                                           #Definimos metodo para descripcion del vehiculo
        print('Soy generico no tengo descripcion',self.tipo)         #Contenido del metodo
#v=Vehiculo('Cualquier tipo')

    def getTipo(self):                                               #Definimos metodo para ver el tipo especificado
        return self.tipo                                             #Retonra el tipo
        #return Vehiculo.tipo
    def __str__(self):                                               #Definimos metodo para ver en forma de cadena el objeto
        return 'Soy objeto de la clase Vehiculo'                     #Retorna mensaje

class Herramienta:                                                  
    def __init__(self,proposito):
        self.__proposito=proposito
    def getProposito(self):
        return self.__proposito
    def __str__(self):
        return 'Soy objeto de la clase Herramienta'
class Terrestre(Vehiculo,Herramienta):                               #Subclase llamada terrestre con herencia multiple (subclase de varias clases)
    def __init__(self,tipo,proposito):                               #Iniciador de la subclase con los parametros de los datos de sus clases superiores
        Herramienta.__init__(self,proposito)                         #Constructor de la clase herrmaienta
        Vehiculo.__init__(self,tipo)                                 #Constructor de la clase vehiculo
    def datos(self):                                                 #Definimos metodo para obtener los datos de las otras clases
        print('Tipo: ',super().getTipo())                            #Imprime un texto de tipo y luego gracias a super, va a la clase superior y llama al metodo de obtener el tipo de Vehiculo
        print('Tipo: ',super().getProposito())                       #Lo mismo que con el print anterior pero con la clase Herramienta
    # def __str__(self):
    #     return 'Soy objeto de la clase Terrestre'
               
t=Terrestre("terrestre","carga")
t.datos()
print(t.__str__())