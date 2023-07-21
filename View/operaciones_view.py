"""Vista del menú de operaciones"""
# region Importaciones
from colorama import Fore, Style
from Common import mensaje
import Controller.OperacionController as operacioncontroller
import Controller.ClienteController as clientecontroller
import View.administrador_view as administradorview
import View.operacion_cliente_view as operacionclienteview
# endregion

msj = mensaje.Mensaje()

# region Funciones de Opciones
def selecciona_operacion(nromenu):
    """Opción para escoger el formulario"""
    while True:
        print(Style.BRIGHT + Fore.BLUE)
        print(msj.mensaje_menu("Cliente" if nromenu ==1 else "Administrador"))
        print(Fore.WHITE + Style.NORMAL)
        print("Ingresa el número de operación a realizar:")
        operacioncontroller.listado_opciones_por_menu(nromenu)
        cant = operacioncontroller.cantidad_opciones_por_menu(nromenu)
        nro_operacion = input("")
        if nro_operacion.isdigit() and int(nro_operacion) in range(1,cant+1):
            return int(nro_operacion)
        print(Style.BRIGHT + Fore.RED)
        print("===============================")
        print(msj.mensaje_opcion_ingresada_incorrecta())
        print("===============================")

# endregion

#region Selección de Opciones
def seleccionar_operaciones(opc_menu):
    """Selección de las opciones de Operaciones"""
    iniciar_operacion = True
    while iniciar_operacion:
        opc_operacion= selecciona_operacion(opc_menu)
        if opc_operacion == operacioncontroller.cantidad_opciones_por_menu(opc_menu):
            iniciar_operacion = False
        elif opc_menu == 2 :
            administradorview.seleccion_formulario(opc_operacion)
        else:
            contar =0
            if opc_operacion == 3:
                clientes = clientecontroller.listado_cliente()
                for cliente in clientes:
                    if cliente[5] == 1:
                    # if cliente.estado == 1:
                        contar+=1
                if contar <=1:
                    print(msj.mensaje_mantenimiento("Operación de Transferencia"))
                else:
                    operacionclienteview.seleccion_formulario_operacion_cliente(opc_operacion)
            else:
                operacionclienteview.seleccion_formulario_operacion_cliente(opc_operacion)
#endregion
