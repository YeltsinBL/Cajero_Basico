"""Vista para las Operaciones por Cliente Transferir"""
# region importaciones
from time import sleep
from colorama import Fore, Style
from Common import mensaje
from Common import elemento
import Controller.transferencia_controller as transferenciacontroller
# endregion

msj = mensaje.Mensaje()

# region Formulario Transferir
def frm_cliente_transferencia():
    """Consulta de Transferencia"""
    print(Style.BRIGHT + Fore.CYAN)
    print("================================")
    print(msj.mensaje_frm_registro("transferencia"))
    print("================================")
    print(Style.NORMAL + Fore.WHITE)
    codigo_cliente = elemento.ingresar_codigo_cliente("código del cliente", True)
    if codigo_cliente =="":
        return
    clave = elemento.ingresar_clave_cliente("clave del cliente", codigo_cliente)
    if clave is False:
        return
    codigo_dispensador = elemento.ingresar_codigo_dispensador(
        nombre="código del dispensador", codigo_cliente=codigo_cliente, verificar_cuenta=True)
    if codigo_dispensador == 0:
        return
    codigo_cliente_trans = elemento.ingresar_codigo_cliente("código del cliente a transferir", True)
    if codigo_cliente_trans =="":
        return
    codigo_dispensador_transferir = elemento.ingresar_codigo_dispensador(
        nombre="código dispensador a transferir", codigo_cliente=codigo_cliente_trans,
        mensaje_cliente="cliente a transferir", verificar_cuenta=True)
    if codigo_dispensador_transferir == 0:
        return
    if codigo_cliente==codigo_cliente_trans and\
            codigo_dispensador==codigo_dispensador_transferir:
        mensaje_transferir_misma_cuenta()
        return
    monto = elemento.ingresar_monto(codigo_dispensador,codigo_cliente)
    if monto==0:
        return
    datos = {"codigo_cliente":codigo_cliente, "codigo_dispensador":int(codigo_dispensador),
                "codigo_cliente_transferir":codigo_cliente_trans, 
                "codigo_dispensador_transferir":int(codigo_dispensador_transferir),
                "monto":float(monto)}
    sleep(1)
    print(Style.BRIGHT + Fore.YELLOW+"===============================")
    print(msj.mensaje_realizando_accion("transferencia"))
    print("===============================")
    resp = transferenciacontroller.registro_transferencia(datos)
    if resp:
        print(Style.BRIGHT + Fore.GREEN)
        print("======================")
        print(msj.mensaje_registrado("transferencia"))
        print("======================")
    else:
        print(Style.BRIGHT + Fore.RED)
        print("======================")
        print(msj.mensaje_error_al("registrar","transferencia"))
        print("======================")
# endregion

# region Formato de Mensajes
def mensaje_transferir_misma_cuenta():
    """Mensaje: No se puede transferir a la misma cuenta"""
    print(Style.BRIGHT + Fore.RED)
    print("===============================")
    print(msj.mensaje_transferencia_codigo_iguales())
    print("===============================")
    print(Style.NORMAL + Fore.WHITE)
# endregion
