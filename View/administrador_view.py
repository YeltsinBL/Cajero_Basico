"""Vista para las Operaciones por Administrador"""
# region importaciones
from colorama import Fore, Style
from Common import mensaje
import Controller.ClienteController as clientecontroller
import Controller.dispensador_controller as dispensadorcontroller
import Controller.MenuController as menucontroller
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
                               if opc_operacion ==4 else "Gestión Dispensador"))
        print(Fore.WHITE + Style.NORMAL)
        print("Ingresa el número de la acción a realizar:")
        lista_menu =[]
        nueva_lista={}
        if len(lista_menu)==0:
            lista_menu = menucontroller.listar_menu(opc_operacion)
        for resultado in lista_menu:
            print(resultado[0], resultado[1])
            nueva_lista[resultado[0]]=resultado[2]
        nro_accion = input("")
        if nro_accion.isdigit() and int(nro_accion)\
            in list(range(len(lista_menu)+1)):
            return int(nro_accion), nueva_lista
        print(Style.BRIGHT + Fore.RED)
        print("===============================")
        print(msj.mensaje_opcion_ingresada_incorrecta())
        print("===============================")

def seleccionar_acciones_formulario_operacion_inicial(opc_operacion):
    """Opción para Mostrar las acciones de los formularios"""
    while True:
        print(Style.BRIGHT + Fore.BLUE)
        print(msj.mensaje_menu("Gestión Cliente"\
                               if opc_operacion ==4 else "Gestión Dispensador"))
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

def seleccion_accion_formulario(opc_accion, lista_menu, opc_operacion):
    """Acciones de acuerdo al formulario seleccionado"""
    match opc_accion:
        case 1:
            _ = cliente.frm_registrar_cliente() if opc_operacion == 4 \
                else dispensador.frm_agregar_dispensador()
        case 2:
            _ = cliente.frm_modificar_cliente() if opc_operacion == 4 \
                else dispensador.frm_modificar_dispensador()
        case 3:
            _ = cliente.frm_buscar_cliente() if opc_operacion == 4 \
                else dispensador.frm_buscar_dispensador()
        case 4:
            _ = cliente.frm_estado_cliente(lista_menu.get(int(opc_accion))) if opc_operacion == 4 \
                else dispensador.frm_estado_dispensador(lista_menu.get(int(opc_accion)))
        case 5:
            _ = cliente.frm_listado_cliente() if opc_operacion == 4 \
                else dispensador.frm_listado_dispensadores()

def seleccion_formulario(opc_operacion):
    """Selección del Formulario"""
    iniciar_accion = True
    while iniciar_accion:
        opc_accion: int | None
        if (opc_operacion == 4 and len(clientecontroller.listado_cliente()) == 0) or \
            (opc_operacion == 5 and len(dispensadorcontroller.listado_dispensador()) == 0):
            opc_accion = seleccionar_acciones_formulario_operacion_inicial(opc_operacion)
        else:
            opc_accion, lista = seleccionar_acciones_formulario_operacion(opc_operacion)
        if opc_accion == len(lista):
            iniciar_accion = False
            break
        seleccion_accion_formulario(opc_accion=opc_accion,
                                    lista_menu= lista,
                                    opc_operacion=opc_operacion)

# endregion
