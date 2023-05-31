"""Funciones que interactúan con los datos del Dispensador """

# region Importación
import ViewModel.dispensador_viewmodel as dispensadorviewmodel
#endregion

dispensador_vm = dispensadorviewmodel.DispensadorViewModel()

# region Funciones
def registro_dispensador(datos_dispensador:dict[str,any]):
    """Registro Dispensador"""
    dispensador_vm.registrar_dispensador(datos_dispensador)

def listado_dispensador():
    """Verificar si hay Dispensadores"""
    return dispensador_vm.lista_dispensadores()

def verifica_dispensador_codigo(codigo:int):
    """Verifica Dispensador por Código"""
    return dispensador_vm.verifica_dispensador_codigo(codigo)

def modificar_dispensador(datos_dispensador:dict[str,any]):
    """Modificar Dispensador"""
    return dispensador_vm.modificar_dispensador(datos_dispensador)

def buscar_dispensador_codigo(codigo:int):
    """Buscar Dispensador por código"""
    return dispensador_vm.buscar_dispensador_codigo(codigo)

def listado_dispensador_estado(estado:str):
    """Listar los Dispensadores por su estado"""
    return dispensador_vm.lista_dispensador_estado(estado)
# endregion
