"""Elementos Reutilizables"""

from time import sleep
from colorama import Fore, Style
import Common.mensaje as mensaje
import Common.Validacion as validacion
import Controller.ClienteController as clientecontroller
import Controller.dispensador_controller as dispensadorcontroller
import Controller.cuenta_cliente_controller as cuentaclientecontroller

msj = mensaje.Mensaje()

# region Elementos
def ingresar_codigo_cliente(nombre:str, verificar_cuenta=False):
    """Ingresar el codigo del cliente"""
    vali_codigo_cliente = True
    while vali_codigo_cliente:
        codigo_cliente = input(nombre.upper() +": ")
        vali_codigo_cliente = not validacion.\
                                valores_ingresados(nombre,codigo_cliente,4)
        if vali_codigo_cliente is False:
            vali_codigo_cliente = not clientecontroller.verifica_cliente_codigo(codigo_cliente)
            if vali_codigo_cliente:
                mensaje_codigo_cliente(nombre)
            else:
                if verificar_cuenta:
                    existe_cliente = cuentaclientecontroller\
                            .buscar_saldo_cuenta_cliente(codigo_cliente)
                    if len(existe_cliente)==0:
                        mensaje_cuenta_activa(nombre, "depósito")
                        return ""
    return codigo_cliente
def ingresar_clave_cliente(nombre, codigo_cliente):
    """Ingresar la clave del cliente"""
    vali_clave_cliente = True
    cont = 0
    while vali_clave_cliente:
        clave = input(nombre.upper()+": ")
        vali_clave_cliente = not clientecontroller.\
            verifica_cliente_codigo_clave(codigo_cliente, clave)
        if vali_clave_cliente:
            cont +=1
            mensaje_clave_cliente(nombre, cont)
            if cont == 3:
                return False
    return True
def ingresar_codigo_dispensador(nombre,codigo_cliente=0, mensaje_cliente ="cliente",
                                verificar_cuenta=False):
    """Ingresar el código del dispensador"""
    vali_codigo_dispensador= True
    while vali_codigo_dispensador:
        codigo_dispensador = input(nombre.upper()+": ")
        vali_codigo_dispensador = not validacion.\
                            valores_ingresados(nombre, codigo_dispensador,1)
        if vali_codigo_dispensador is False:
            vali_codigo_dispensador = not dispensadorcontroller\
                                    .verifica_dispensador_codigo(int(codigo_dispensador))
            if vali_codigo_dispensador:
                mensaje_codigo_dispensador(nombre)
            else:
                if verificar_cuenta:
                    existe_cliente = cuentaclientecontroller\
                        .buscar_saldo_cuenta_cliente(codigo_cliente)
                    vali_codigo_dispensador = mensaje_relacion_cliente_dispensador(
                                            codigo_dispensador, existe_cliente, mensaje_cliente)
                    if vali_codigo_dispensador:
                        return 0
    return int(codigo_dispensador)
def ingresar_monto(codigo_dispensador,codigo_cliente):
    """Ingresar el monto"""
    vali_monto = True
    while vali_monto:
        monto = input("MONTO: ")
        vali_monto = not validacion.valores_ingresados("MONTO",monto,2)
        if vali_monto is False:
            if int(monto) ==0:
                print(Style.BRIGHT + Fore.RED)
                print("===============================")
                print(msj.mensaje_monto_mayor_cero())
                print("===============================")
                print(Style.BRIGHT + Fore.WHITE)
                vali_monto = True
            else:
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
                    print(Style.NORMAL + Fore.WHITE)
                else:
                    print("====================================================")
                    print(msj.mensaje_verificar_tipo("saldo","la cuenta del cliente"))
                    print("====================================================")
                    sleep(1)
                    monto_vali = cuentaclientecontroller.verificar_cuenta_cliente(
                                            codigo_cliente, int(codigo_dispensador))
                    if monto_vali ==0.0:
                        print(Style.BRIGHT + Fore.RED)
                        print("====================================================")
                        print(msj.mensaje_no_tiene("cliente", "saldo en su cuenta"))
                        print("====================================================")
                        return 0
                    if monto_vali < float(monto):
                        print(Style.BRIGHT + Fore.RED)
                        print("====================================================")
                        print(msj.mensaje_monto_excedido("el saldo del cliente"))
                        print("====================================================")
                        return 0
    return int(monto)
def ingresar_cantidad_billetes():
    """Ingresar cantidad de billetes"""
    vali_bill_200=True
    vali_bill_100=True
    vali_bill_50=True
    vali_bill_20=True
    vali_bill_10=True
    billetes=[]
    print("Cantidad de Billetes")
    while vali_bill_200:
        billete_200 = input("Billetes de 200: ")
        vali_bill_200 = not validacion.valores_ingresados("billetes de 200",billete_200,1)
    while vali_bill_100:
        billete_100 = input("Billetes de 100: ")
        vali_bill_100 = not validacion.valores_ingresados("billetes de 100",billete_100,1)
    while vali_bill_50:
        billete_50 = input("Billetes de 50: ")
        vali_bill_50 = not validacion.valores_ingresados("billetes de 50",billete_50,1)
    while vali_bill_20:
        billete_20 = input("Billetes de 20: ")
        vali_bill_20 = not validacion.valores_ingresados("billetes de 20",billete_20,1)
    while vali_bill_10:
        billete_10 = input("Billetes de 10: ")
        vali_bill_10 = not validacion.valores_ingresados("billetes de 10",billete_10,1)
    billetes.append({200:int(billete_200), 100:int(billete_100), 50:int(billete_50),
                        20:int(billete_20), 10:int(billete_10)})
    return billetes
def ingresar_lugar(nombre):
    """Ingresar el Lugar del Dispensador"""
    vali_lugar = True
    while vali_lugar:
        lugar = input(nombre.upper()+": ")
        vali_lugar = not validacion.valores_ingresados(nombre,lugar,3)
    return lugar
def ingresar_estado(nombre):
    """Ingresar el para el estado"""
    while True:
        print(nombre.upper()+" 1 [Activo]  o 0 [Inactivo] ")
        confirmar = input("INGRESE OPCIÓN: ")
        if confirmar== "1":
            return "activo"
        if confirmar == "0":
            return "desactivo"
        msj.mensaje_opcion_ingresada_incorrecta()
# endregion

# region Mensajes de Validación
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
def mensaje_relacion_cliente_dispensador(codigo_dispensador,existe_cliente,
                                         mensaje_cliente):
    """mensaje si el cliente tiene depósito en el dispensador"""
    existe_dis = False
    for valor in existe_cliente:
        if valor.codigo_dispensador != int(codigo_dispensador):
            existe_dis = True
    if existe_dis:
        print(Style.BRIGHT + Fore.RED)
        print("===========================================")
        print(msj.mensaje_no_tiene(mensaje_cliente, "cuenta en este dispensador"))
        print("===========================================")
    return existe_dis
def mensaje_cuenta_activa(nombre, detalle):
    """mensaje si la cuenta esta activa"""
    print(Style.BRIGHT + Fore.RED)
    print("===============================")
    print(msj.mensaje_cuenta_no_activa())
    print("===============================")
    sleep(1)
    print(msj.mensaje_no_tiene(nombre[11:], detalle))
    print("===============================")
# endregion
