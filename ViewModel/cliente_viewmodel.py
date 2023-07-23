"""Cliente ViewModel"""
import ViewModel.cuenta_cliente_viewmodel as cuentaclienteviewmodel
from Data.conexion import conexion

cuentacliente_vm = cuentaclienteviewmodel.CuentaClienteViewModel()

class  ClienteViewModel:
    """Clase Ciente ViewModel"""
    def __init__(self) -> None:
        pass

    def lista_cliente(self):
        """LISTADO DE CLIENTES"""
        try:
            connection= conexion()
            cursor = connection.cursor()
            cursor.execute("exec sp_ListarCliente_Codigo")
            resultset= cursor.fetchall()
            connection.close()
            return resultset
        except ImportError as ex:
            print(ex)
            return []

    def registrar_cliente(self, dicts:dict[str,any]):
        """Registro Cliente"""
        try:
            connection= conexion()
            cursor = connection.cursor()
            store_proc = "exec sp_CrearCliente @strCodigo = ?, @strNombre = ?, @strClave = ?"
            params = (dicts.get("codigo"), dicts.get("nombre"), dicts.get("clave"))
            cursor.execute(store_proc, params)
            cursor.commit()
            cursor.close()
        except ImportError as ex:
            print(ex)
        cuenta_cliente={"codigo_cliente":dicts.get("codigo"),
                        "monto":0}
        return cuentacliente_vm.registro_cuenta_cliente(cuenta_cliente)

    def modificar_cliente(self, dicts:dict[str,any]):
        """Modificar Cliente"""
        try:
            connection= conexion()
            cursor = connection.cursor()
            store_proc = "exec sp_ModificarCliente @strCodigo = ?, @strNombre = ?, @bitEstado = ?"
            params = (dicts.get("codigo"), dicts.get("nombre"), dicts.get("estado"))
            cursor.execute(store_proc, params)
            cursor.commit()
            cursor.close()
            return True
        except ImportError as ex:
            print(ex)
            return False

    def buscar_cliente_codigo(self, codigo):
        """Buscar Cliente por Código"""
        try:
            connection= conexion()
            cursor = connection.cursor()
            store_proc = "exec sp_ListarCliente_Codigo @strCodigo = ?"
            params = codigo
            cursor.execute(store_proc, params)
            resultset= cursor.fetchone()
            connection.close()
            return resultset
        except ImportError as ex:
            print(ex)
            return []

    def lista_cliente_estado(self, estado = None):
        """Listar los Clientes por su estado"""
        try:
            connection= conexion()
            cursor = connection.cursor()
            store_proc = "exec sp_ListarCliente_Codigo @bitEstado = ?"
            params = estado
            cursor.execute(store_proc, params)
            resultset= cursor.fetchall()
            connection.close()
            return resultset
        except ImportError as ex:
            print(ex)
            return []
    def verifica_cliente_codigo_clave(self, codigo, clave):
        """Buscar Cliente por Código"""
        try:
            connection= conexion()
            cursor = connection.cursor()
            store_proc = "exec sp_Listar_Cliente_Clave @strCodigo = ?, @strClave =?"
            params = (codigo, clave)
            cursor.execute(store_proc, params)
            resultset= cursor.fetchone()
            connection.close()
            return True if len(resultset)>0 else False
        except ImportError as ex:
            print(ex)
            return False
