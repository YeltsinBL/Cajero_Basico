"""Transferencia"""
class Transferencia:
    """Clase Transferencia"""
    def __init__(self, codigo_transferencia, codigo_cliente, codigo_cuenta,
                 codigo_cliente_transferir, codigo_cuenta_transferir,
                 monto) -> None:
        self.codigo_transferencia = codigo_transferencia
        self.codigo_cliente = codigo_cliente
        self.codigo_cuenta = codigo_cuenta
        self.codigo_cliente_transferir = codigo_cliente_transferir
        self.codigo_cuenta_transferir = codigo_cuenta_transferir
        self.monto=monto
