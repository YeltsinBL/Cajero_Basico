"""Depositar ViewModel"""
# region Importación
import Data.service as service
import Model.cuenta_cliente as cuentacliente
import ViewModel.dispensador_viewmodel as dispensadorviewmodel
from Data.conexion import conexion
#endregion

dispensador_vm = dispensadorviewmodel.DispensadorViewModel()

class CuentaClienteViewModel:
    """Clase Cuenta Cliente ViewModel"""
    def __init__(self) -> None:
        pass
    def registro_cuenta_cliente(self, disp:dict[str,any]):
        """Registro Cuenta Cliente"""
        nueva_cuenta=len(self.lista_cuenta_cliente())+1
        codigo_cuenta=str(nueva_cuenta).zfill(9)
        deposita = cuentacliente.CuentaCliente(
                                codigo_cuenta=codigo_cuenta,
                                codigo_cliente=disp.get("codigo_cliente"),
                                monto=disp.get("monto"), estado=0)
        service.cuenta_cliente.append(deposita)
        return codigo_cuenta

    def lista_cuenta_cliente(self):
        """Lista de la Cuenta Cliente"""
        try:
            connection= conexion()
            cursor = connection.cursor()
            cursor.execute("exec sp_ListaCuentaCliente")
            resultset= cursor.fetchall()
            connection.close()
            return resultset
        except ImportError as ex:
            print(ex)
            return []
        #return service.cuenta_cliente

    def modificar_cuenta_cliente(self, dicts:dict[str,any]):
        """Modificar la Cuenta Cliente"""
        for dato in service.cuenta_cliente:
            if dato.codigo_cliente == dicts.get("codigo_cliente") and\
                dato.codigo_cuenta == dicts.get("codigo_cuenta"):
                dato.monto=dicts["monto"]
                dato.estado=dicts["estado"]if dicts["estado"]==1 else dato.estado
                return True
        return False

    def modificar_saldo_cuenta_cliente(self, codigo_cliente, codigo_cuenta, monto,
                                     operacion =0, activar=0):
        """Aumentar o Reducir el saldo del cliente"""
        cta_cliente = self.buscar_cuenta_cliente_codcuenta_codcli(codigo_cliente,codigo_cuenta)
        for valor in cta_cliente:
            valor.monto = valor.monto + monto if operacion ==1 else valor.monto - monto
            nuevo_cta_cliente = {"codigo_cliente":valor.codigo_cliente,
                        "codigo_cuenta":valor.codigo_cuenta,
                        "monto":valor.monto, "estado":activar}
        return self.modificar_cuenta_cliente(nuevo_cta_cliente)

    def buscar_cuenta_cliente_codcuenta_codcli(self, codigo_cliente:str, codigo_cuenta = ""):
        """Buscar Cuenta Cliente por Código Cuenta y Código Cliente"""
        dispensa = []
        for dato in self.lista_cuenta_cliente():
            if dato.codigo_cliente == codigo_cliente and\
                codigo_cuenta in ["", dato.codigo_cuenta]:
                dispensa.append(dato)
        return dispensa
    # def verificar_cuenta_cliente(self, codigo_cliente, codigo_dispensador:int):
    #     """Verificar el Saldo de la Cuenta del Cliente"""
    #     lista_cuenta_cliente = self.lista_cuenta_cliente()
    #     monto_v=0.0
    #     for dato in lista_cuenta_cliente:
    #         if dato.codigo_dispensador == codigo_dispensador and\
    #             dato.codigo_cliente == codigo_cliente:
    #             monto_v= float(dato.monto)
    #     return monto_v
    # def buscar_cuenta_cliente(self, codigo_cliente, nro_cuenta):
    #     """Buscar la cuenta del Cliente"""
    #     lista_cuenta_cliente = self.lista_cuenta_cliente()
    #     for dato in lista_cuenta_cliente:
    #         if dato.nro_cuenta == nro_cuenta and\
    #             dato.codigo_cliente == codigo_cliente:
    #             pass
