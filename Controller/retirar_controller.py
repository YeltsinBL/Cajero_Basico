"""Funciones que interactúan con los datos de Retiro """

# region Importación
import ViewModel.retirar_viewmodel as retirarviewmodel
#endregion

retirar_vm = retirarviewmodel.RetirarViewModel()

# region Funciones
def registro_retiro(datos_depositar:dict[str,any]):
    """Registro Retiro"""
    return retirar_vm.registro_retiro(datos_depositar)

# endregion
