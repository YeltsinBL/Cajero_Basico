class Persona:
    """Clase Persona"""
    def __init__(self, codigo, nombre) -> None:
        self.codigo = codigo
        self.nombre = nombre

class Cliente(Persona):
    """Clase Cliente"""
    def __init__(self, codigo=None, nombre=None, nrocuentasoles=None, saldo=0,\
                clave=None, estado=None) -> None:
        Persona.__init__(self,codigo, nombre)
        self.nrocuentasoles = nrocuentasoles
        self.saldo = saldo
        self.clave = clave
        self.estado = estado

    def input_persona(self, cls):
        """Aceptar entradas de Persona"""
        self.codigo = cls.codigo
        self.nombre = cls.nombre
