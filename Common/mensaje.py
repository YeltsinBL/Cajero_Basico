"""Mensajes para cada acción en los formularios"""

class Mensaje:
    """Clase Mensaje"""
    def __init__(self) -> None:
        pass

# region Inicio Formulario
    def mensaje_frm_registro(self, nombre:str):
        """Mensaje: ¡REGISTRO DE {nombre}! """
        return f"¡REGISTRO DE {nombre.upper()}!"
    def mensaje_frm_modifica(self, nombre:str):
        """Mensaje: ¡MODIFICAR {nombre}!"""
        return f"¡MODIFICAR {nombre.upper()}!"
    def mensaje_frm_buscar(self, nombre:str):
        """Mensaje: ¡BUSCAR {nombre} POR CÓDIGO"""
        return f"¡BUSCAR {nombre.upper()} POR CÓDIGO!"
    def mensaje_frm_listar_estado(self, nombre:str, estado:str):
        """Mensaje: ¡LISTA DE LOS {nombre} {estado}!"""
        return f"¡LISTA DE LOS {nombre.upper()} {estado.upper()}!"
    def mensaje_frm_lista(self, nombre:str):
        """Mensaje: ¡LISTA DE LOS {nombre}!"""
        return f"¡LISTA DE LOS {nombre.upper()}!"
    def mensaje_frm_vista_previa(self, nombre:str):
        """Mensaje: ¡VISTA PREVIA DEL {nombre}!"""
        return f"¡VISTA PREVIA DEL {nombre.upper()}!"
    def mensaje_despedida(self):
        """Mensaje: ¡GRACIAS POR USAR ESTE SISTEMA!"""
        return "¡GRACIAS POR USAR ESTE SISTEMA!"
    def mensaje_frm_consultar(self, nombre:str):
        """Mensaje: ¡CONSULTAR {nombre} POR CÓDIGO"""
        return f"¡CONSULTAR {nombre.upper()} POR CÓDIGO!"
    def mensaje_todas_sus(self, nombre:str):
        """Mensaje: ¡TODAS SUS {nombre}"""
        return f"¡TODAS SUS {nombre.upper()}!"
    def mensaje_menu(self, nombre:str):
        """Mensaje: ¡MENÚ {nombre}"""
        return f"¡MENÚ {nombre.upper()}!"
# endregion

# region Exito
    def mensaje_existe(self, nombre:str):
        """Mensaje: ¡{nombre} ENCONTRADO!"""
        return f"¡{nombre.upper()} ENCONTRADO!"
    def mensaje_modificar(self, nombre:str):
        """Mensaje: ¡{nombre} MODIFICADO!"""
        return f"¡{nombre.upper()} MODIFICADO!"
    def mensaje_encontro_por_estado(self,nombre:str, estado:str):
        """Mensaje: ¡TODOS LOS {nombre} {estado}!"""
        return f"¡TODOS LOS {nombre.upper()} {estado.upper()}!"
    def mensaje_registrado(self, nombre:str):
        """Mensaje: ¡{nombre} REGISTRADO!"""
        return f"¡{nombre.upper()} REGISTRADO!"
    def mensaje_listado(self, nombre:str):
        """Mensaje: ¡TODOS LOS {nombre}!"""
        return f"¡TODOS LOS {nombre.upper()}!"
    def mensaje_su_numero_cuenta(self, cantidad):
        """Mensaje: ¡SU NÚMERO DE CUENTA ES: {cantidad}!"""
        return f"¡SU NÚMERO DE CUENTA ES: {cantidad}!"
# endregion

# region ERRORES
    def mensaje_no_existe(self, nombre:str):
        """Mensaje: ¡EL {nombre} INGRESADO NO EXISTE! """
        return f"¡EL {nombre.upper()} INGRESADO NO EXISTE!"
    def mensaje_error_al(self, tipo:str, nombre:str):
        """Mensaje: ¡HUBO UN ERROR AL {tipo} EL {nombre}!"""
        return f"¡HUBO UN ERROR AL {tipo.upper()} EL {nombre.upper()}!"
    def mensaje_no_encontro_por_estado(self, nombre:str, estado:str):
        """Mensaje: ¡NO HAY {nombre} {estado}!"""
        return f"¡NO HAY {nombre.upper()} {estado.upper()}!"
    def mensaje_no_existe_lista(self, nombre:str):
        """Mensaje: ¡NO EXISTE {nombre}! """
        return f"¡NO EXISTE {nombre.upper()}!"
    def mensaje_monto_mayor_cero(self):
        """Mensaje: ¡NO EXISTE {nombre}! """
        return "¡EL MONTO INGRESADO DEBE SER MAYOR A CERO!"
    def mensaje_mantenimiento(self, nombre:str):
        """Mensaje: ¡{nombre} EN MANTENIMIENTO!"""
        return f"¡{nombre.upper()} EN MANTENIMIENTO!"
    def mensaje_transferencia_codigo_iguales(self):
        """Mensaje: ¡NO SE PUEDE TRANSFERIR A SU MISMA CUENTA!"""
        return "¡NO SE PUEDE TRANSFERIR A SU MISMA CUENTA!"
#endregion

# region Validaciones
    def mensaje_cancelar_confirmacion(self, nombre:str):
        """Mensaje: ¡USTED HA CANCELADO EL REGISTRO DEL {nombre}!"""
        return f"¡USTED HA CANCELADO EL REGISTRO DEL {nombre.upper()}!"
    def mensaje_verificar_tipo(self, tipo:str, nombre:str):
        """Mensaje: ¡Verificando {tipo} en {nombre}!"""
        return str(f"¡Verificando {tipo} en {nombre}!").upper()
    def mensaje_monto_excedido(self, nombre:str):
        """Mensaje: ¡EL MONTO INGRESADO EXCEDE {nombre.upper()}!"""
        return str(f"¡El monto ingresado excede {nombre}!").upper()
    def mensaje_error_confirmar(self):
        """Mensaje: ¡INGRESE SI O NO!"""
        print("¡INGRESE SI O NO!")
    def mensaje_clave_incorrecta(self, nombre:str):
        """Mensaje: ¡LA {nombre} INGRESADA ES INCORRECTA! """
        return f"¡LA {nombre.upper()} INGRESADA ES INCORRECTA!"
    def mensaje_realizando_accion(self, nombre:str):
        """Mensaje: ¡REALIZANDO {nombre}! """
        return f"¡REALIZANDO {nombre.upper()}!"
    def mensaje_opcion_ingresada_incorrecta(self):
        """Mensaje: ¡INGRESE UNA OPCIÓN VÁLIDA! """
        return "¡INGRESE UNA OPCIÓN VÁLIDA!"
    def mensaje_no_tiene(self, nombre:str, detalle:str):
        """Mensaje: ¡EL {nombre.upper()} NO TIENE {detalle.upper()}! """
        return f"¡EL {nombre.upper()} NO TIENE {detalle.upper()}!"
    def mensaje_no_esta(self, nombre:str, detalle:str):
        """Mensaje: ¡{nombre} NO ESTA {detalle}!"""
        return f"¡{nombre.upper()} NO ESTA {detalle.upper()}!"
    def mensaje_no_se_puede(self, detalle:str):
        """Mensaje: NO SE PUEDE {detalle}"""
        return f"¡NO SE PUEDE {detalle.upper()}!"
    def mensaje_usted_cuenta(self, nombre:str, detalle):
        """Mensaje: USTED CUENTA CON {nombre} {detalle}"""
        return f"¡USTED CUENTA CON {nombre.upper()} {detalle}!"
# endregion
