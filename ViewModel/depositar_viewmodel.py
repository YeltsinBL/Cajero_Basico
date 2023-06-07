"""Depositar ViewModel"""
# region Importación
import Api.service as service
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
        return respt

    def agregar_billete_dispensador(self, cod_dispensador:int, lugar_dispensador:str,
                        estado_dispensador:str, billete:list):
        """Agregar billetes al dispensador"""
        nueva_lista=[]
        # Lista guardada del Dispensador
        respt_dispensador = dispensador_vm.buscar_dispensador_codigo(cod_dispensador)
        for valor in respt_dispensador.billete:
            for nro_billete, vbillete in valor.items():
                # Lista de los nuevos valores de billetes para el Dispensdaor
                for val_billete in billete:
                    for nro_billete2, vbillete2 in val_billete.items():
                        # Comparación de las claves de las listas para sumar sus valores
                        if nro_billete == nro_billete2:
                            nueva_lista.append({nro_billete: vbillete+vbillete2})
                            break
        disp={"codigo":cod_dispensador,"lugar":lugar_dispensador,
              "estado":estado_dispensador, "billete": nueva_lista}
        return dispensador_vm.modificar_dispensador(disp)

    def lista_deposito(self):
        """Lista de Depósito"""
        return service.depositos

    def modificar_deposito(self, dicts:dict[str,any]):
        """Modificar el depósito"""
        for dato in service.depositos:
            if dato.codigo_cliente == dicts.get("codigo_cliente") and\
                dato.codigo_dispensador == dicts.get("codigo_dispensador"):
                dato.billete=dicts["billete"]
                return True
        return False

    def buscar_deposito(self, codigo_cliente:str, cod_dispensador:int):
        """Buscar depósito por Código"""
        dispensa = []
        for dato in service.depositos:
            if dato.codigo_cliente == codigo_cliente and\
                (cod_dispensador == 0 or dato.codigo_dispensador == cod_dispensador):
                dispensa.append(dato)
                #return dispensa
        return dispensa
