"""Depositar ViewModel"""
# region Importación
import Data.service as service
import Model.depositar as depositar
import ViewModel.dispensador_viewmodel as dispensadorviewmodel
import ViewModel.cuenta_cliente_viewmodel as cuentaclienteviewmodel
#endregion

dispensador_vm = dispensadorviewmodel.DispensadorViewModel()
cuentacliente_vm = cuentaclienteviewmodel.CuentaClienteViewModel()

class DepositarViewModel:
    """Clase Depositar ViewModel"""
    def __init__(self) -> None:
        pass
    def registro_deposito(self, disp:dict[str,any]):
        """Registro Depósito"""
        deposita = depositar.Depositar(codigo_deposito=len(self.lista_deposito())+1,
                                       codigo_cliente=disp.get("codigo_cliente"),
                                       codigo_dispensador=disp.get("codigo_dispensador"),
                                       monto=disp.get("monto"))
        # AGREGAR BILLETES AL DISPENSADOR
        respt = dispensador_vm.agregar_billete_dispensador(disp.get("codigo_dispensador"),
                             disp.get("lugar_dispensador"),
                             disp.get("estado_dispensador"),
                             disp.get("billete"))
        if respt:
            service.depositos.append(deposita)
            cuentacliente_vm.modificar_saldo_cuenta_cliente(
                codigo_cliente=disp.get("codigo_cliente"),
                codigo_cuenta=disp.get("codigo_cuenta"),
                monto=disp.get("monto"), operacion=1, activar=1
            )
        return respt

    def lista_deposito(self):
        """Lista de Depósito"""
        return service.depositos

    def buscar_deposito(self, codigo_cliente:str, cod_dispensador:int):
        """Buscar depósito por Código"""
        dispensa = []
        for dato in service.depositos:
            if dato.codigo_cliente == codigo_cliente and\
                (cod_dispensador == 0 or dato.codigo_dispensador == cod_dispensador):
                dispensa.append(dato)
        return dispensa
