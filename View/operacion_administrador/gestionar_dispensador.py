"""Gestionar Dispensador"""

# region importaciones
from time import sleep
from colorama import Fore, Style
import Common.Validacion as validacion
from Common import mensaje
from Common import elemento
import Controller.dispensador_controller as dispensadorcontroller
import Controller.OperacionController as operacioncontroller
# endregion

msj = mensaje.Mensaje()

# region Formulario DISPENSADOR
def frm_agregar_dispensador():
    """Registrar Dispensador"""
    print(Style.BRIGHT + Fore.CYAN)
    print("============================")
    print(msj.mensaje_frm_registro("DISPENSADOR"))
    print("============================")
    print(Style.NORMAL + Fore.WHITE)
    cant_disp= len(dispensadorcontroller.listado_dispensador())
    lugar = elemento.ingresar_lugar("lugar")
    billetes = elemento.ingresar_cantidad_billetes()
    dispensadorcontroller.registro_dispensador(
        {"codigo":cant_disp+1,"lugar":lugar, "billete": billetes,"estado": "Activo"})
    print(Style.BRIGHT + Fore.GREEN)
    print("============================")
    print(msj.mensaje_registrado("DISPENSADOR"))
    print("============================")

def frm_listado_dispensadores():
    """Listar los Dispensadores"""
    dispensa = dispensadorcontroller.listado_dispensador()
    cantidad = 0
    print(Style.BRIGHT + Fore.CYAN)
    print("============================")
    print(msj.mensaje_frm_lista("DISPENSADORES"))
    print("============================")
    print(Style.NORMAL + Fore.WHITE)
    for dato in dispensa:
        cantidad += 1
        print(f"DISPENSADOR NRO. {cantidad}")
        print("CODIGO:", dato.codigo)
        print("LUGAR:", dato.lugar)
        print("BILLETES:")
        for valor in dato.billete:
            for nro_billete, vbillete in valor.items():
                print(str(nro_billete).upper()+ ": ",vbillete)
        print("ESTADO:", dato.estado)
        print("============================")
    print(Style.BRIGHT + Fore.GREEN)
    print("============================")
    print(msj.mensaje_listado("DISPENSADORES"))
    print("============================")

def frm_modificar_dispensador():
    """Modififcar Dispensdaor"""
    datos_dispensador:dict[str,any]
    print(Style.BRIGHT + Fore.CYAN)
    print("============================")
    print(msj.mensaje_frm_modifica("DISPENSADOR"))
    print("============================")
    print(Style.NORMAL + Fore.WHITE)
    codigo_dispensador = elemento.\
                    ingresar_codigo_dispensador(nombre="código del dispensador")
    lugar = elemento.ingresar_lugar("nuevo lugar")
    billetes = elemento.ingresar_cantidad_billetes()
    estado = elemento.ingresar_estado("nuevo estado")
    datos_dispensador={"codigo":int(codigo_dispensador),"lugar":lugar,
                    "billete": billetes,"estado": estado.capitalize()}
    respt = dispensadorcontroller.modificar_dispensador(datos_dispensador)
    if respt:
        print(Style.BRIGHT + Fore.GREEN)
        print("============================")
        print(msj.mensaje_modificar("DISPENSADOR"))
        print("============================")
    else:
        print(Style.BRIGHT + Fore.RED)
        print("============================")
        print(msj.mensaje_error_al("modificar","DISPENSADOR"))
        print("============================")

def frm_buscar_dispensador():
    """Buscar Dispensador por Código"""
    print(Style.BRIGHT + Fore.CYAN)
    print("================================")
    print(msj.mensaje_frm_buscar("DISPENSADOR"))
    print("================================")
    print(Style.NORMAL + Fore.WHITE)
    codigo_dispensador = elemento.\
                    ingresar_codigo_dispensador(nombre="código del dispensador")
    respt = dispensadorcontroller.buscar_dispensador_codigo(int(codigo_dispensador))
    if not isinstance(respt,list):
        print("LUGAR:",respt.lugar)
        print("BILLETES:")
        for valor in respt.billete:
            for nro_billete, vbillete in valor.items():
                print(str(nro_billete).upper()+ ": ",vbillete)
        print("ESTADO:",respt.estado)
        print(Style.BRIGHT + Fore.GREEN)
        print("============================")
        print(msj.mensaje_existe("DISPENSADOR"))
        print("============================")
    else:
        print(Style.BRIGHT + Fore.RED)
        print("===========================================")
        print(msj.mensaje_error_al("buscar","DISPENSADOR"))
        print("===========================================")
        sleep(1)
        existe_dispensador = dispensadorcontroller.\
                                verifica_dispensador_codigo(int(codigo_dispensador))
        if not existe_dispensador:
            print(msj.mensaje_no_existe("CÓDIGO"))
            print("===============================")
            sleep(1)
            frm_listado_dispensadores()

def frm_estado_dispensador():
    """Lista de los Dispensadores por estado"""
    nro_estado = selecciona_estado_cliente()
    if nro_estado == 3:
        return
    estado = "activo" if nro_estado == 1 else "desactivo"
    respt = dispensadorcontroller.listado_dispensador_estado(estado)
    if len(respt)>0:
        cantidad = 0
        print(Style.BRIGHT + Fore.CYAN)
        print("=====================================")
        print(msj.mensaje_frm_listar_estado("DISPENSADOR", estado.upper()+"S"))
        print("=====================================")
        print(Style.BRIGHT + Fore.WHITE)
        for dato in respt:
            cantidad += 1
            print(f"DISPENSADOR NRO. {cantidad}")
            print("CÓDIGO:",dato.codigo)
            print("LUGAR:",dato.lugar)
            print("BILLETES:")
            for valor in dato.billete:
                for nro_billete, vbillete in valor.items():
                    print(str(nro_billete).upper()+ ": ",vbillete)
            print("ESTADO:",dato.estado)
            print("====================================")
        print(Style.BRIGHT + Fore.GREEN)
        print("====================================")
        print(msj.mensaje_encontro_por_estado("DISPENSADORES", estado.upper()+"S"))
        print("====================================")
    else:
        print(Style.BRIGHT + Fore.YELLOW)
        print("==================================")
        print(msj.mensaje_no_encontro_por_estado("DISPENSADORES", estado.upper()+"S"))
        print("==================================")
#endregion

def selecciona_estado_cliente():
    """Selecciona el tipo a listar de los Clientes por estado"""
    inicio = True
    cont = 0
    while inicio:
        try:
            print()
            print("Ingresa el número del estado")
            operacioncontroller.listado_estados_clientes()
            nro_menu = int(input(""))
            if 3 < nro_menu or nro_menu < 1:
                cont += 1
                inicio = validacion.mensaje_validacion(cont)
                continue
            return nro_menu
        except (ValueError, TypeError):
            cont += 1
            validacion.mensaje_validacion(cont)
