"""Vista para las Operaciones por Cliente Consultar Movimiento"""
# region importaciones
from time import sleep
from colorama import Fore, Style
import Common.Validacion as validacion
import Common.mensaje as mensaje
import Controller.ClienteController as clientecontroller
import Controller.depositar_controller as depositocontroller
import Controller.retirar_controller as retirocontroller
import Controller.dispensador_controller as dispensadorcontroller
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
    vali_codigo_cliente = True
    vali_clave_cliente = True
    while vali_codigo_cliente:
        codigo_cliente = input("CÓDIGO CLIENTE: ")
        vali_codigo_cliente = not validacion.\
                                valores_ingresados("código del cliente",codigo_cliente,4)
        if vali_codigo_cliente is False:
            vali_codigo_cliente =  not clientecontroller.verifica_cliente_codigo(codigo_cliente)
            if vali_codigo_cliente:
                print(Style.BRIGHT + Fore.RED)
                print("===============================")
                print(msj.mensaje_no_existe("código del cliente"))
                print("===============================")
                print(Style.NORMAL + Fore.WHITE)
            else:
                cont = 0
                while vali_clave_cliente:
                    clave = input("CLAVE CLIENTE: ")
                    vali_clave_cliente = not clientecontroller.\
                        verifica_cliente_codigo_clave(codigo_cliente, clave)
                    if vali_clave_cliente:
                        print(Style.BRIGHT + Fore.RED)
                        print("===================================")
                        print(msj.mensaje_clave_incorrecta("clave"))
                        print("===================================")
                        cont +=1
                        if cont == 3:
                            vali_clave_cliente = False
                            return
                        intent = lambda cont : "intento" if(3-cont == 1) else "intentos"
                        print(f"LE QUEDA {3 - cont}", intent(cont).upper())
                        print("===================================")
                    print(Style.NORMAL + Fore.WHITE)
    resp_deposito = depositocontroller.buscar_deposito_codigo(codigo_cliente,0)
    if len(resp_deposito)>0:
        print(Style.BRIGHT + Fore.CYAN)
        print("============================")
        print(msj.mensaje_listado("depósitos"))
        print("============================")
        print(Style.NORMAL + Fore.WHITE)
        for deposito in resp_deposito:
            respt_cliente = clientecontroller.buscar_cliente_codigo(deposito.codigo_cliente)
            respt_dispensador = dispensadorcontroller.\
                        buscar_dispensador_codigo(int(deposito.codigo_dispensador))
            print("CLIENTE:",deposito.codigo_cliente, "-", respt_cliente.nombre)
            print("DISPENSADOR:",deposito.codigo_dispensador, "-", respt_dispensador.lugar)
            print("TOTAL:", deposito.monto)
            print("============================")
    else:
        print(Style.BRIGHT + Fore.YELLOW)
        print("===========================================")
        print(msj.mensaje_no_existe_lista("depósito"))
        print("===========================================")
    sleep(1)
    resp_retiro = retirocontroller.buscar_retiro(codigo_cliente)
    if len(resp_retiro)>0:
        print(Style.BRIGHT + Fore.CYAN)
        print("============================")
        print(msj.mensaje_listado("retiros"))
        print("============================")
        print(Style.NORMAL + Fore.WHITE)
        for retiro in resp_retiro:
            respt_cliente = clientecontroller.buscar_cliente_codigo(retiro.codigo_cliente)
            respt_dispensador = dispensadorcontroller.\
                        buscar_dispensador_codigo(int(retiro.codigo_dispensador))
            print("CLIENTE:",retiro.codigo_cliente, "-", respt_cliente.nombre)
            print("DISPENSADOR:",retiro.codigo_dispensador, "-", respt_dispensador.lugar)
            print("MONTO:", retiro.monto)
            print("============================")
    else:
        print(Style.BRIGHT + Fore.YELLOW)
        print("===========================================")
        print(msj.mensaje_no_existe_lista("retiro"))
        print("===========================================")
    sleep(1)
    resp_transferencia = transfereciacontroller.buscar_transferencia_codigo(codigo_cliente)
    if len(resp_transferencia)>0:
        print(Style.BRIGHT + Fore.CYAN)
        print("============================")
        print(msj.mensaje_listado("transferencia"))
        print("============================")
        print(Style.NORMAL + Fore.WHITE)
        for retiro in resp_transferencia:
            respt_cliente = clientecontroller.buscar_cliente_codigo(retiro.codigo_cliente)
            respt_dispensador = dispensadorcontroller.\
                        buscar_dispensador_codigo(int(retiro.codigo_dispensador))
            respt_cliente_trans = clientecontroller.\
                        buscar_cliente_codigo(retiro.codigo_cliente_transferir)
            respt_dispensador_trans = dispensadorcontroller.\
                        buscar_dispensador_codigo(int(retiro.codigo_dispensador_transferir))
            print("CLIENTE:",retiro.codigo_cliente, "-", respt_cliente.nombre)
            print("DISPENSADOR:",retiro.codigo_dispensador, "-", respt_dispensador.lugar)
            print("CLIENTE TRANSFERENCIA:",retiro.codigo_cliente_transferir, "-",
                                        respt_cliente_trans.nombre)
            print("DISPENSADOR TRANSFERENCIA:",retiro.codigo_dispensador_transferir, "-",
                                        respt_dispensador_trans.lugar)
            print("MONTO:", retiro.monto)
            print("============================")
    else:
        print(Style.BRIGHT + Fore.YELLOW)
        print("===========================================")
        print(msj.mensaje_no_existe_lista("transferencia"))
        print("===========================================")

# endregion
