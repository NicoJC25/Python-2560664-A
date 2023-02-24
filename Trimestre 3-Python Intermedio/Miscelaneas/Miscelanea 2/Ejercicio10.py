try:
    d=2+ "Hola"
except Exception:
    print(" ha habido una excepcion")

try:
    d=2+"hola"
except Exception as ex:
    print(" Ha habido una excepcion",type(ex))