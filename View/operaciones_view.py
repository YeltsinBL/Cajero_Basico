"""Vista del menú de operaciones"""
# region Importaciones
from colorama import Fore, Style
import Common.mensaje as mensaje
import Common.Validacion as validacion
import Controller.OperacionController as operacioncontroller
import View.administrador_view as administradorview
import View.operacion_cliente_view as operacionclienteview
# endregion

msj = mensaje.Mensaje()

# region Funciones de Opciones
def selecciona_operacion(nromenu):
    """Opción para escoger el formulario"""
    inicio = True
    cont = 0
    while inicio:
        try:
            print(Style.BRIGHT + Fore.BLUE)
            print(msj.mensaje_menu("Cliente" if nromenu ==1 else "Administrador"))
            print(Fore.WHITE + Style.NORMAL)
            print("Ingresa el número de operación a realizar:")
            operacioncontroller.listado_opciones_por_menu(nromenu)
            nro_operacion = int(input(""))
            cant = operacioncontroller.cantidad_opciones_por_menu(nromenu)
            if cant < nro_operacion or nro_operacion < 1:
                cont += 1
                inicio = validacion.mensaje_validacion(cont)
                continue
            return nro_operacion
        except (ValueError, TypeError):
            cont +=1
            inicio = validacion.mensaje_validacion(cont)

# endregion

#region Selección de Opciones
def seleccionar_operaciones(opc_menu):
    """Selección de las opciones de Operaciones"""
    iniciar_operacion = True
    while iniciar_operacion:
        opc_operacion= selecciona_operacion(opc_menu)
        if opc_operacion == operacioncontroller.cantidad_opciones_por_menu(opc_menu):
            iniciar_operacion = False
            break
        elif opc_menu == 2 :
            administradorview.seleccion_formulario(opc_operacion)
        else:
            operacionclienteview.seleccion_formulario_operacion_cliente(opc_operacion)
#endregion
