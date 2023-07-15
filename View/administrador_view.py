"""Vista para las Operaciones por Administrador"""
# region importaciones
from colorama import Fore, Style
import Common.Validacion as validacion
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
    inicio = True
    cont = 0
    while inicio:
        try:
            print(Style.BRIGHT + Fore.BLUE)
            print(msj.mensaje_menu("Gestión Cliente"\
                                   if opc_operacion ==1 else "Gestión Dispensador"))
            print(Fore.WHITE + Style.NORMAL)
            print("Ingresa el número de la acción a realizar:")
            operacioncontroller.listado_opciones_formulario()
            cant_opc_form = operacioncontroller.cantidad_opciones_formulario()
            nro_accion = int(input(""))
            if cant_opc_form < nro_accion or nro_accion < 1:
                cont += 1
                inicio = validacion.mensaje_validacion(cont)
                continue
            return nro_accion
        except (ValueError, TypeError):
            cont +=1
            inicio = validacion.mensaje_validacion(cont)

def seleccionar_acciones_formulario_operacion_inicial(opc_operacion):
    """Opción para Mostrar las acciones de los formularios"""
    inicio = True
    cont = 0
    while inicio:
        try:
            print(Style.BRIGHT + Fore.BLUE)
            print(msj.mensaje_menu("Gestión Cliente"\
                                   if opc_operacion ==1 else "Gestión Dispensador"))
            print(Fore.WHITE + Style.NORMAL)
            print("Ingresa el número de la acción a realizar:")
            print(1, "Agregar")
            print(6, "Regresar al Menú Administrador")
            nro_accion = int(input(""))
            if nro_accion == 6 or nro_accion == 1:
                return nro_accion
            else:
                cont += 1
                inicio = validacion.mensaje_validacion(cont)
                continue
        except (ValueError, TypeError):
            cont +=1
            inicio = validacion.mensaje_validacion(cont)

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
