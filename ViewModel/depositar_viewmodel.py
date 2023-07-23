"""Depositar ViewModel"""
# region Importación
import ViewModel.dispensador_viewmodel as dispensadorviewmodel
import ViewModel.cuenta_cliente_viewmodel as cuentaclienteviewmodel
from Data.conexion import conexion
#endregion

dispensador_vm = dispensadorviewmodel.DispensadorViewModel()
cuentacliente_vm = cuentaclienteviewmodel.CuentaClienteViewModel()

class DepositarViewModel:
    """Clase Depositar ViewModel"""
    def __init__(self) -> None:
        pass
    def registro_deposito(self, disp:dict[str,any]):
        """Registro Depósito"""
        try:
            codigo_deposito=len(self.lista_deposito())+1
            connection= conexion()
            cursor = connection.cursor()
            store_proc = "exec sp_RegistrarDeposito @strCodigoDeposito = ?,\
                            @strCodigoCliente = ?, @strCodigoDispensador=?,\
                            @dcmMonto = ?"
            params = (codigo_deposito, disp.get("codigo_cliente"), disp.get("codigo_dispensador"),
                      disp.get("monto"))
            cursor.execute(store_proc, params)
            cursor.commit()
            cursor.close()
            # AGREGAR BILLETES AL DISPENSADOR
            respt = dispensador_vm.agregar_billete_dispensador(disp.get("codigo_dispensador"),
                                disp.get("lugar_dispensador"),
                                disp.get("estado_dispensador"),
                                disp.get("billete"))
            if respt:
                return cuentacliente_vm.modificar_saldo_cuenta_cliente(
                    codigo_cliente=disp.get("codigo_cliente"),
                    codigo_cuenta=disp.get("codigo_cuenta"),
                    monto=disp.get("monto"), operacion=1)
            return respt
        except ImportError as ex:
            print(ex)
            return False

    def lista_deposito(self):
        """Lista de Depósito"""
        lista_dispensador = []
        try:
            connection= conexion()
            cursor = connection.cursor()
            cursor.execute("exec sp_Lista_Dispensador")
            resultset= cursor.fetchall()
            for resultado in resultset:
                lista_dispensador.append({"codigo_deposito":resultado[1],
                                          "codigo_cliente":resultado[2],
                                          "codigo_dispensador": resultado[3],
                                          "monto": resultado[4]})
            connection.close()
        except ImportError as ex:
            print(ex)
        return  lista_dispensador

    def buscar_deposito(self, codigo_cliente:str):
        """Buscar depósito por Código"""
        lista_dispensador = []
        try:
            connection= conexion()
            cursor = connection.cursor()
            store_proc = "exec sp_Listar_Deposito_Cliente_Dispensador @strCodigoCliente = ?"
            params = codigo_cliente
            cursor.execute(store_proc, params)
            resultset= cursor.fetchall()
            for resultado in resultset:
                lista_dispensador.append({"codigo_deposito":resultado[1],
                                          "codigo_cliente":resultado[2],
                                          "codigo_dispensador": resultado[3],
                                          "monto": resultado[4],
                                          "nombre_persona":resultado[5],
                                          "numero_cuenta":resultado[6],
                                          "dispensador_lugar":resultado[7]})
            connection.close()
        except ImportError as ex:
            print(ex)
        return  lista_dispensador
