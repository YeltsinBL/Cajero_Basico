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

    # def calcular_billetes_restantes_cuenta_cliente(self, codigo_cliente:int,
    #                            codigo_dispensador:str, monto):
    #     """Calcular los billetes que quedan en la Cuenta del cliente al Retirar y/o transferir"""
    #     billete_actualizar_dispensador=[]
    #     lista_billete_restante={}
    #     cuenta_cliente = self.lista_cuenta_cliente()
    #     for dato in cuenta_cliente:
    #         if dato.codigo_cliente == codigo_cliente and\
    #             dato.codigo_dispensador == codigo_dispensador:
    #             for valor in dato.billete:
    #                 for nro_billete, vbillete in valor.items():
    #                     lista_billete_restante[nro_billete] = vbillete
    #                     # Contar cuantos billetes quedan
    #                     while monto > 0:
    #                         cantidad_billete=0
    #                         while monto >= nro_billete and vbillete >0:
    #                             cantidad_billete+=1
    #                             monto -= nro_billete
    #                             vbillete -= 1
    #                         if cantidad_billete>0:
    #                             # Billetes queda
    #                             lista_billete_restante[nro_billete] = vbillete
    #                         break
    #     billete_actualizar_dispensador.append(lista_billete_restante)

    #     disp = {"codigo_cliente":codigo_cliente, "codigo_dispensador":codigo_dispensador,
    #             "billete":billete_actualizar_dispensador}
    #     return self.modificar_cuenta_cliente(disp)

    # def calcular_billete_agregar_cuenta_cliente(self, codigo_cliente:int,
    #                            codigo_dispensador:str, monto):
    #     """Calcular los billetes que se agregan en la Cuenta del cliente al Depositar"""
    #     nueva_lista=[]
    #     # Lista guardada del Dispensador
    #     respt_dispensador = self.buscar_cuenta_cliente_coddisp_codcli(
    #                                 codigo_dispensador, codigo_cliente)
    #     # for valor in respt_dispensador:
    #     #     if valor.codigo_cliente == codigo_cliente and\
    #     #         valor.codigo_dispensador == codigo_dispensador:
    #     #         for val in valor.billete:
    #     #             for nro_billete, vbillete in val.items():
    #     #                 # Lista de los nuevos valores de billetes para el Dispensdaor
    #     #                 for val_billete in billete:
    #     #                     for nro_billete2, vbillete2 in val_billete.items():
    #     #                         # Comparación de las claves de las listas para sumar sus valores
    #     #                         if nro_billete == nro_billete2:
    #     #                             nueva_lista.append({nro_billete: vbillete+vbillete2})
    #     #                             break
    #     disp = {"codigo_cliente":codigo_cliente, "codigo_dispensador":codigo_dispensador,
    #             "billete":nueva_lista}
    #     return self.modificar_cuenta_cliente(disp)

    def buscar_cuenta_cliente_coddisp_codcli(self, codigo_cliente:str, cod_dispensador:int):
        """Buscar Cuenta Cliente por Código Dispensdor y Código Cliente"""
        dispensa = []
        for dato in service.cuenta_cliente:
            if dato.codigo_cliente == codigo_cliente and\
                (cod_dispensador == 0 or dato.codigo_dispensador == cod_dispensador):
                dispensa.append(dato)
        return dispensa
