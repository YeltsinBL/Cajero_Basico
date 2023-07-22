"""Retirar ViewModel"""
# region Importación
# import Data.service as service
# import Model.retirar as retirar
import ViewModel.dispensador_viewmodel as dispensadorviewmodel
import ViewModel.depositar_viewmodel as depositarviewmodel
import ViewModel.cuenta_cliente_viewmodel as cuentaclienteviewmodel
from Data.conexion import conexion
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
        # retiro = retirar.Retirar(datos_retiro.get("codigo_cliente"),
        #                          datos_retiro.get("codigo_dispensador"),
        #                          datos_retiro.get("monto"))
        # respt = self.calcular_billetes_dispensador(datos_retiro.get("codigo_dispensador"),
        #                      datos_retiro.get("lugar_dispensador"),
        #                      datos_retiro.get("estado_dispensador"),
        #                      datos_retiro.get("monto"))
        # if isinstance(respt, list) and len(respt)>0:
        #     respt_ctacliente = cuentacliente_vm.modificar_saldo_cuenta_cliente(
        #                             datos_retiro.get("codigo_cliente"),
        #                             datos_retiro.get("codigo_cuenta"),
        #                             datos_retiro.get("monto"))
        #     if respt_ctacliente:
        #         service.retiros.append(retiro)
        # return respt
        try:
            respt = self.calcular_billetes_dispensador(datos_retiro.get("codigo_dispensador"),
                                 datos_retiro.get("lugar_dispensador"),
                                 datos_retiro.get("estado_dispensador"),
                                 datos_retiro.get("monto"))
            if isinstance(respt, list) and len(respt)>0:
                respt_ctacliente = cuentacliente_vm.modificar_saldo_cuenta_cliente(
                                        datos_retiro.get("codigo_cliente"),
                                        datos_retiro.get("codigo_cuenta"),
                                        datos_retiro.get("monto"))
                if respt_ctacliente:
                    connection= conexion()
                    cursor = connection.cursor()
                    store_proc = "exec sp_Registrar_Retiro @strCodigoCliente = ?,\
                            @strCodigoDispensador=?, @dcmMonto = ?"
                    params = (datos_retiro.get("codigo_cliente"),
                              datos_retiro.get("codigo_dispensador"),
                              datos_retiro.get("monto"))
                    cursor.execute(store_proc, params)
                    cursor.commit()
                    cursor.close()

                    #service.retiros.append(retiro)
                    return respt
            return respt
        except ImportError as ex:
            print(ex)
            return []

    def calcular_billetes_dispensador(self, cod_dispensador:int, lugar_dispensador:str,
                               estado_dispensador:str, monto):
        """Calcular los Billetes que se moodificarán en el Dispensador"""
        billete_entregar=[]
        lista_billete_entregar={}
        billete_actualizar_dispensador=[]
        billete_falta =""
        respt_dispensador = dispensador_vm.buscar_dispensador_codigo(cod_dispensador)
        for data in respt_dispensador:
            for valor in data.get("billete"):
                for nro_billete, vbillete in valor.items():
                    # Contar cuantos billetes a entregar y queda
                    if monto >= nro_billete and\
                        (vbillete ==0 or monto > (nro_billete * vbillete)):
                        billete_falta += str(nro_billete) + " - "
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
                    # Billetes queda
                    billete_actualizar_dispensador.append({nro_billete:vbillete})
        billete_entregar.append(lista_billete_entregar)
        if monto ==0:
            disp={"codigo":cod_dispensador,"lugar":lugar_dispensador,
                "estado":estado_dispensador, "billete": billete_actualizar_dispensador}
            respt = dispensador_vm.modificar_dispensador(disp)
            if respt:
                return billete_entregar
            return []
        return billete_falta

    def buscar_retiro(self, codigo_cliente:str):
        """Buscar Retiro por Código"""
        # retiro = []
        # for dato in service.retiros:
        #     if dato.codigo_cliente == codigo_cliente:
        #         retiro.append(dato)
        # return retiro
        try:
            retiro = []
            connection= conexion()
            cursor = connection.cursor()
            store_proc = "exec sp_Listar_Retiro @strCodigoCliente=?"
            parametro = codigo_cliente
            cursor.execute(store_proc, parametro)
            resultset= cursor.fetchall()
            for resultado in resultset:
                retiro.append({"codigo_cliente":resultado[1],
                                "codigo_dispensador":resultado[2],
                                "monto": resultado[3]})
            connection.close()
            return retiro
        except ImportError as ex:
            print(ex)
            return []
