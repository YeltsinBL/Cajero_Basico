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
    codigo_cliente = elemento.ingresar_codigo_cliente(
        nombre="código del cliente", verificar_cuenta=True, verificar_estado=True)
    if codigo_cliente =="":
        return
    clave = elemento.ingresar_clave_cliente("clave del cliente", codigo_cliente)
    if clave is False:
        return
    nro_cuenta = elemento.ingresar_numero_cuenta(
        nombre="nro. cuenta soles",codigo_cliente=codigo_cliente, verificar_estado=True)
    if nro_cuenta=="":
        return
    codigo_cliente_trans = elemento.ingresar_codigo_cliente(
        nombre="código del cliente a transferir", verificar_cuenta=True, verificar_estado=True)
    if codigo_cliente_trans =="":
        return
    nro_cuenta_transferir = elemento.ingresar_numero_cuenta(
        nombre="nro. cuenta a transferir",codigo_cliente=codigo_cliente_trans,
        verificar_estado=True)
    if nro_cuenta_transferir=="":
        return
    if codigo_cliente==codigo_cliente_trans and\
            nro_cuenta==nro_cuenta_transferir:
        print(Style.BRIGHT + Fore.RED)
        print("===============================")
        print(msj.mensaje_no_se_puede("TRANSFERIR A SU MISMA CUENTA"))
        print("===============================")
        print(Style.NORMAL + Fore.WHITE)
        return
    monto = elemento.ingresar_monto(codigo_cliente=codigo_cliente, numero_cuenta=nro_cuenta)
    if monto==float(0):
        return
    datos = {"codigo_cliente":codigo_cliente, "codigo_cuenta":nro_cuenta,
                "codigo_cliente_transferir":codigo_cliente_trans, 
                "codigo_cuenta_transferir":nro_cuenta_transferir,
                "monto":monto}
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
