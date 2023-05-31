"""Funciones que interactúan con los datos de Depositar """

# region Importación
import ViewModel.depositar_viewmodel as depositarviewmodel
#endregion

dispensador_vm = depositarviewmodel.DepositarViewModel()

# region Funciones
def registro_deposito(datos_dispensador:dict[str,any]):
    """Registro Depósito"""
    return dispensador_vm.registro_deposito(datos_dispensador)
# endregion
