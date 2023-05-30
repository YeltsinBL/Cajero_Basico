"""Mensajes para cada acción en los formularios"""

class Mensaje:
    """Clase Mensaje"""
    def __init__(self) -> None:
        pass

# region Inicio Formulario
    def mensaje_frm_registro(self, nombre):
        """Mensaje que inicia el formulario de registro"""
        return f"¡REGISTRO DE {nombre}!"
    def mensaje_frm_modifica(self, nombre):
        """Mensaje que inicia el formulario de modificar"""
        return f"¡MODIFICAR {nombre}!"
    def mensaje_frm_buscar(self, nombre):
        """Mensaje que inicia el formulario de buscar"""
        return f"¡BUSCAR {nombre} POR CÓDIGO!"
    def mensaje_frm_listar_estado(self, nombre, estado):
        """Mensaje que inicia el listado por estado"""
        return f"¡LISTA DE LOS {nombre} {estado}!"
    def mensaje_frm_lista(self, nombre):
        """Mensaje que inicia el listado"""
        return f"¡LISTA DE LOS {nombre}!"
# endregion

# region Exito
    def mensaje_existe(self, nombre):
        """Mensaje cuando existe un elemento buscado"""
        return f"¡{nombre} ENCONTRADO!"
    def mensaje_modificar(self, nombre):
        """Mensaje cuando se modificó"""
        return f"¡{nombre} MODIFICADO!"
    def mensaje_encontro_por_estado(self,nombre, estado):
        """Mensaje cuando encontro un elemento por su estado"""
        return f"¡TODOS LOS {nombre} {estado}!"
    def mensaje_registrado(self, nombre):
        """Mensaje cuando se registró"""
        return f"¡{nombre} REGISTRADO!"
    def mensaje_listado(self, nombre):
        """Mensaje cuando se listó"""
        return f"¡TODOS LOS {nombre}!"
# endregion

# region ERRORES
    def mensaje_no_existe(self, nombre):
        """Mensaje cuando no existe un elemento buscado"""
        return f"¡EL {nombre} INGRESADO NO EXISTE!"
    def mensaje_error_modificar(self, nombre):
        """Mensaje cuando hubo un error al modificar"""
        return f"¡HUBO UN ERROR AL MODIFICAR EL {nombre}!"
    def mensaje_error_buscar(self, nombre):
        """Mensaje cuando hubo un error al buscar"""
        return f"¡HUBO UN ERROR AL BUSCAR EL {nombre}!"
    def mensaje_no_encontro_por_estado(self, nombre, estado):
        """Mensaje cuando no encontro un elemento por su estado"""
        return f"¡NO HAY {nombre} {estado}!"
#endregion
