import sys

def mensaje_validacion(cont):
    """Mensaje para las validaciones"""
    retorno: bool
    if cont == 3:
        print("Gracias por su visita")
        retorno = False
        sys.exit(0)
    else:
        intent = lambda cont : "intento" if(3-cont == 1) else "intentos"
        print("Ingresa un número de las opciones mostradas, por favor")
        print(f"Le queda {3 - cont}", intent(cont))
        retorno = True
    return retorno
