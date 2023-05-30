"""Funciones que interactúan con los datos del Cliente"""
import ViewModel.cliente_viewmodel as clienteviewmodel

clientevm = clienteviewmodel.ClienteViewModel()

# region Funciones
def registro_cliente(datos_cliente:dict[str,any]):
    """Registro Cliente"""
    clientevm.registrar_cliente(datos_cliente)
def listado_cliente():
    """Verificar si hay existen Clientes"""
    return clientevm.lista_cliente()
def verifica_cliente_codigo(codigo):
    """Verifica Cliente por Código"""
    return clientevm.verifica_cliente_codigo(codigo)
def modificar_cliente(datos_cliente:dict[str,any]):
    """Modificar Cliente"""
    return clientevm.modificar_cliente(datos_cliente)
def buscar_cliente_codigo(codigo):
    """Buscar Cliente por código"""
    return clientevm.buscar_cliente_codigo(codigo)
def listado_cliente_estado(estado):
    """Listar los Clientes por su estado"""
    return clientevm.lista_cliente_estado(estado)
# endregion
