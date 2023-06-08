"""Depositar ViewModel"""
# region Importación
import Api.service as service
import Model.cuenta_cliente as cuentacliente
import ViewModel.dispensador_viewmodel as dispensadorviewmodel
#endregion

dispensador_vm = dispensadorviewmodel.DispensadorViewModel()

class CuentaClienteViewModel:
    """Clase Cuenta Cliente ViewModel"""
    def __init__(self) -> None:
        pass
    def registro_cuenta_cliente(self, disp:dict[str,any]):
        """Registro Cuenta Cliente"""
        #respt_dispensador = self.buscar_cuenta_cliente_coddisp_codcli(
            #disp.codigo_dispensador, disp.codigo_cliente)
        #if len(respt_dispensador)>0:
            # deposita = self.calcular_billete_agregar_cuenta_cliente(
            #                     codigo_cliente=disp.codigo_cliente,
            #                     codigo_dispensador=disp.codigo_dispensador,
            #                     monto=disp.monto)

        #else:
        deposita = cuentacliente.CuentaCliente(
                                codigo_cuenta=len(self.lista_cuenta_cliente())+1,
                                codigo_cliente=disp.codigo_cliente,
                                codigo_dispensador=disp.codigo_dispensador,
                                monto=disp.monto)
        service.cuenta_cliente.append(deposita)

    def lista_cuenta_cliente(self):
        """Lista de Depósito"""
        return service.cuenta_cliente

    def modificar_cuenta_cliente(self, dicts:dict[str,any]):
        """Modificar la Cuenta Cliente"""
        for dato in service.cuenta_cliente:
            if dato.codigo_cliente == dicts.get("codigo_cliente") and\
                dato.codigo_dispensador == dicts.get("codigo_dispensador"):
                dato.monto=dicts["monto"]
                return True
        return False

    def modificar_saldo_cuenta_cliente(self, codigo_cliente, codigo_dispensador, monto,
                                     operacion =0):
        """Reducir el saldo del cliente"""
        cta_cliente = self.buscar_cuenta_cliente_coddisp_codcli(codigo_cliente,codigo_dispensador)
        for valor in cta_cliente:
            valor.monto = valor.monto + monto if operacion ==1 else valor.monto - monto
            nuevo_cta_cliente = {"codigo_cliente":valor.codigo_cliente,
                        "codigo_dispensador":valor.codigo_dispensador,
                        "monto":valor.monto}
        return self.modificar_cuenta_cliente(nuevo_cta_cliente)

    def buscar_cuenta_cliente_coddisp_codcli(self, codigo_cliente:str, cod_dispensador = 0):
        """Buscar Cuenta Cliente por Código Dispensdor y Código Cliente"""
        dispensa = []
        for dato in service.cuenta_cliente:
            if dato.codigo_cliente == codigo_cliente and\
                (cod_dispensador == 0 or dato.codigo_dispensador == cod_dispensador):
                dispensa.append(dato)
        return dispensa
