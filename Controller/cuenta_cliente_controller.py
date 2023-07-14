"""Funciones que interactúan con los datos de la Cuenta del Cliente"""
import ViewModel.cuenta_cliente_viewmodel as cuentaclienteviewmodel

cta_cliente_vm = cuentaclienteviewmodel.CuentaClienteViewModel()

# region Funciones
def buscar_saldo_cuenta_cliente(codigo_cliente:str, cod_dispensador = 0):
    """Buscar el saldo de la Cuenta del Cliente"""
    return cta_cliente_vm.buscar_cuenta_cliente_coddisp_codcli(codigo_cliente, cod_dispensador)
def verificar_cuenta_cliente(codigo_cliente, codigo_dispensador:int):
    """Verificar Monto de la Cuenta del Cliente"""
    return cta_cliente_vm.verificar_cuenta_cliente(codigo_cliente, codigo_dispensador)
# endregion
