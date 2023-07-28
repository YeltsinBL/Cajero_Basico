"""Gestionar Cliente"""
# region importaciones
from time import sleep
from colorama import Fore, Style
import Common.Validacion as validacion
from Common import mensaje
from Common import elemento
import Controller.ClienteController as clientecontroller
import Controller.MenuController as menucontroller
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
    clave = input("CLAVE: ")
    nrocuentasoles = clientecontroller.registro_cliente({"codigo":codigo, "nombre": nombre,
                                        "clave":clave})
    print(Style.BRIGHT + Fore.GREEN)
    print("======================")
    print(msj.mensaje_registrado("CLIENTE"))
    print("======================")
    print(msj.mensaje_su_numero_cuenta(nrocuentasoles))
    print("======================")

def frm_modificar_cliente():
    """Modificar Cliente"""
    print(Style.BRIGHT + Fore.CYAN)
    print("======================")
    print(msj.mensaje_frm_modifica("CLIENTE"))
    print("======================")
    print(Style.NORMAL + Fore.WHITE)
    datos_cliente:dict[str,any]
    codigo_cliente = elemento.\
                    ingresar_codigo_cliente("código")
    nombre = ingresar_nombre()
    estado = elemento.ingresar_estado("estado")
    if estado==0:
        cliente = clientecontroller.buscar_cliente_codigo(codigo_cliente)
        if cliente[4]>0:
            print(Style.BRIGHT + Fore.RED)
            print("=====================")
            print(msj.mensaje_no_se_puede("desactivar el cliente"))
            print("=====================")
            sleep(1)
            print(msj.mensaje_usted_cuenta("un saldo de",cliente[4]))
            print("=====================")
            return
    datos_cliente = {"codigo":codigo_cliente, "nombre": nombre,
             "estado": estado}
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
    if respt is None:
        print("====================")
        print(msj.mensaje_no_existe("código"))
        print("====================")
    elif not isinstance(respt,list):
        print("NOMBRE:",respt[2])
        print("NRO. CUENTA SOLES:",respt[3])
        print("SALDO:",respt[4])
        print("ESTADO:","Activo" if respt[5] == 1 else "Inactivo")
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
        if len(respt)<=0:
            print(msj.mensaje_no_existe("CÓDIGO"))
            print("================================")
            sleep(1)
            frm_listado_cliente()

def frm_listado_cliente():
    """Listado de los Clientes"""
    clientes = clientecontroller.listado_cliente()
    print(Style.BRIGHT + Fore.CYAN)
    print("=======================")
    print(msj.mensaje_frm_lista("CLIENTES"))
    print("=======================")
    print(Style.BRIGHT + Fore.WHITE)
    for dato in clientes:
        print("CÓDIGO:",dato[1])
        print("NOMBRE:",dato[2])
        print("NRO. CUENTA SOLES:",dato[3])
        print("SALDO:",dato[4])
        print("ESTADO:","Activo" if dato[5] == 1 else "Inactivo")
        print("=======================")
    print(Style.BRIGHT + Fore.GREEN)
    print("=======================")
    print(msj.mensaje_listado("CLIENTES"))
    print("=======================")

def selecciona_estado_cliente(nro_menu):
    """Selecciona el tipo a listar de los Clientes por estado"""
    while True:
        print(Fore.BLUE + Style.BRIGHT)
        print("¡SELECCIONE UN ESTADO!")
        print(Fore.WHITE + Style.NORMAL)
        print("Ingresa el número del estado")
        lista_menu =[]
        nueva_lista={}
        if len(lista_menu)==0:
            lista_menu = menucontroller.listar_menu(nro_menu)
        for resultado in lista_menu:
            print(resultado[0], resultado[1])
            nueva_lista[resultado[0]]=resultado[0]
        nro_menu = int(input(""))
        if nro_menu in list(range(len(lista_menu)+1)):
            return nro_menu
        print(Style.BRIGHT + Fore.RED)
        print("=================================")
        print(msj.mensaje_opcion_ingresada_incorrecta())
        print("=================================")
        print(Style.BRIGHT + Fore.WHITE)

def frm_estado_cliente(nro_menu):
    """Lista de los Clientes por estado"""
    nro_estado = selecciona_estado_cliente(nro_menu)
    if nro_estado == 3:
        return
    estado = "Activo" if nro_estado == 1 else "Inactivo"
    respt = clientecontroller.listado_cliente_estado(
        nro_estado if nro_estado == 1 else 0)
    if len(respt)>0:
        print(Style.BRIGHT + Fore.CYAN)
        print("=================================")
        print(msj.mensaje_frm_listar_estado("CLIENTE", estado.upper()+"S"))
        print("=================================")
        print(Style.BRIGHT + Fore.WHITE)
        for dato in respt:
            print("CÓDIGO:",dato[1])
            print("NOMBRE:",dato[2])
            print("NRO. CUENTA SOLES:",dato[3])
            print("SALDO:",dato[4])
            print("ESTADO:","Activo" if dato[5] == 1 else "Inactivo")
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
