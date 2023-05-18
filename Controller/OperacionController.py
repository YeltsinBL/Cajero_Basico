import Model.Operacion as operacion

# lISTADO DE LAS OPCIONES
def listado_opciones_por_menu(idmenu):
    """Mustra las opciones a realizar por cada cliente"""
    listado = operacion.opcion_fuera.get(idmenu)
    for valor in listado:
        for idx, dato in valor.items():
            print(idx,dato)

accion_formulario = {1:"Agregar", 2:"Modificar", 3:"Consultar",
                4: "Estado", 5:"Listar", 6:"Salir"}
def listado_opciones_formulario():
    """Mustra las opciones del formulario"""
    for idx, dato in accion_formulario.items():
        print(idx,dato)
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
    