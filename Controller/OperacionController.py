"""Funciones que interactúan con las opciones de Operaciones"""
import Model.Operacion as operacion

# LISTADO DE LAS OPCIONES
def listado_opciones_por_menu(idmenu):
    """Muestra las opciones a realizar por cada usuario"""
    listado = operacion.opcion_fuera.get(idmenu)
    for valor in listado:
        for idx, dato in valor.items():
            print(idx,dato)

accion_formulario = {1:"Agregar", 2:"Modificar", 3:"Consultar",
                4: "Estado", 5:"Listar", 6:"Salir"}
def listado_opciones_formulario():
    """Muestra las opciones del formulario"""
    for idx, dato in accion_formulario.items():
        print(idx,dato)

def listado_estados_clientes():
    """Muestra las opciones de estado del cliente"""
    for idk, valor in operacion.opcion_estado_cliente.items():
        print(idk,valor)

def cantidad_opciones_por_menu(idmenu):
    """Cantidad de Opciones por Menú Principal"""
    listado = operacion.opcion_fuera.get(idmenu)
    cantidad:int
    for valor in listado:
        cantidad = len(valor)
    return cantidad

def cantidad_opciones_formulario():
    """Cantidad de las opciones de los formularios de operacioens"""
    return len(accion_formulario)
# OPCIONES SELECCIONADAS
def opcion_seleccionada_por_menu(idmenu, idoperacion):
    """Mustra la opción que se seleccionó por el menú"""
    listado = operacion.opcion_fuera.get(idmenu)
    for valor in listado:
        return valor.get(idoperacion)

def opcion_seleccionado_formulario(idaccion):
    """Muestra las opción que seleccionó para el formulario"""
    return accion_formulario.get(idaccion)
    