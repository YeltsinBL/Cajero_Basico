"""Transferencia ViewModel"""
# region Importación
import Api.service as service
import Model.transferencia as transferenciamodel
import ViewModel.dispensador_viewmodel as dispensadorviewmodel
import ViewModel.depositar_viewmodel as depositar_viewmodel
import ViewModel.cliente_viewmodel as clienteviewmodel
import ViewModel.retirar_viewmodel as retirarviewmodel
#endregion

dispensador_vm = dispensadorviewmodel.DispensadorViewModel()
depositar_vm = depositar_viewmodel.DepositarViewModel()
client_vm = clienteviewmodel.ClienteViewModel()
retirar_vm = retirarviewmodel.RetirarViewModel()

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
        #respt_cliente = client_vm.buscar_cliente_codigo(disp.get("codigo_cliente_transferir"))
        respt_dispensador = dispensador_vm.\
                        buscar_dispensador_codigo(int(disp.get("codigo_dispensador_transferir")))
        # AGREGAR BILLETES AL Deposito
        billetes_transferencia = self.obtener_billetes_depositar(
                                                int(disp.get("codigo_dispensador_transferir")),
                                                disp.get("monto"))
        respt = depositar_vm.agregar_billete_dispensador(
                                int(disp.get("codigo_dispensador_transferir")),
                                respt_dispensador.lugar, respt_dispensador.estado,
                                billetes_transferencia)
        respt_disp_reducir = retirar_vm.modificar_billetes_dispensador(
                                disp.get("codigo_dispensador"),
                                respt_dispensador.lugar,
                                respt_dispensador.estado,
                                disp.get("monto"))
        respt_deposito = retirar_vm.modificar_billetes_deposito(
                                disp.get("codigo_cliente"),
                                disp.get("codigo_dispensador"),
                                disp.get("monto"))

        if respt and len(respt_disp_reducir)>0 and respt_deposito:
            service.transferencia.append(transferencia)
        return respt

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

    def obtener_billetes_depositar(self, codigo_dispensador:str, monto):
        """Modificar los billetes del depósito"""
        billete_entregar=[]
        lista_billete_entregar={}
        respt_dispensador = dispensador_vm.buscar_dispensador_codigo(codigo_dispensador)
        for valor in respt_dispensador.billete:
            for nro_billete, vbillete in valor.items():
                lista_billete_entregar[nro_billete] = 0
                # Contar cuantos billetes a entregar y queda
                while monto > 0:
                    cantidad_billete=0
                    while monto >= nro_billete and vbillete >0:
                        cantidad_billete+=1
                        monto -= nro_billete
                        vbillete -= 1
                    if cantidad_billete>0:
                        # Billetes a entregar
                        lista_billete_entregar[nro_billete] = cantidad_billete
                    break
        billete_entregar.append(lista_billete_entregar)
        return billete_entregar
 