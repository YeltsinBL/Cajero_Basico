"""Vista para las Operaciones por Cliente Transferir"""
# region importaciones
from time import sleep
from colorama import Fore, Style
import Common.Validacion as validacion
import Common.mensaje as mensaje
import Controller.ClienteController as clientecontroller
import Controller.transferencia_controller as transferenciacontroller
import Controller.dispensador_controller as dispensadorcontroller
import Controller.cuenta_cliente_controller as cuentaclientecontroller
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
    vali_codigo_cliente = True
    vali_clave_cliente = True
    vali_codigo_dispensador= True
    while vali_codigo_cliente:
        codigo_cliente = input("CÓDIGO CLIENTE: ")
        vali_codigo_cliente = not validacion.\
                                valores_ingresados("código del cliente",codigo_cliente,4)
        if vali_codigo_cliente is False:
            vali_codigo_cliente = not clientecontroller.verifica_cliente_codigo(codigo_cliente)
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
    while vali_codigo_dispensador:
        codigo_dispensador = input("CÓDIGO DISPENSADOR: ")
        vali_codigo_dispensador = not validacion.\
                                    valores_ingresados("código dispensador",codigo_dispensador,1)
        if vali_codigo_dispensador is False:
            vali_codigo_dispensador = not dispensadorcontroller\
                                .verifica_dispensador_codigo(int(codigo_dispensador))
            if vali_codigo_dispensador:
                print(Style.BRIGHT + Fore.RED)
                print("===============================")
                print(msj.mensaje_no_existe("código del dispensador"))
                print("===============================")
                print(Style.NORMAL + Fore.WHITE)
    vali_codigo_cliente_transferencia = True
    vali_codigo_dispensador_transferir = True
    while vali_codigo_cliente_transferencia:
        codigo_cliente_trans = input("CÓDIGO CLIENTE A TRANSFERIR: ")
        vali_codigo_cliente_transferencia = not validacion.\
                                valores_ingresados("código del cliente a transferir",
                                                   codigo_cliente_trans,4)
        if vali_codigo_cliente_transferencia is False:
            vali_codigo_cliente_transferencia = not clientecontroller\
                                        .verifica_cliente_codigo(codigo_cliente_trans)
            if vali_codigo_cliente_transferencia:
                print(Style.BRIGHT + Fore.RED)
                print("===============================")
                print(msj.mensaje_no_existe("código del cliente a transferir"))
                print("===============================")
                print(Style.NORMAL + Fore.WHITE)
            else:
                while vali_codigo_dispensador_transferir:
                    codigo_dispensador_transferir = input("CÓDIGO DISPENSADOR A TRANSFERIR: ")
                    vali_codigo_dispensador_transferir = not validacion.\
                                            valores_ingresados("código dispensador a transferir",
                                                                codigo_dispensador_transferir,1)
                    if vali_codigo_dispensador_transferir is False:
                        vali_codigo_dispensador_transferir = not dispensadorcontroller\
                                    .verifica_dispensador_codigo(int(codigo_dispensador_transferir))
                        if vali_codigo_dispensador_transferir:
                            print(Style.BRIGHT + Fore.RED)
                            print("===============================")
                            print(msj.mensaje_no_existe("código del dispensador a transferir"))
                            print("===============================")
                            print(Style.NORMAL + Fore.WHITE)
        if codigo_cliente==codigo_cliente_trans and\
            codigo_dispensador==codigo_dispensador_transferir:
            vali_codigo_cliente_transferencia= True
            vali_codigo_dispensador_transferir = True
            print(Style.BRIGHT + Fore.RED)
            print("===============================")
            print(msj.mensaje_transferencia_codigo_iguales())
            print("===============================")
            print(Style.NORMAL + Fore.WHITE)

    vali_monto = True
    while vali_monto:
        monto = input("MONTO: ")
        vali_monto = not validacion.valores_ingresados("MONTO",monto,2)
        if vali_monto is False:
            print(Style.BRIGHT + Fore.YELLOW)
            print("====================================================")
            print(msj.mensaje_verificar_tipo("saldo","el dispensador"))
            print("====================================================")
            sleep(1)
            vali_monto = not dispensadorcontroller.verificar_monto_dispensador(
                                        int(codigo_dispensador), float(monto))
            if vali_monto:
                print(Style.BRIGHT + Fore.RED)
                print("===============================")
                print(msj.mensaje_monto_excedido("al dispensador"))
                print("===============================")
            else:
                print("====================================================")
                print(msj.mensaje_verificar_tipo("saldo","la cuenta del cliente"))
                print("====================================================")
                sleep(1)
                vali_monto = not cuentaclientecontroller.verificar_cuenta_cliente(
                                        codigo_cliente, int(codigo_dispensador), float(monto))
                if vali_monto:
                    print(Style.BRIGHT + Fore.RED)
                    print("====================================================")
                    print(msj.mensaje_monto_excedido("el saldo del cliente"))
                    print("====================================================")
            print(Style.NORMAL + Fore.WHITE)
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
