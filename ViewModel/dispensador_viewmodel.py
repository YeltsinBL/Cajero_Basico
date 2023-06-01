"""Dispensador ViewModel"""
# region Importación
import Api.service as service
import Model.dispensador as dispensador
#endregion

class DispensadorViewModel:
    """Clase Dispensador ViewModel"""
    def __init__(self) -> None:
        pass
    def lista_dispensadores(self):
        """Lista de Dispensadores"""
        return service.dispensadores

    def registrar_dispensador(self, disp:dict[str,any]):
        """Registro Dispensador"""
        dispensa = dispensador.Dispensador(codigo=disp.get("codigo"),
                                     lugar=disp.get("lugar"),
                                     estado=disp.get("estado"),
                                     billete=disp.get("billete"))
        service.dispensadores.append(dispensa)

    def verifica_dispensador_codigo(self, codigo):
        """Buscar Dispensador por código"""
        existe= False
        for dato in service.dispensadores:
            existe = dato.codigo == codigo
            if existe:
                return existe
        return existe

    def modificar_dispensador(self, dicts:dict[str,any]):
        """Modificar Dispensador"""
        for dato in service.dispensadores:
            if dato.codigo == dicts.get("codigo"):
                dato.lugar=dicts["lugar"]
                dato.estado=dicts["estado"]
                dato.billete=dicts["billete"]
                return True
        return False

    def buscar_dispensador_codigo(self, codigo):
        """Buscar Dispensador por Código"""
        dispensa = []
        for dato in service.dispensadores:
            if dato.codigo == codigo:
                dispensa = dato
                return dispensa
        return dispensa

    def lista_dispensador_estado(self, estado):
        """Listar los Dispensadores por su estado"""
        dispensa = []
        for dato in service.dispensadores:
            if dato.estado.lower() == estado:
                dispensa.append(dato)
        return dispensa

    def verificar_monto_dispensador(self, codigo_dispensador:int, monto:float):
        """Verificar el Monto del Dispensador"""
        cantidad:float = 0
        lista_dispensador = self.lista_dispensadores()
        for dato in lista_dispensador:
            if dato.codigo == codigo_dispensador:
                for valor in dato.billete:
                    for nro_billete, vbillete in valor.items():
                        cantidad = cantidad +(nro_billete * vbillete)
        if cantidad >= monto:
            return True
        else: return False
    # actualizar la verificación del monto a retirar
    # Listar Depósitos que queda después de retirar
