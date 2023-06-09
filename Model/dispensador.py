"""Clase Dispensador"""
class Dispensador:
    """Clase Dispensador"""
    def __init__(self, codigo, lugar, estado, billete:list) -> None:
        self.codigo = codigo
        self.lugar = lugar
        self.estado = estado
        self.billete=billete
# class Billete:
#     """Clase Billete"""
#     def __init__(self, _200, lugar, estado) -> None:
#         self._200 = _200
#         self.lugar = lugar
#         self.estado = estado
