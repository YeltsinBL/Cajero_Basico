"""Vista para las Operaciones por Cliente Consultar Movimiento"""
# region importaciones
from time import sleep
from colorama import Fore, Style
from Common import mensaje
from Common import elemento
import Controller.ClienteController as clientecontroller
import Controller.depositar_controller as depositocontroller
import Controller.retirar_controller as retirocontroller
import Controller.dispensador_controller as dispensadorcontroller
import Controller.transferencia_controller as transfereciacontroller
import Controller.cuenta_cliente_controller as cuentaclientecontroller
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
    resp_deposito = depositocontroller.buscar_deposito_codigo(codigo_cliente,0)
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
            respt_cliente = clientecontroller.buscar_cliente_codigo(deposito.get("codigo_cliente"))
            respt_dispensador = dispensadorcontroller.\
                        buscar_dispensador_codigo(int(deposito.get("codigo_dispensador")))
            cuenta_cliente = cuentaclientecontroller.buscar_saldo_cuenta_cliente(
                                deposito.get("codigo_cliente"))
            for dispensador in respt_dispensador:
                for cuenta in cuenta_cliente:
                    print("CLIENTE:",deposito.get("codigo_cliente"), "-", respt_cliente[2])
                    print("NRO. CUENTA SOLES:",cuenta[1])
                    print("DISPENSADOR:",deposito.get("codigo_dispensador"), "-",
                          dispensador.get("lugar"))
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
            respt_cliente = clientecontroller.buscar_cliente_codigo(retiro.get("codigo_cliente"))
            respt_dispensador = dispensadorcontroller.\
                        buscar_dispensador_codigo(int(retiro.get("codigo_dispensador")))
            cuenta_cliente = cuentaclientecontroller.buscar_saldo_cuenta_cliente(
                                retiro.get("codigo_cliente"))
            for dispensador in respt_dispensador:

                for cuenta in cuenta_cliente:
                    print("CLIENTE:",retiro.get("codigo_cliente"), "-", respt_cliente[2])
                    print("NRO. CUENTA SOLES:",cuenta[1])
                    print("DISPENSADOR:",retiro.get("codigo_dispensador"), "-",
                          dispensador.get("lugar"))
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
            respt_cliente = clientecontroller.buscar_cliente_codigo(
                                transferencia.get("codigo_cliente"))
            cuenta_cliente = cuentaclientecontroller.buscar_saldo_cuenta_cliente(
                transferencia.get("codigo_cliente"))
            respt_cliente_trans = clientecontroller.\
                        buscar_cliente_codigo(transferencia.get("codigo_cliente_transferir"))
            cuenta_cliente_trans = cuentaclientecontroller.buscar_saldo_cuenta_cliente(
                transferencia.get("codigo_cliente_transferir"))
            print("CLIENTE:",transferencia.get("codigo_cliente"), "-", respt_cliente[2])
            for cuenta in cuenta_cliente:
                print("NRO. CUENTA SOLES:",cuenta[1])
            print("CLIENTE TRANSFERENCIA:",transferencia.get("codigo_cliente_transferir"), "-",
                                        respt_cliente_trans[2])
            for cuenta in cuenta_cliente_trans:
                print("NRO. CUENTA SOLES TRANSFERENCIA:",cuenta[1])
            print("MONTO:", transferencia.get("monto"))
            print("============================")
    else:
        print(Style.BRIGHT + Fore.YELLOW)
        print("===========================================")
        print(msj.mensaje_no_existe_lista("transferencia"))
        print("===========================================")
# endregion
