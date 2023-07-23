"""Transferencia ViewModel"""
# region Importación
import ViewModel.dispensador_viewmodel as dispensadorviewmodel
import ViewModel.depositar_viewmodel as depositar_viewmodel
import ViewModel.cliente_viewmodel as clienteviewmodel
import ViewModel.retirar_viewmodel as retirarviewmodel
import ViewModel.cuenta_cliente_viewmodel as cuentaclienteviewmodel
from Data.conexion import conexion
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
        try:
            # Reducir Saldo
            reducir_saldo_cta = cuentacliente_vm.modificar_saldo_cuenta_cliente(
                                    disp.get("codigo_cliente"),
                                    disp.get("codigo_cuenta"),
                                    disp.get("monto"))
            if reducir_saldo_cta:
                # Aumentar Saldo
                agregar_saldo_cta = cuentacliente_vm.modificar_saldo_cuenta_cliente(
                                    disp.get("codigo_cliente_transferir"),
                                    disp.get("codigo_cuenta_transferir"),
                                    disp.get("monto"),1)

                if agregar_saldo_cta and reducir_saldo_cta:
                    connection= conexion()
                    cursor = connection.cursor()
                    store_proc = "exec sp_Registrar_Transferencia @intCodigoTransferencia =?,\
                            @strCodigoCliente = ?, @strNumeroCuenta=?, @strCodigoClienteTransferencia=?,\
                            @strNumeroCuentaTransferencia=?, @dcmMonto = ?"
                    params = (len(self.lista_transferencia())+1,
                              disp.get("codigo_cliente"),
                              disp.get("codigo_cuenta"),
                              disp.get("codigo_cliente_transferir"),
                              disp.get("codigo_cuenta_transferir"),
                              disp.get("monto"))
                    cursor.execute(store_proc, params)
                    cursor.commit()
                    cursor.close()
            return agregar_saldo_cta and reducir_saldo_cta
        except ImportError as ex:
            print(ex)
            return []

    def lista_transferencia(self):
        """Lista de Transferencia"""
        try:
            transferencia = []
            connection= conexion()
            cursor = connection.cursor()
            cursor.execute("exec sp_Listar_Transferencia_Codigo")
            resultset= cursor.fetchall()
            for resultado in resultset:
                transferencia.append({
                    "codigo_transferencia": resultado[1],
                    "codigo_cliente":resultado[2],
                    "codigo_cuenta":resultado[3],
                    "codigo_cliente_transferir":resultado[4],
                    "codigo_cuenta_transferir":resultado[5],
                    "monto": resultado[6]})
            connection.close()
            return transferencia
        except ImportError as ex:
            print(ex)
            return []

    def buscar_transferencia_codigo(self, codigo_cliente):
        """Buscar la Transferencia por Código Cliente"""
        try:
            transferencia = []
            connection= conexion()
            cursor = connection.cursor()
            store_proc = "exec sp_Listar_Transferencia_Codigo @strCodigo=?"
            parametro = codigo_cliente
            cursor.execute(store_proc, parametro)
            resultset= cursor.fetchall()
            for resultado in resultset:
                transferencia.append({
                    "codigo_transferencia": resultado[1],
                    "codigo_cliente":resultado[2],
                    "codigo_cuenta":resultado[3],
                    "codigo_cliente_transferir":resultado[4],
                    "codigo_cuenta_transferir":resultado[5],
                    "monto": resultado[6],
                    "nombre_persona": resultado[7],
                    "transferencia_nombre_persona": resultado[8]})
            connection.close()
            return transferencia
        except ImportError as ex:
            print(ex)
            return []
