"""Vista para las Operaciones por Administrador"""
# region importaciones
from colorama import Fore, Style
from Common import mensaje
import Controller.ClienteController as clientecontroller
import Controller.dispensador_controller as dispensadorcontroller
import Controller.OperacionController as operacioncontroller
import View.operacion_administrador.gestionar_cliente as cliente
import View.operacion_administrador.gestionar_dispensador as dispensador
# endregion

msj = mensaje.Mensaje()

# region Función para SELECCIONAR FORMULARIO

def seleccionar_acciones_formulario_operacion(opc_operacion):
    """Opción para Mostrar las acciones de los formularios"""
    while True:
        print(Style.BRIGHT + Fore.BLUE)
        print(msj.mensaje_menu("Gestión Cliente"\
                               if opc_operacion ==1 else "Gestión Dispensador"))
        print(Fore.WHITE + Style.NORMAL)
        print("Ingresa el número de la acción a realizar:")
        operacioncontroller.listado_opciones_formulario()
        cant_opc_form = operacioncontroller.cantidad_opciones_formulario()
        nro_accion = input("")
        if nro_accion.isdigit() and int(nro_accion) in range(1,cant_opc_form+1):
            return int(nro_accion)
        print(Style.BRIGHT + Fore.RED)
        print("===============================")
        print(msj.mensaje_opcion_ingresada_incorrecta())
        print("===============================")

def seleccionar_acciones_formulario_operacion_inicial(opc_operacion):
    """Opción para Mostrar las acciones de los formularios"""
    while True:
        print(Style.BRIGHT + Fore.BLUE)
        print(msj.mensaje_menu("Gestión Cliente"\
                               if opc_operacion ==1 else "Gestión Dispensador"))
        print(Fore.WHITE + Style.NORMAL)
        print("Ingresa el número de la acción a realizar:")
        print(1, "Agregar")
        print(6, "Regresar al Menú Administrador")
        nro_accion = input("")
        if nro_accion.isdigit() and int(nro_accion) in {1, 6}:
            return int(nro_accion)
        print(Style.BRIGHT + Fore.RED)
        print("===============================")
        print(msj.mensaje_opcion_ingresada_incorrecta())
        print("===============================")

# endregion

# region Función de Administrador

def seleccion_accion_formulario(opc_accion, opc_operacion):
    """Acciones de acuerdo al formulario seleccionado"""
    match opc_accion:
        case 1:
            _ = cliente.frm_registrar_cliente() if opc_operacion == 1 \
                else dispensador.frm_agregar_dispensador()
        case 2:
            _ = cliente.frm_modificar_cliente() if opc_operacion == 1 \
                else dispensador.frm_modificar_dispensador()
        case 3:
            _ = cliente.frm_buscar_cliente() if opc_operacion == 1 \
                else dispensador.frm_buscar_dispensador()
        case 4:
            _ = cliente.frm_estado_cliente() if opc_operacion == 1 \
                else dispensador.frm_estado_dispensador()
        case 5:
            _ = cliente.frm_listado_cliente() if opc_operacion == 1 \
                else dispensador.frm_listado_dispensadores()

def seleccion_formulario(opc_operacion):
    """Selección del Formulario"""
    iniciar_accion = True
    while iniciar_accion:
        opc_accion: int | None
        if (opc_operacion == 1 and len(clientecontroller.listado_cliente()) == 0) or \
            (opc_operacion == 2 and len(dispensadorcontroller.listado_dispensador()) == 0):
            opc_accion = seleccionar_acciones_formulario_operacion_inicial(opc_operacion)
        else:
            opc_accion = seleccionar_acciones_formulario_operacion(opc_operacion)
        if opc_accion == 6:
            iniciar_accion = False
            break
        seleccion_accion_formulario(opc_accion=opc_accion,
                                    opc_operacion=opc_operacion)

# endregion
