try:
    val=input('Ingresa un valor: ')
    print(int(val)/len(val))
except ValueError:
    print('Entrada incorrecta')
except ZeroDivisionError:
    print('Entrada erronea')
except TypeError:
    print('Entrada muy incorrecta')
except:
    print('¡Buuu!')