"""Vista para las Operaciones por Cliente Retirar"""
# region importaciones
from time import sleep
from colorama import Fore, Style
from Common import mensaje
from Common import elemento
import Controller.ClienteController as clientecontroller
import Controller.dispensador_controller as dispensadorcontroller
import Controller.retirar_controller as retirocontroller
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
    codigo_dispensador = elemento.ingresar_codigo_dispensador(
            nombre="código del dispensador", verificar_estado=True)
    if codigo_dispensador == 0:
        return
    monto = elemento.ingresar_monto(codigo_cliente, nro_cuenta, codigo_dispensador)
    if monto==float(0):
        return
    respt_cliente = clientecontroller.buscar_cliente_codigo(codigo_cliente)
    respt_dispensador = dispensadorcontroller.\
                        buscar_dispensador_codigo(codigo_dispensador)
    datos = {"codigo_cliente":codigo_cliente, "nombre_cliente":respt_cliente.nombre,
            "codigo_cuenta":nro_cuenta,
            "codigo_dispensador":codigo_dispensador,
            "lugar_dispensador":respt_dispensador.lugar, 
            "estado_dispensador":respt_dispensador.estado, 
            "monto":monto}
    print("============================================")
    print(msj.mensaje_verificar_tipo("billetes","el dispensador"))
    print("============================================")
    print(Style.BRIGHT + Fore.WHITE)
    sleep(1)
    resp = retirocontroller.registro_retiro(datos)
    if isinstance(resp, list) and len(resp)>0:
        detalle_retiro(datos,resp)
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
def detalle_retiro(datos, resp):
    """Verificar el monto del Dispensador"""
    print("CÓDIGO CLIENTE:", datos.get("codigo_cliente"))
    print("NOMBRE CLIENTE:", datos.get("nombre_cliente"))
    print("NRO. CUENTA SOLES:", datos.get("codigo_cuenta"))
    print("CÓDIGO DISPENSADOR:", datos.get("codigo_dispensador"),"-",
                                 datos.get("lugar_dispensador"))
    print("MONTO:", datos.get("monto"))
    print("BILLETES:")
    for dato in resp:
        for nro_billete, vbillete in dato.items():
            print(str(nro_billete)+ ": ",vbillete)
# endregion
