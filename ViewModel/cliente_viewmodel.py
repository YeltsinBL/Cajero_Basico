"""Cliente ViewModel"""
import Data.service as service
import Model.Cliente as clientemodel
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
            cursor.execute("exec sp_ListaCliente")
            resultset= cursor.fetchall()
            # for cliente in resultset:
            #     print("SP1:",cliente)
            connection.close()
            return resultset
        except ImportError as ex:
            print(ex)
            return []
        # cantidad = len(service.clientes)
        # if cantidad > 0:
        #     for i in range(0, cantidad-1):
        #         for k in range(0, cantidad-(i+1)):
        #             if service.clientes[k].codigo>service.clientes[k+1].codigo:
        #                 aux=service.clientes[k]
        #                 service.clientes[k]=service.clientes[k+1]
        #                 service.clientes[k+1]= aux
        #     return service.clientes
        # return service.clientes

    def registrar_cliente(self, dicts:dict[str,any]):
        """Registro Cliente"""
        # cliente = clientemodel.Cliente(codigo=dicts.get("codigo"),
        #                              nombre=dicts.get("nombre"),
        #                              clave=dicts.get("clave"),
        #                              estado=dicts.get("estado"))
        # service.clientes.append(cliente)
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

    def verifica_cliente_codigo(self, codigo):
        """Buscar Cliente por Código"""
        for dato in service.clientes:
            if dato.codigo == codigo:
                return True
        return False

    def modificar_cliente(self, dicts:dict[str,any]):
        """Modificar Cliente"""
        for dato in service.clientes:
            if dato.codigo == dicts.get("codigo"):
                dato.nombre=dicts["nombre"]
                dato.estado=dicts["estado"]
                return True
        return False

    def buscar_cliente_codigo(self, codigo):
        """Buscar Cliente por Código"""
        cliente = []
        for dato in service.clientes:
            if dato.codigo == codigo:
                cliente = dato
                return cliente
        return cliente

    def lista_cliente_estado(self, estado):
        """Listar los Clientes por su estado"""
        cliente = []
        for dato in service.clientes:
            if dato.estado == estado:
                cliente.append(dato)
        return cliente
    def verifica_cliente_codigo_clave(self, codigo, clave):
        """Buscar Cliente por Código"""
        for dato in service.clientes:
            if dato.codigo == codigo and dato.clave ==clave:
                return True
        return False
