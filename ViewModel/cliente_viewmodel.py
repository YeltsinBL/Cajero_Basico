"""Cliente ViewModel"""
import Api.service as service
import Model.Cliente as clientemodel
class  ClienteViewModel:
    """Clase Ciente ViewModel"""
    def __init__(self) -> None:
        pass

    def lista_cliente(self):
        """LISTADO DE CLIENTES"""
        return service.clientes

    def registrar_cliente(self, dicts:dict[str,any]):
        """Registro Cliente"""
        clien = clientemodel.Cliente(codigo=dicts.get("codigo"),
                                     nombre=dicts.get("nombre"),
                                     nrocuentasoles=dicts.get("nrocuentasoles"),
                                     saldo=dicts.get("saldo"),
                                     clave=dicts.get("clave"),
                                     estado=dicts.get("estado"))
        service.clientes.append(clien)

    def verifica_cliente_codigo(self, codigo):
        """Buscar Cliente por Id"""
        existe= False
        for dato in service.clientes:
            existe = dato.codigo == codigo
            if existe:
                return existe
        return existe

    def modificar_cliente(self, dicts:dict[str,any]):
        """Modificar Cliente"""
        for dato in service.clientes:
            if dato.codigo == dicts.get("codigo"):
                dato.nombre=dicts["nombre"]
                dato.nrocuentasoles=dicts["nrocuentasoles"]
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
            if dato.estado.lower() == estado:
                cliente.append(dato)
        return cliente
