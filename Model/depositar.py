"""Depositar"""
class Depositar:
    """Clase Depositar"""
    def __init__(self, codigo_cliente, codigo_dispensador,
                 billete:list) -> None:
        self.codigo_cliente = codigo_cliente
        self.codigo_dispensador = codigo_dispensador
        self.billete=billete
