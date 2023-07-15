"""Gestionar Cliente"""
# region importaciones
from time import sleep
from colorama import Fore, Style
import Common.Validacion as validacion
from Common import mensaje
from Common import elemento
import Controller.ClienteController as clientecontroller
import Controller.OperacionController as operacioncontroller
# endregion

msj = mensaje.Mensaje()

# region Formulario Cliente
def frm_registrar_cliente():
    """Registro de Clientes"""
    print(Style.BRIGHT + Fore.CYAN)
    print("======================")
    print(msj.mensaje_frm_registro("CLIENTE"))
    print("======================")
    print(Style.NORMAL + Fore.WHITE)
    codigo = ingresar_codigo()
    nombre = ingresar_nombre()
    nrocuentasoles = ingresar_numero_cuenta()
    clave = input("CLAVE: ")
    clientecontroller.registro_cliente({"codigo":codigo, "nombre": nombre,
                                        "nrocuentasoles": int(nrocuentasoles),
                                        "clave":clave, "estado": "Activo"})
    print(Style.BRIGHT + Fore.GREEN)
    print("======================")
    print(msj.mensaje_registrado("CLIENTE"))
    print("======================")

def frm_modificar_cliente():
    """Modificar Cliente"""
    datos_cliente:dict[str,any]
    codigo_cliente = elemento.\
                    ingresar_codigo_cliente("código")
    nombre = ingresar_nombre()
    nrocuentasoles = ingresar_numero_cuenta()
    estado = elemento.ingresar_estado("estado")
    datos_cliente = {"codigo":codigo_cliente, "nombre": nombre,
             "nrocuentasoles": int(nrocuentasoles), "estado": estado.capitalize()}
    respt= clientecontroller.modificar_cliente(datos_cliente)
    if respt:
        print(Style.BRIGHT + Fore.GREEN)
        print("=====================")
        print(msj.mensaje_modificar("CLIENTE"))
        print("=====================")
    else:
        print(Style.BRIGHT + Fore.RED)
        print("=====================")
        print(msj.mensaje_error_al("modificar","CLIENTE"))
        print("=====================")

def frm_buscar_cliente():
    """Función para Buscar un cliente por su código"""
    print(Style.BRIGHT + Fore.CYAN)
    print("===========================")
    print(msj.mensaje_frm_buscar("CLIENTE"))
    print("===========================")
    print(Style.NORMAL + Fore.WHITE)
    codigo_cliente = elemento.\
                    ingresar_codigo_cliente("código")
    respt = clientecontroller.buscar_cliente_codigo(codigo_cliente)
    if not isinstance(respt,list):
        print("NOMBRE:",respt.nombre)
        print("NRO. CUENTA SOLES:",respt.nrocuentasoles)
        print("SALDO:",respt.saldo)
        print("ESTADO:",respt.estado)
        print(Style.BRIGHT + Fore.GREEN)
        print("====================")
        print(msj.mensaje_existe("CLIENTE"))
        print("====================")
    else:
        print(Style.BRIGHT + Fore.RED)
        print("====================================")
        print(msj.mensaje_error_al("buscar","CLIENTE"))
        print("====================================")
        sleep(1)
        existe_clientes = clientecontroller.verifica_cliente_codigo(codigo_cliente)
        if not existe_clientes:
            print(msj.mensaje_no_existe("CÓDIGO"))
            print("================================")
            sleep(1)
            frm_listado_cliente()

def frm_listado_cliente():
    """Listado de los Clientes"""
    clientes = clientecontroller.listado_cliente()
    cantidad = 0
    print(Style.BRIGHT + Fore.CYAN)
    print("=======================")
    print(msj.mensaje_frm_lista("CLIENTES"))
    print("=======================")
    print(Style.BRIGHT + Fore.WHITE)
    for dato in clientes:
        cantidad += 1
        print(f"CLIENTE NRO. {cantidad}")
        print("CÓDIGO:",dato.codigo)
        print("NOMBRE:",dato.nombre)
        print("NRO. CUENTA SOLES:",dato.nrocuentasoles)
        print("SALDO:",dato.saldo)
        print("ESTADO:",dato.estado)
        print("=======================")
    print(Style.BRIGHT + Fore.GREEN)
    print("=======================")
    print(msj.mensaje_listado("CLIENTES"))
    print("=======================")

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

def frm_estado_cliente():
    """Lista de los Clientes por estado"""
    nro_estado = selecciona_estado_cliente()
    if nro_estado == 3:
        return
    estado = "activo" if nro_estado == 1 else "desactivo"
    respt = clientecontroller.listado_cliente_estado(estado)
    if len(respt)>0:
        cantidad = 0
        print(Style.BRIGHT + Fore.CYAN)
        print("=================================")
        print(msj.mensaje_frm_listar_estado("CLIENTE", estado.upper()+"S"))
        print("=================================")
        print(Style.BRIGHT + Fore.WHITE)
        for dato in respt:
            cantidad += 1
            print(f"CLIENTE NRO. {cantidad}")
            print("CÓDIGO:",dato.codigo)
            print("NOMBRE:",dato.nombre)
            print("NRO. CUENTA SOLES:",dato.nrocuentasoles)
            print("SALDO:",dato.saldo)
            print("ESTADO:",dato.estado)
            print("===============================")
        print(Style.BRIGHT + Fore.GREEN)
        print("===============================")
        print(msj.mensaje_encontro_por_estado("CLIENTES", estado.upper()+"S"))
        print("===============================")
    else:
        print(Style.BRIGHT + Fore.YELLOW)
        print("============================")
        print(msj.mensaje_no_encontro_por_estado("CLIENTES", estado.upper()+"S"))
        print("============================")
        print("")

# endregion

# region Ingresar Elementos

def ingresar_codigo():
    """Ingresar el código del cliente"""
    vali_cod = True
    while vali_cod:
        codigo = input("CÓDIGO: ")
        vali_cod = not validacion.valores_ingresados("código",codigo,4)
    return codigo
def ingresar_nombre():
    """Ingresar el nombre del cliente"""
    vali_nom= True
    while vali_nom:
        nombre = input("NOMBRE: ")
        vali_nom = not validacion.valores_ingresados("nombre",nombre,3)
    return nombre
def ingresar_numero_cuenta():
    """Ingresar el número de la cuenta del cliente"""
    vali_nrocta= True
    while vali_nrocta:
        nrocuentasoles = input("NRO CUENTA SOLES: ")
        vali_nrocta = not validacion.valores_ingresados("nro cuenta soles",nrocuentasoles,1)
    return nrocuentasoles

# endregion