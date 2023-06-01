"""Retirar ViewModel"""
# region Importación
import Api.service as service
import Model.retirar as retirar
import ViewModel.dispensador_viewmodel as dispensadorviewmodel
#endregion

dispensador_vm = dispensadorviewmodel.DispensadorViewModel()

class RetirarViewModel:
    """Clase Retirar ViewModel"""
    def __init__(self) -> None:
        pass
    def registro_retiro(self,datos_retiro:dict[str,any]):
        """Registrar Retiro"""
        retiro = retirar.Retirar(datos_retiro.get("codigo_cliente"),
                                 datos_retiro.get("codigo_dispensador"),
                                 datos_retiro.get("monto"))
        respt = self.actualizar_billetes_dispensador(datos_retiro.get("codigo_dispensador"),
                             datos_retiro.get("lugar_dispensador"),
                             datos_retiro.get("estado_dispensador"),
                             datos_retiro.get("monto"))
        if len(respt)>0:
            service.retiros.append(retiro)
        return respt
    def actualizar_billetes_dispensador(self, cod_dispensador:int, lugar_dispensador:str,
                               estado_dispensador:str, monto):
        """Actualizar los Billetes del Dispensador"""
        nueva_lista=[]
        nueva_lista_billete={}
        nueva_lista2=[]
        nueva_lista_billete2={}
        respt_dispensador = dispensador_vm.buscar_dispensador_codigo(cod_dispensador)
        for valor in respt_dispensador.billete:
            for nro_billete, vbillete in valor.items():
                nueva_lista_billete2[nro_billete] = vbillete
                # Contar cuantos billetes a entregar
                while monto > 0:
                    cantidad_billete=0
                    while monto >= nro_billete and vbillete >0:
                        cantidad_billete+=1
                        monto -= nro_billete
                        vbillete -= 1
                    if cantidad_billete>0:
                        # Billetes a entregar
                        nueva_lista_billete[nro_billete] = cantidad_billete
                        # Billetes queda
                        nueva_lista_billete2[nro_billete] = vbillete
                    break
        nueva_lista.append(nueva_lista_billete)
        nueva_lista2.append(nueva_lista_billete2)
        print("Lista entregar",nueva_lista)
        print("Lista restante",nueva_lista2)
        disp={"codigo":cod_dispensador,"lugar":lugar_dispensador,
              "estado":estado_dispensador, "billete": nueva_lista2}
        respt = dispensador_vm.modificar_dispensador(disp)
        if respt:
            return nueva_lista
        return []
    # actualizar la verificación del monto a retirar
    # agregar el retiro al depósito, sólo está agregado al dispensador
