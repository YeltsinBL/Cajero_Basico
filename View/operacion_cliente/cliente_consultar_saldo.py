"""Vista para las Operaciones por Cliente Consultar Saldo"""
# region importaciones
from time import sleep
from colorama import Fore, Style
from Common import mensaje
from Common import elemento
import Controller.ClienteController as clientecontroller
import Controller.cuenta_cliente_controller as cuentaclientecontroller
# endregion

msj = mensaje.Mensaje()

# region Formulario Saldo
def frm_consulta_saldo():
    """Consulta de Saldo"""
    print(Style.BRIGHT + Fore.CYAN)
    print("================================")
    print(msj.mensaje_frm_consultar("saldo"))
    print("================================")
    print(Style.NORMAL + Fore.WHITE)
    opc_accion = opciones_consulta()
    codigo_cuenta =0
    codigo_cliente = elemento.ingresar_codigo_cliente(
        nombre="código del cliente", verificar_cuenta=True, verificar_estado=True)
    if codigo_cliente =="":
        return
    if opc_accion == 1:
        codigo_cuenta = elemento.ingresar_numero_cuenta(
            nombre="nro. cuenta soles", codigo_cliente=codigo_cliente)
        if codigo_cuenta == 0:
            return
    respt = cuentaclientecontroller.buscar_saldo_cuenta_cliente(
                                codigo_cliente,
                                codigo_cuenta)
    if len(respt)>0:
        lista_saldo(respt)
    else:
        error_lista_saldo(codigo_cliente,codigo_cuenta)
def opciones_consulta():
    """Consultar por código o Todos"""
    while True:
        print("Ingresa el número de la acción a realizar:")
        print(1, "Nro. Cuenta Soles")
        print(2, "Todas las Cuentas Soles")
        nro_accion = input("")
        if nro_accion.isdigit() and int(nro_accion) in {1, 2}:
            return int(nro_accion)
        print(Style.BRIGHT + Fore.RED)
        print("===============================")
        print(msj.mensaje_opcion_ingresada_incorrecta())
        print("===============================")
def lista_saldo(respt):
    """Lista de los saldos"""
    print(Style.BRIGHT + Fore.CYAN)
    print("============================")
    print(msj.mensaje_frm_lista("saldos"))
    print("============================")
    print(Style.NORMAL + Fore.WHITE)
    for deposito in respt:
        respt_cliente = clientecontroller.buscar_cliente_codigo(deposito.codigo_cliente)
        cuenta_cliente = cuentaclientecontroller.buscar_saldo_cuenta_cliente(
                            deposito.codigo_cliente)
        for cuenta in cuenta_cliente:
            print("CLIENTE:",deposito.codigo_cliente, "-", respt_cliente.nombre)
            print("NRO. CUENTA SOLES:", cuenta.codigo_cuenta)
            print("TOTAL:", cuenta.monto)
            print("============================")
    print(Style.BRIGHT + Fore.GREEN)
    print("============================")
    print(msj.mensaje_existe("saldo"))
    print("============================")
def error_lista_saldo(codigo_cliente,codigo_dispensador):
    """Error al listar los saldos"""
    print(Style.BRIGHT + Fore.RED)
    print("===========================================")
    print(msj.mensaje_error_al("consultar","saldo"))
    print("===========================================")
    sleep(1)
    existe_cliente = cuentaclientecontroller\
            .buscar_saldo_cuenta_cliente(codigo_cliente)
    if len(existe_cliente)>0:
        existe_dis = False
        for valor in existe_cliente:
            if valor.codigo_dispensador != int(codigo_dispensador):
                existe_dis = True
        if existe_dis:
            print(msj.mensaje_no_tiene("cliente", "cuenta en este dispensador"))
            print("===========================================")
        else: pass
    else:
        print(msj.mensaje_no_esta("la cuenta","activa"))
        print("===============================")
        sleep(1)
        print(msj.mensaje_no_tiene("cliente", "depósito"))
        print("===============================")

# endregion
