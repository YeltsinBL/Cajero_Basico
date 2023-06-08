"""Cuenta Cliente"""
class CuentaCliente:
    """Clase Cuenta Cliente"""
    def __init__(self, codigo_cuenta, codigo_cliente, codigo_dispensador,
                 monto) -> None:
        self.codigo_cuenta = codigo_cuenta
        self.codigo_cliente = codigo_cliente
        self.codigo_dispensador = codigo_dispensador
        self.monto=monto
