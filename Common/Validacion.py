"""Validaciones Globales"""
import sys
from colorama import Fore, Style

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
    """Función para validar la información ingresada"""
    retorno =  True
    if tipo_dato == 1 and (not valor.isdigit()):
        print(Style.BRIGHT + Fore.RED+
              "El campo", nombre_campo.upper(),"sólo acepta números enteros"
              +Style.NORMAL + Fore.WHITE)
        retorno= False
    elif tipo_dato == 2 and (not tiene_exactamente_un_punto(valor)):
        print(Style.BRIGHT + Fore.RED+
              "El campo", nombre_campo.upper(),"sólo acepta números"
              +Style.NORMAL + Fore.WHITE)
        retorno= False
    elif tipo_dato == 3 and (not valor.isalpha()):
        print(Style.BRIGHT + Fore.RED+
              "El campo", nombre_campo.upper(),"sólo acepta letras"
              +Style.NORMAL + Fore.WHITE)
        retorno= False
    elif tipo_dato == 4 and (not valor.isalnum()):
        print(Style.BRIGHT + Fore.RED+
              "El campo", nombre_campo.upper(),"sólo aceptan letras y números"
              +Style.NORMAL + Fore.WHITE)
        retorno= False
    elif tipo_dato == 5 and not (valor.lower() == "activo" or valor.lower() == "desactivo"):
        print(Style.BRIGHT + Fore.RED+
              "El campo", nombre_campo.upper(),"sólo las palabras \"Activo\" y \"Desactivo\""
              +Style.NORMAL + Fore.WHITE)
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
                print(Style.BRIGHT + Fore.RED+
                      "Existe más de un punto decimal"
                      +Style.NORMAL + Fore.WHITE)
                return False
            else: num = float(numero)
        return isinstance(num,float)
    except ValueError:
        return False
