"""Retirar ViewModel"""
# region Importación
import Api.service as service
import Model.retirar as retirar
import ViewModel.dispensador_viewmodel as dispensadorviewmodel
import ViewModel.depositar_viewmodel as depositarviewmodel
import ViewModel.cuenta_cliente_viewmodel as cuentaclienteviewmodel
#endregion

dispensador_vm = dispensadorviewmodel.DispensadorViewModel()
depositar_vm = depositarviewmodel.DepositarViewModel()
cuentacliente_vm = cuentaclienteviewmodel.CuentaClienteViewModel()

class RetirarViewModel:
    """Clase Retirar ViewModel"""
    def __init__(self) -> None:
        pass
    def registro_retiro(self,datos_retiro:dict[str,any]):
        """Registrar Retiro"""
        retiro = retirar.Retirar(datos_retiro.get("codigo_cliente"),
                                 datos_retiro.get("codigo_dispensador"),
                                 datos_retiro.get("monto"))
        respt = self.modificar_billetes_dispensador(datos_retiro.get("codigo_dispensador"),
                             datos_retiro.get("lugar_dispensador"),
                             datos_retiro.get("estado_dispensador"),
                             datos_retiro.get("monto"))
        respt_ctacliente = cuentacliente_vm.modificar_saldo_cuenta_cliente(
                                datos_retiro.get("codigo_cliente"),
                                datos_retiro.get("codigo_dispensador"),
                                datos_retiro.get("monto"))
        if len(respt)>0 and respt_ctacliente:
            service.retiros.append(retiro)
        return respt

    def modificar_billetes_dispensador(self, cod_dispensador:int, lugar_dispensador:str,
                               estado_dispensador:str, monto):
        """Modificar los Billetes del Dispensador"""
        billete_entregar=[]
        lista_billete_entregar={}
        billete_actualizar_dispensador=[]
        lista_billete_restante={}
        respt_dispensador = dispensador_vm.buscar_dispensador_codigo(cod_dispensador)
        for valor in respt_dispensador.billete:
            for nro_billete, vbillete in valor.items():
                lista_billete_restante[nro_billete] = vbillete
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
                        # Billetes queda
                        lista_billete_restante[nro_billete] = vbillete
                    break
        billete_entregar.append(lista_billete_entregar)
        billete_actualizar_dispensador.append(lista_billete_restante)
        disp={"codigo":cod_dispensador,"lugar":lugar_dispensador,
              "estado":estado_dispensador, "billete": billete_actualizar_dispensador}
        respt = dispensador_vm.modificar_dispensador(disp)
        if respt:
            return billete_entregar
        return []
    # actualizar la verificación del monto a retirar

    def buscar_retiro(self, codigo_cliente:str):
        """Buscar Retiro por Código"""
        retiro = []
        for dato in service.retiros:
            if dato.codigo_cliente == codigo_cliente:
                retiro.append(dato)
        return retiro
