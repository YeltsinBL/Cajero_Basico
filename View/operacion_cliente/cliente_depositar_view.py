"""Vista para las Operaciones por Cliente Depositar"""
# region importaciones
from colorama import Fore, Style
from Common import mensaje
from Common import elemento
import Controller.ClienteController as clientecontroller
import Controller.dispensador_controller as dispensadorcontroller
import Controller.depositar_controller as depositarcontroller
# endregion

msj = mensaje.Mensaje()

# region Formulario Depositar
def frm_registrar_deposito():
    """Registrar Depósito"""
    print(Style.BRIGHT + Fore.CYAN)
    print("======================")
    print(msj.mensaje_frm_registro("depósito"))
    print("======================")
    print(Style.NORMAL + Fore.WHITE)
    codigo_cliente = elemento.ingresar_codigo_cliente(
        nombre="código del cliente", verificar_estado=True)
    if codigo_cliente == "":
        return
    nro_cuenta = elemento.ingresar_numero_cuenta("nro. cuenta soles",codigo_cliente)
    if nro_cuenta=="":
        return
    codigo_dispensador = elemento.ingresar_codigo_dispensador(
        nombre="código del dispensador", verificar_estado=True)
    if codigo_dispensador == 0:
        return
    billetes = elemento.ingresar_cantidad_billetes()
    respt_cliente = clientecontroller.buscar_cliente_codigo(codigo_cliente)
    respt_dispensador = dispensadorcontroller.\
                            buscar_dispensador_codigo(codigo_dispensador)
    for resp in respt_dispensador:
        dato_dispensador = {"codigo_cliente":codigo_cliente,
                            "nombre_cliente":respt_cliente[2],
                            "codigo_cuenta":nro_cuenta,
                            "codigo_dispensador": codigo_dispensador,
                            "lugar_dispensador":resp.get("lugar"),
                            "estado_dispensador":resp.get("estado"),
                            "billete":billetes}
    respt= vista_previa_registro(dato_dispensador)
    if respt:
        dato_dispensador["monto"] = float(respt)
        respt2 = depositarcontroller.registro_deposito(dato_dispensador)
        if respt2:
            print(Style.BRIGHT + Fore.GREEN)
            print("======================")
            print(msj.mensaje_registrado("depósito"))
            print("======================")
        else:
            print(Style.BRIGHT + Fore.RED)
            print("======================")
            print(msj.mensaje_error_al("registrar","depósito"))
            print("======================")
    else:
        print(Style.BRIGHT + Fore.YELLOW)
        print("======================")
        print(msj.mensaje_cancelar_confirmacion("depósito"))
        print("======================")

def vista_previa_registro(datos_depositar:dict[str,any]):
    """Vista previa al registrar"""
    total=0
    print(Style.BRIGHT + Fore.YELLOW)
    print("===========================")
    print(msj.mensaje_frm_vista_previa("depósito"))
    print("===========================")
    print(Style.BRIGHT + Fore.WHITE)
    print("CLIENTE:",datos_depositar.get("nombre_cliente"))
    print("NRO. CUENTA SOLES:",datos_depositar.get("codigo_cuenta"))
    print("DISPENSADOR:",datos_depositar.get("codigo_dispensador"),"-",
          datos_depositar.get("lugar_dispensador"))
    print("CANTIDAD DE BILLETES:")
    for valor in datos_depositar.get("billete"):
        for nro_billete, vbillete in valor.items():
            print(str(nro_billete)+ ": ",vbillete)
            total = total + (int(nro_billete)* vbillete)
    print("TOTAL:", total)
    print("===========================")
    while True:
        print("¿CONFIRMAR DEPÓSITO? 1 [SI]  o 0 [NO] ")
        confirmar = input("INGRESE OPCIÓN: ")
        if confirmar== "1":
            return int(total)
        if confirmar == "0":
            return 0
        msj.mensaje_opcion_ingresada_incorrecta()

# endregion
