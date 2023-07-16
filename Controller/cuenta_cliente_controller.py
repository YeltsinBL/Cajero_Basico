"""Funciones que interactúan con los datos de la Cuenta del Cliente"""
import ViewModel.cuenta_cliente_viewmodel as cuentaclienteviewmodel

cta_cliente_vm = cuentaclienteviewmodel.CuentaClienteViewModel()

# region Funciones
def buscar_saldo_cuenta_cliente(codigo_cliente:str, codigo_cuenta = 0):
    """Buscar el saldo de la Cuenta del Cliente"""
    return cta_cliente_vm.buscar_cuenta_cliente_coddisp_codcli(codigo_cliente, codigo_cuenta)
def buscar_cuenta_cliente(codigo_cliente, nro_cuenta):
    """Buscar la cuenta del cliente"""
    return cta_cliente_vm.buscar_cuenta_cliente(codigo_cliente, nro_cuenta)
# endregion
