"""Transferencia ViewModel"""
# region Importación
import Api.service as service
import Model.transferencia as transferenciamodel
import ViewModel.dispensador_viewmodel as dispensadorviewmodel
import ViewModel.depositar_viewmodel as depositar_viewmodel
import ViewModel.cliente_viewmodel as clienteviewmodel
import ViewModel.retirar_viewmodel as retirarviewmodel
import ViewModel.cuenta_cliente_viewmodel as cuentaclienteviewmodel
#endregion

dispensador_vm = dispensadorviewmodel.DispensadorViewModel()
depositar_vm = depositar_viewmodel.DepositarViewModel()
client_vm = clienteviewmodel.ClienteViewModel()
retirar_vm = retirarviewmodel.RetirarViewModel()
cuentacliente_vm = cuentaclienteviewmodel.CuentaClienteViewModel()

class TransferenciaViewModel:
    """Clase Transferencia ViewModel"""
    def __init__(self) -> None:
        pass
    def registro_transferencia(self, disp:dict[str,any]):
        """Registro Transferencia"""
        transferencia = transferenciamodel.Transferencia(
                            codigo_transferencia=len(self.lista_transferencia())+1,
                            codigo_cliente=disp.get("codigo_cliente"),
                            codigo_dispensador=disp.get("codigo_dispensador"),
                            codigo_cliente_transferir=disp.get("codigo_cliente_transferir"),
                            codigo_dispensador_transferir=disp.get("codigo_dispensador_transferir"),
                            monto=disp.get("monto"))
        # Aumentar Saldo
        agregar_saldo_cta = cuentacliente_vm.modificar_saldo_cuenta_cliente(
                                disp.get("codigo_cliente_transferir"),
                                disp.get("codigo_dispensador_transferir"),
                                disp.get("monto"),1)
        # Reducir Saldo
        reducir_saldo_cta = cuentacliente_vm.modificar_saldo_cuenta_cliente(
                                disp.get("codigo_cliente"),
                                disp.get("codigo_dispensador"),
                                disp.get("monto"))

        if agregar_saldo_cta and reducir_saldo_cta:
            service.transferencia.append(transferencia)
        return agregar_saldo_cta and reducir_saldo_cta

    def lista_transferencia(self):
        """Lista de Transferencia"""
        return service.transferencia

    def lista_transferencia_codigo(self, codigo_cliente):
        """Lista de Transferencia por Código Cliente"""
        transferencia = []
        for dato in service.transferencia:
            if dato.codigo_cliente == codigo_cliente:
                transferencia.append(dato)
            if dato.codigo_cliente_transferir == codigo_cliente:
                transferencia.append(dato)
        return transferencia
