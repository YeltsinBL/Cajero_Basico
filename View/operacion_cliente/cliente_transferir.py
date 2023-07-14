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
                mensaje_codigo_cliente("código del cliente")
    cont = 0
    while vali_clave_cliente:
        clave = input("CLAVE CLIENTE: ")
        vali_clave_cliente = not clientecontroller.\
            verifica_cliente_codigo_clave(codigo_cliente, clave)
        if vali_clave_cliente:
            cont +=1
            mensaje_clave_cliente("clave", cont)
            if cont == 3:
                return
    while vali_codigo_dispensador:
        codigo_dispensador = input("CÓDIGO DISPENSADOR: ")
        vali_codigo_dispensador = not validacion.\
                                    valores_ingresados("código dispensador",
                                                       codigo_dispensador,1)
        if vali_codigo_dispensador is False:
            vali_codigo_dispensador = not dispensadorcontroller\
                                            .verifica_dispensador_codigo(int(codigo_dispensador))
            if vali_codigo_dispensador:
                mensaje_codigo_dispensador("código del dispensador")
            else:
                existe_cliente = cuentaclientecontroller\
                        .buscar_saldo_cuenta_cliente(codigo_cliente)
                if len(existe_cliente)>0:
                    vali_codigo_dispensador = mensaje_relacion_cliente_dispensador(
                                            codigo_dispensador, existe_cliente)
                    if vali_codigo_dispensador:
                        return
                else:
                    mensaje_cuenta_activa("cliente", "depósito")
                    return
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
                mensaje_codigo_cliente("código del cliente a transferir")
            #else:
    while vali_codigo_dispensador_transferir:
        codigo_dispensador_transferir = input("CÓDIGO DISPENSADOR A TRANSFERIR: ")
        vali_codigo_dispensador_transferir = not validacion.\
                                            valores_ingresados("código dispensador a transferir",
                                                                codigo_dispensador_transferir,1)
        if vali_codigo_dispensador_transferir is False:
            vali_codigo_dispensador_transferir = not dispensadorcontroller\
                                    .verifica_dispensador_codigo(int(codigo_dispensador_transferir))
            if vali_codigo_dispensador_transferir:
                mensaje_codigo_dispensador("código del dispensador a transferir")
            else:
                existe_cliente = cuentaclientecontroller\
                        .buscar_saldo_cuenta_cliente(codigo_cliente_trans)
                if len(existe_cliente)>0:
                    vali_codigo_dispensador = mensaje_relacion_cliente_dispensador(
                                        codigo_dispensador_transferir, existe_cliente)
                    if vali_codigo_dispensador:
                        return
                else:
                    mensaje_cuenta_activa("cliente a transferir", "depósito")
                    return
        if codigo_cliente==codigo_cliente_trans and\
            codigo_dispensador==codigo_dispensador_transferir:
            mensaje_transferir_misma_cuenta()
            return
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
                monto_vali = cuentaclientecontroller.verificar_cuenta_cliente(
                                        codigo_cliente, int(codigo_dispensador))
                if monto_vali ==0:
                    print(Style.BRIGHT + Fore.RED)
                    print("====================================================")
                    print(msj.mensaje_no_tiene("cliente", "saldo en su cuenta"))
                    print("====================================================")
                    return
                if monto_vali < float(monto):
                    print(Style.BRIGHT + Fore.RED)
                    print("====================================================")
                    print(msj.mensaje_monto_excedido("el saldo del cliente"))
                    print("====================================================")
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
def mensaje_codigo_cliente(msj_codigo_cliente):
    """mensaje el código del cliente"""
    print(Style.BRIGHT + Fore.RED)
    print("===============================")
    print(msj.mensaje_no_existe(msj_codigo_cliente))
    print("===============================")
    print(Style.NORMAL + Fore.WHITE)
def mensaje_clave_cliente(msj_clave_cliente, contador):
    """mensaje la clave del cliente"""
    print(Style.BRIGHT + Fore.RED)
    print("===================================")
    print(msj.mensaje_clave_incorrecta(msj_clave_cliente))
    print("===================================")
    intent = lambda cont : "intento" if(3-contador == 1) else "intentos"
    print(f"LE QUEDA {3 - contador}", intent(contador).upper())
    print("===================================")
    print(Style.NORMAL + Fore.WHITE)
def mensaje_codigo_dispensador(msj_codigo_dispensador):
    """mensaje el código del dispensador"""
    print(Style.BRIGHT + Fore.RED)
    print("===============================")
    print(msj.mensaje_no_existe(msj_codigo_dispensador))
    print("===============================")
    print(Style.NORMAL + Fore.WHITE)
def mensaje_relacion_cliente_dispensador(codigo_dispensador,existe_cliente):
    """mensaje si el cliente tiene depósito en el dispensador"""
    existe_dis = False
    for valor in existe_cliente:
        if valor.codigo_dispensador != int(codigo_dispensador):
            existe_dis = True
    if existe_dis:
        print(Style.BRIGHT + Fore.RED)
        print("===========================================")
        print(msj.mensaje_no_tiene("cliente", "cuenta en este dispensador"))
        print("===========================================")
    return existe_dis
def mensaje_cuenta_activa(nombre, detalle):
    """mensaje si la cuenta esta activa"""
    print(Style.BRIGHT + Fore.RED)
    print("===============================")
    print(msj.mensaje_cuenta_no_activa())
    print("===============================")
    sleep(1)
    print(msj.mensaje_no_tiene(nombre, detalle))
    print("===============================")
def mensaje_transferir_misma_cuenta():
    """Mensaje: No se puede transferir a la misma cuenta"""
    print(Style.BRIGHT + Fore.RED)
    print("===============================")
    print(msj.mensaje_transferencia_codigo_iguales())
    print("===============================")
    print(Style.NORMAL + Fore.WHITE)
# endregion
