class Cliente:
    codigo:str
    # nombre:str
    # nroCuentaSoles:float
    # saldo:float
    # clave:str
    # estado: bool
    def __init__(self) -> None:
        pass
    def get_codigo(self):
        return self.codigo
    def set_codigo(self, value):
        self.codigo = value
