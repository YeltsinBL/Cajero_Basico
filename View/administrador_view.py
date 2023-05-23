"""Vista para el Administrador"""
# region importaciones
import Common.Validacion as validacion
import Controller.ClienteController as clientecontroller
import Controller.OperacionController as operacioncontroller
import View.MenuView as menuview
# endregion

# region Función para seleccionar formulario

def seleccionar_acciones_formulario_operacion():
    """Opción para Mostrar las acciones de los formularios"""
    inicio = True
    cont = 0
    while inicio:
        try:
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

def seleccionar_acciones_formulario_operacion_inicial():
    """Opción para Mostrar las acciones de los formularios"""
    inicio = True
    cont = 0
    while inicio:
        try:
            print("Ingresa el número de la acción a realizar:")
            print(1, "Agregar")
            print(6, "Salir")
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

# region Funciones para los clientes
def selecciona_estado_cliente():
    """Selecciona el tipo a listar de los Clientes por estado"""
    inicio = True
    cont = 0
    while inicio:
        try:
            print()
            print("Ingresa el número del estado")
            operacioncontroller.listado_estados_clientes()
            nro_menu = int(input(""))
            if 3 < nro_menu or nro_menu < 1:
                cont += 1
                inicio = validacion.mensaje_validacion(cont)
                continue
            return nro_menu
        except (ValueError, TypeError):
            cont += 1
            validacion.mensaje_validacion(cont)

def agregar_cliente():
    """Registrar los clientes"""
    menuview.clientes.append(clientecontroller.registrar_cliente())
    print("============================")
    print("¡CLIENTE REGISTRADO!")
    print("============================")
    print("")

def modificar_cliente():
    """Modififcar Cliente"""
    _ = clientecontroller.modificar_cliente(clientes=menuview.clientes)
    print("============================")
    print("¡CLIENTE MODIFICADO!")
    print("============================")
    print("")

def consultar_cliente():
    """Consultar Cliente"""
    clientecontroller.consultar_cliente(menuview.clientes)
    print("")

def estado_cliente():
    """Lista de los Clientes por estado"""
    nro_estado = selecciona_estado_cliente()
    if nro_estado == 3:
        return
    clientecontroller.activo_cliente(menuview.clientes, nro_estado)
    estado = "activo" if nro_estado == 1 else "desactivo"
    print("============================================")
    print("¡TODOS LOS CLIENTES", estado.upper()+"S!")
    print("============================================")
    print("")
# endregion

# region Función de Administrador


def seleccion_accion_formulario(opc_accion, opc_operacion):
    """Acciones de acuerdo al formulario seleccionado"""
    # mostrar_seleccionados(opc_menu,opc_operacion,opc_accion)
    match opc_accion:
        case 1:
            _ = agregar_cliente() if opc_operacion == 1 \
                else print("Registrar Dispensador")
        case 2:
            _ = modificar_cliente() if opc_operacion == 1 \
                else print("Modificar Dispensador")
        case 3:
            _ = consultar_cliente() if opc_operacion == 1 \
                else print("Consultar Dispensador")
        case 4:
            _ = estado_cliente() if opc_operacion == 1 \
                else print("Estado Dispensador")
        case 5:
            _ = clientecontroller.listado_clientes(menuview.clientes) if opc_operacion == 1 \
                else print("Listar Dispensador")


def seleccion_formulario(opc_operacion):
    """Selección del Formulario"""
    iniciar_accion = True
    while iniciar_accion:
        opc_accion: int | None
        if (opc_operacion == 1 and len(menuview.clientes) == 0) or \
                (opc_operacion == 2 and len(menuview.dispensadores) == 0):
            opc_accion = seleccionar_acciones_formulario_operacion_inicial()
        else:
            opc_accion = seleccionar_acciones_formulario_operacion()
        if opc_accion == 6:
            iniciar_accion = False
            break
        seleccion_accion_formulario(opc_accion=opc_accion,
                                    opc_operacion=opc_operacion)

# endregion
