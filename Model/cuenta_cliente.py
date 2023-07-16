"""Cuenta Cliente"""
class CuentaCliente:
    """Clase Cuenta Cliente"""
    def __init__(self, codigo_cuenta, codigo_cliente,
                 monto, estado) -> None:
        self.codigo_cuenta = codigo_cuenta
        self.codigo_cliente = codigo_cliente
        self.monto=monto
        self.estado=estado
