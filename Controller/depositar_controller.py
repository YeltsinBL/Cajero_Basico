"""Funciones que interactúan con los datos de Depositar """

# region Importación
import ViewModel.depositar_viewmodel as depositarviewmodel
#endregion

depositar_vm = depositarviewmodel.DepositarViewModel()

# region Funciones
def registro_deposito(datos_depositar:dict[str,any]):
    """Registro Depósito"""
    return depositar_vm.registro_deposito(datos_depositar)
# endregion
