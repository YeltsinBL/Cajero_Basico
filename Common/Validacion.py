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
def valores_ingresados(nombre_campo:str, valor, tipo_dato):
    """Función para validar la nformación ingresada"""
    retorno =  True
    if tipo_dato == 1 and (not valor.isdigit()):
        print("El campo", nombre_campo.upper(),"sólo acepta números enteros,\n\
              vuelva a ingresar la información")
        retorno= False
    elif tipo_dato == 2 and (not tiene_exactamente_un_punto(valor)):
        print("El campo", nombre_campo.upper(),"sólo acepta números,\n\
              vuelva a ingresar la información")
        retorno= False
    elif tipo_dato == 3 and (not valor.isalpha()):
        print("El campo", nombre_campo.upper(),"sólo acepta letras,\n\
              vuelva a ingresar la información")
        retorno= False
    elif tipo_dato == 4 and (not valor.isalnum()):
        print("El campo", nombre_campo.upper(),"sólo aceptan letras y números,\n\
              vuelva a ingresar la información")
        retorno= False
    return retorno
def tiene_exactamente_un_punto(numero):
    """Verifica si solo existe un punto decimal"""
    try:
        num:float
        primer_indice = numero.find(".")
        if primer_indice is -1:
            num = float(numero)
        else:
            if primer_indice is not numero.rfind("."):
                print("Existe más de un punto decimal")
                return False
            else: num = float(numero)
        return isinstance(num,float)
    except ValueError:
        return False
