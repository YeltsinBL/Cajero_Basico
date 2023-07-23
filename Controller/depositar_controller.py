"""Funciones que interactúan con los datos de Depositar """

# region Importación
import ViewModel.depositar_viewmodel as depositarviewmodel
#endregion

depositar_vm = depositarviewmodel.DepositarViewModel()

# region Funciones
def registro_deposito(datos_depositar:dict[str,any]):
    """Registro Depósito"""
    return depositar_vm.registro_deposito(datos_depositar)
def buscar_deposito_codigo(codigo_cliente:str):
    """Buscar Dispensador por código"""
    return depositar_vm.buscar_deposito(codigo_cliente)
# endregion
