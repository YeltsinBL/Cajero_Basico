"""Funciones que interactúan con los datos de Transferencia """

# region Importación
import ViewModel.transferencia_viewmodel as transferenciaviewmodel
#endregion

transferencia_vm = transferenciaviewmodel.TransferenciaViewModel()

# region Funciones
def registro_transferencia(datos_depositar:dict[str,any]):
    """Registro Transferencia"""
    return transferencia_vm.registro_transferencia(datos_depositar)
def buscar_transferencia_codigo(codigo_cliente:str):
    """Buscar Transferencia por código"""
    return transferencia_vm.lista_transferencia_codigo(codigo_cliente)
# endregion
