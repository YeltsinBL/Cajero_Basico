"""Transferencia"""
class Transferencia:
    """Clase Transferencia"""
    def __init__(self, codigo_transferencia, codigo_cliente, codigo_dispensador,
                 codigo_cliente_transferir, codigo_dispensador_transferir,
                 monto) -> None:
        self.codigo_transferencia = codigo_transferencia
        self.codigo_cliente = codigo_cliente
        self.codigo_dispensador = codigo_dispensador
        self.codigo_cliente_transferir = codigo_cliente_transferir
        self.codigo_dispensador_transferir = codigo_dispensador_transferir
        self.monto=monto
