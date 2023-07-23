"""Depositar ViewModel"""
# region Importación
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
        try:
            connection= conexion()
            cursor = connection.cursor()
            store_proc = "exec sp_CrearCuentaCliente @strNumeroCuentaCliente = ?,\
                            @strCodigoCliente = ?, @dcmMonto = ?"
            params = (codigo_cuenta, disp.get("codigo_cliente"), disp.get("monto"))
            cursor.execute(store_proc, params)
            cursor.commit()
            cursor.close()
        except ImportError as ex:
            print(ex)
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
        try:
            connection= conexion()
            cursor = connection.cursor()
            store_proc = "exec sp_ModificarCuentaCliente @strNumeroCuentaCliente = ?,\
                            @strCodigoCliente = ?, @dcmMonto = ?"
            params = (dicts.get("codigo_cuenta"), dicts.get("codigo_cliente"),
                      dicts.get("monto"))
            cursor.execute(store_proc, params)
            cursor.commit()
            cursor.close()
            return True
        except ImportError as ex:
            print(ex)
            return False

    def modificar_saldo_cuenta_cliente(self, codigo_cliente, codigo_cuenta, monto,
                                     operacion =0):
        """Aumentar o Reducir el saldo del cliente"""
        cta_cliente = self.buscar_cuenta_cliente_codcuenta_codcli(codigo_cliente,codigo_cuenta)
        for valor in cta_cliente:
            calculado = float(valor[3]) + monto if operacion ==1 else float(valor[3]) - monto
            nuevo_cta_cliente = {"codigo_cliente":valor[2], "codigo_cuenta":valor[1],
                        "monto":calculado}
        return self.modificar_cuenta_cliente(nuevo_cta_cliente)

    def buscar_cuenta_cliente_codcuenta_codcli(self, codigo_cliente:str, codigo_cuenta = ""):
        """Buscar Cuenta Cliente por Código Cuenta y Código Cliente"""
        try:
            connection= conexion()
            cursor = connection.cursor()
            store_proc = "exec sp_ListaCuentaCliente @strNumeroCuentaCliente = ?,\
                            @strCodigoCliente = ?"
            params = (codigo_cuenta, codigo_cliente)
            cursor.execute(store_proc, params)
            resultset= cursor.fetchall()
            connection.close()
            return resultset
        except ImportError as ex:
            print(ex)
            return []
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
