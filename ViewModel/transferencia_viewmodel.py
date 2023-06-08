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
        nuevo_cta_cliente:dict[str,any]
        # Aumentar Saldo
        cta_cliente = cuentacliente_vm.buscar_cuenta_cliente_coddisp_codcli(
                                disp.get("codigo_cliente_transferir"),
                                disp.get("codigo_dispensador_transferir"))
        for valor in cta_cliente:
            valor.monto += disp.get("monto")
            nuevo_cta_cliente = {"codigo_cliente":valor.codigo_cliente,
                        "codigo_dispensador":valor.codigo_dispensador,
                        "monto":valor.monto}
        agregar_saldo_cta = cuentacliente_vm.modificar_cuenta_cliente(nuevo_cta_cliente)
        # Reducir Saldo
        cta_cliente = cuentacliente_vm.buscar_cuenta_cliente_coddisp_codcli(
                                disp.get("codigo_cliente"),
                                disp.get("codigo_dispensador"))
        for valor in cta_cliente:
            valor.monto -= disp.get("monto")
            nuevo_cta_cliente = {"codigo_cliente":valor.codigo_cliente,
                        "codigo_dispensador":valor.codigo_dispensador,
                        "monto":valor.monto}
        reducir_saldo_cta = cuentacliente_vm.modificar_cuenta_cliente(nuevo_cta_cliente)

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
        return transferencia

    # def obtener_billetes_transferir(self, codigo_dispensador:str, monto):
    #     """Obtener los billetes que se van a transferir al Dispensador"""
    #     billete_entregar=[]
    #     lista_billete_entregar={}
    #     respt_dispensador = dispensador_vm.buscar_dispensador_codigo(codigo_dispensador)
    #     for valor in respt_dispensador.billete:
    #         for nro_billete, vbillete in valor.items():
    #             lista_billete_entregar[nro_billete] = 0
    #             # Contar cuantos billetes a entregar y queda
    #             while monto > 0:
    #                 cantidad_billete=0
    #                 while monto >= nro_billete and vbillete >0:
    #                     cantidad_billete+=1
    #                     monto -= nro_billete
    #                     vbillete -= 1
    #                 if cantidad_billete>0:
    #                     # Billetes a entregar
    #                     lista_billete_entregar[nro_billete] = cantidad_billete
    #                 break
    #     billete_entregar.append(lista_billete_entregar)
    #     return billete_entregar
 