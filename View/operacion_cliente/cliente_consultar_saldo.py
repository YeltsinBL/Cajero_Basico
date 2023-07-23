"""Vista para las Operaciones por Cliente Consultar Saldo"""
# region importaciones
from colorama import Fore, Style
from Common import mensaje
from Common import elemento
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
    codigo_cuenta =""
    codigo_cliente = elemento.ingresar_codigo_cliente(
        nombre="código del cliente", verificar_cuenta=True, verificar_estado=True)
    if codigo_cliente =="":
        return
    if opc_accion == 1:
        codigo_cuenta = elemento.ingresar_numero_cuenta(
            nombre="nro. cuenta soles", codigo_cliente=codigo_cliente)
        if codigo_cuenta == "":
            return
    respt = cuentaclientecontroller.buscar_saldo_cuenta_cliente(
                                codigo_cliente,
                                codigo_cuenta)
    lista_saldo(respt)
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
        print("CLIENTE:",deposito[2], "-", deposito[5])
        print("NRO. CUENTA SOLES:", deposito[1])
        print("TOTAL:", float(deposito[3]))
        print("============================")
    print(Style.BRIGHT + Fore.GREEN)
    print("============================")
    print(msj.mensaje_existe("saldo"))
    print("============================")
# endregion
