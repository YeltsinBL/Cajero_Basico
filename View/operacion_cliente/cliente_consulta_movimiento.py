"""Vista para las Operaciones por Cliente Consultar Movimiento"""
# region importaciones
from time import sleep
from colorama import Fore, Style
from Common import mensaje
from Common import elemento
import Controller.depositar_controller as depositocontroller
import Controller.retirar_controller as retirocontroller
import Controller.transferencia_controller as transfereciacontroller
# endregion

msj = mensaje.Mensaje()

# region Formulario Movimiento
def frm_consulta_movimiento():
    """Consulta de Movimiento"""
    print(Style.BRIGHT + Fore.CYAN)
    print("================================")
    print(msj.mensaje_frm_consultar("movimiento"))
    print("================================")
    print(Style.NORMAL + Fore.WHITE)
    codigo_cliente = elemento.ingresar_codigo_cliente(
        nombre="código del cliente", verificar_cuenta=True, verificar_estado=True)
    if codigo_cliente =="":
        return
    clave = elemento.ingresar_clave_cliente("clave del cliente", codigo_cliente)
    if clave is False:
        return
    resp_deposito = depositocontroller.buscar_deposito_codigo(codigo_cliente)
    listado_deposito(resp_deposito)
    sleep(1)
    resp_retiro = retirocontroller.buscar_retiro(codigo_cliente)
    listado_retiro(resp_retiro)
    sleep(1)
    resp_transferencia = transfereciacontroller.buscar_transferencia_codigo(codigo_cliente)
    listado_transferencia(resp_transferencia)

def listado_deposito(resp_deposito):
    """Listado de los depósitos"""
    if len(resp_deposito)>0:
        print(Style.BRIGHT + Fore.CYAN)
        print("============================")
        print(msj.mensaje_listado("depósitos"))
        print("============================")
        print(Style.NORMAL + Fore.WHITE)
        for deposito in resp_deposito:
            print("CLIENTE:", deposito.get("codigo_cliente"), "-", deposito.get("nombre_persona"))
            print("NRO. CUENTA SOLES:", deposito.get("numero_cuenta"))
            print("DISPENSADOR:",deposito.get("codigo_dispensador"), "-",
                  deposito.get("dispensador_lugar"))
            print("TOTAL:", deposito.get("monto"))
            print("============================")
    else:
        print(Style.BRIGHT + Fore.YELLOW)
        print("===========================================")
        print(msj.mensaje_no_existe_lista("depósito"))
        print("===========================================")
def listado_retiro(resp_retiro):
    """Listadp de los Retiros"""
    if len(resp_retiro)>0:
        print(Style.BRIGHT + Fore.CYAN)
        print("============================")
        print(msj.mensaje_listado("retiros"))
        print("============================")
        print(Style.NORMAL + Fore.WHITE)
        for retiro in resp_retiro:
            print("CLIENTE:", retiro.get("codigo_cliente"), "-", retiro.get("nombre_persona"))
            print("NRO. CUENTA SOLES:", retiro.get("numero_cuenta"))
            print("DISPENSADOR:",retiro.get("codigo_dispensador"), "-",
                  retiro.get("dispensador_lugar"))
            print("MONTO:", retiro.get("monto"))
            print("============================")
    else:
        print(Style.BRIGHT + Fore.YELLOW)
        print("===========================================")
        print(msj.mensaje_no_existe_lista("retiro"))
        print("===========================================")
def listado_transferencia(resp_transferencia):
    """Listado de las Transferencias"""
    if len(resp_transferencia)>0:
        print(Style.BRIGHT + Fore.CYAN)
        print("============================")
        print(msj.mensaje_listado("transferencia"))
        print("============================")
        print(Style.NORMAL + Fore.WHITE)
        for transferencia in resp_transferencia:
            print("CLIENTE:",transferencia.get("codigo_cliente"), "-",
                  transferencia.get("nombre_persona"))
            print("NRO. CUENTA SOLES:", transferencia.get("codigo_cuenta"))
            print("CLIENTE TRANSFERENCIA:",transferencia.get("codigo_cliente_transferir"), "-",
                                        transferencia.get("transferencia_nombre_persona"))
            print("NRO. CUENTA SOLES TRANSFERENCIA:", transferencia.get("codigo_cuenta_transferir"))
            print("MONTO:", transferencia.get("monto"))
            print("============================")
    else:
        print(Style.BRIGHT + Fore.YELLOW)
        print("===========================================")
        print(msj.mensaje_no_existe_lista("transferencia"))
        print("===========================================")
# endregion
