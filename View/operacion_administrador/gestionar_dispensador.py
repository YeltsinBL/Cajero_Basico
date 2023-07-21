"""Gestionar Dispensador"""

# region importaciones
from time import sleep
from colorama import Fore, Style
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
        {"codigo":cant_disp+1,"lugar":lugar, "billete": billetes,"estado": 1})
    print(Style.BRIGHT + Fore.GREEN)
    print("============================")
    print(msj.mensaje_registrado("DISPENSADOR"))
    print("============================")

def frm_listado_dispensadores():
    """Listar los Dispensadores"""
    dispensa = dispensadorcontroller.listado_dispensador()
    print(Style.BRIGHT + Fore.CYAN)
    print("============================")
    print(msj.mensaje_frm_lista("DISPENSADORES"))
    print("============================")
    print(Style.NORMAL + Fore.WHITE)
    for dato in dispensa:
        print("CODIGO:", dato.get("codigo"))
        print("LUGAR:", dato.get("lugar"))
        print("BILLETES:")
        for valor in dato.get("billete"):
            for nro_billete, vbillete in valor.items():
                print(str(nro_billete).upper()+ ": ",vbillete)
        print("ESTADO:", "Activo" if dato.get("estado") else "Inactivo")
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
                    "billete": billetes,"estado": estado}
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
    result = dispensadorcontroller.buscar_dispensador_codigo(int(codigo_dispensador))
    if len(result)>0:
        for respt in result:
            print("LUGAR:",respt.get("lugar"))
            print("BILLETES:")
            for valor in respt.get("billete"):
                for nro_billete, vbillete in valor.items():
                    print(str(nro_billete).upper()+ ": ",vbillete)
            print("ESTADO:","Activo" if respt.get("estado") else "Inactivo")
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
    estado = "Activo" if nro_estado == 1 else "Inactivo"
    respt = dispensadorcontroller.listado_dispensador_estado(
        nro_estado if nro_estado == 1 else 0)
    if len(respt)>0:
        print(Style.BRIGHT + Fore.CYAN)
        print("=====================================")
        print(msj.mensaje_frm_listar_estado("DISPENSADOR", estado.upper()+"S"))
        print("=====================================")
        print(Style.BRIGHT + Fore.WHITE)
        for dato in respt:
            print("CÓDIGO:",dato.codigo)
            print("LUGAR:",dato.lugar)
            print("BILLETES:")
            for valor in dato.billete:
                for nro_billete, vbillete in valor.items():
                    print(str(nro_billete).upper()+ ": ",vbillete)
            print("ESTADO:",estado)
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
    while True:
        print(Fore.BLUE + Style.BRIGHT)
        print("¡SELECCIONE UN ESTADO!")
        print(Fore.WHITE + Style.NORMAL)
        print("Ingresa el número del estado")
        operacioncontroller.listado_estados_clientes()
        nro_menu = int(input(""))
        if nro_menu in [3,2,1]:
            return nro_menu
        print(Style.BRIGHT + Fore.RED)
        print("=================================")
        print(msj.mensaje_opcion_ingresada_incorrecta())
        print("=================================")
        print(Style.BRIGHT + Fore.WHITE)
