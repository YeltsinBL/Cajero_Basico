"""Vista para las Operaciones por Cliente Retirar"""
# region importaciones
from time import sleep
from colorama import Fore, Style
import Common.Validacion as validacion
import Common.mensaje as mensaje
import Controller.ClienteController as clientecontroller
import Controller.dispensador_controller as dispensadorcontroller
import Controller.retirar_controller as retirocontroller
import Controller.cuenta_cliente_controller as cuentaclientecontroller
# endregion

msj = mensaje.Mensaje()

# region Formulario Retirar
def frm_registrar_retiro():
    """Registrar Retiro"""
    print(Style.BRIGHT + Fore.CYAN)
    print("======================")
    print(msj.mensaje_frm_registro("retiro"))
    print("======================")
    print(Style.NORMAL + Fore.WHITE)
    vali_codigo_cliente = True
    vali_clave_cliente = True
    vali_codigo_dispensador= True
    vali_monto = True
    while vali_codigo_cliente:
        vali_codigo_dispensador= True
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
                print(Style.BRIGHT + Fore.WHITE)
                vali_codigo_dispensador = False
            else:
                cont = 0
                while vali_clave_cliente:
                    vali_codigo_dispensador= True
                    clave = input("CLAVE CLIENTE: ")
                    vali_clave_cliente = not clientecontroller.\
                        verifica_cliente_codigo_clave(codigo_cliente, clave)
                    if vali_clave_cliente:
                        print(Style.BRIGHT + Fore.RED)
                        print("===============================")
                        print(msj.mensaje_clave_incorrecta("clave"))
                        print("===============================")
                        cont +=1
                        if cont == 3:
                            return
                        intent = lambda cont : "intento" if(3-cont == 1) else "intentos"
                        print(f"LE QUEDA {3 - cont}", intent(cont).upper())
                        vali_codigo_dispensador = False
                        print(Style.BRIGHT + Fore.WHITE)
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
                print(Style.BRIGHT + Fore.WHITE)
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
                    print(Style.BRIGHT + Fore.WHITE)
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
    respt_cliente = clientecontroller.buscar_cliente_codigo(codigo_cliente)
    respt_dispensador = dispensadorcontroller.\
                        buscar_dispensador_codigo(int(codigo_dispensador))
    datos = {"codigo_cliente":codigo_cliente, "nombre_cliente":respt_cliente.nombre,
            "codigo_dispensador":int(codigo_dispensador),
            "lugar_dispensador":respt_dispensador.lugar, 
            "estado_dispensador":respt_dispensador.estado, 
            "monto":float(monto)}
    print("============================================")
    print(msj.mensaje_verificar_tipo("billetes","el dispensador"))
    print("============================================")
    print(Style.BRIGHT + Fore.WHITE)
    sleep(1)
    resp = retirocontroller.registro_retiro(datos)
    if isinstance(resp, list) and len(resp)>0:
        detalle_retiro(datos.get("codigo_cliente"), datos.get("nombre_cliente"),
                    datos.get("codigo_dispensador"), datos.get("lugar_dispensador"),
                    datos.get("monto"), resp)
        print(Style.BRIGHT + Fore.GREEN)
        print("======================")
        print(msj.mensaje_registrado("retiro"))
        print("======================")
    elif isinstance(resp, str):
        print(Style.BRIGHT + Fore.RED)
        print("============================================")
        print(msj.mensaje_error_al("registrar","el dispensador"))
        print(msj.mensaje_no_tiene("dispensador",f"suficientes billetes de {resp[:-3]}"))
        print("============================================")
    else:
        print(Style.BRIGHT + Fore.RED)
        print("======================")
        print(msj.mensaje_error_al("registrar","retiro"))
        print("======================")

def detalle_retiro(codigo_cliente,nombre_cliente, codigo_dispensador,
                   lugar_dispensador, monto, datos_retiro:list):
    """Verificar el monto del Dispensador"""
    print("CÓDIGO CLIENTE:", codigo_cliente)
    print("NOMBRE CLIENTE:", nombre_cliente)
    print("CÓDIGO DISPENSADOR:", codigo_dispensador,"-", lugar_dispensador)
    print("MONTO:", monto)
    print("BILLETES:")
    for dato in datos_retiro:
        for nro_billete, vbillete in dato.items():
            print(str(nro_billete)+ ": ",vbillete)
# endregion

# region Mensaje Validación
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
# endregion
