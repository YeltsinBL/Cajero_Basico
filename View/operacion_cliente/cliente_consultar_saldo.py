"""Vista para las Operaciones por Cliente Consultar Saldo"""
# region importaciones
from time import sleep
from colorama import Fore, Style
import Common.Validacion as validacion
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
    codigo_dispensador =0
    codigo_cliente = elemento.ingresar_codigo_cliente(
        nombre="código del cliente", verificar_cuenta=True, verificar_estado=True)
    if codigo_cliente =="":
        return
    if opc_accion == 1:
        codigo_dispensador = elemento.ingresar_codigo_dispensador(
            nombre="código del dispensador", codigo_cliente=codigo_cliente, verificar_cuenta=True)
        if codigo_dispensador == 0:
            return
    respt = cuentaclientecontroller.buscar_saldo_cuenta_cliente(
                                codigo_cliente,
                                int(codigo_dispensador))
    if len(respt)>0:
        print(Style.BRIGHT + Fore.CYAN)
        print("============================")
        print(msj.mensaje_frm_lista("saldos"))
        print("============================")
        print(Style.NORMAL + Fore.WHITE)
        for deposito in respt:
            respt_cliente = clientecontroller.buscar_cliente_codigo(deposito.codigo_cliente)
            print("CLIENTE:",deposito.codigo_cliente, "-", respt_cliente.nombre)
            print("NUMERO CUENTA:",respt_cliente.nrocuentasoles)
            print("TOTAL:", deposito.monto)
            print("============================")
        print(Style.BRIGHT + Fore.GREEN)
        print("============================")
        print(msj.mensaje_existe("saldo"))
        print("============================")
    else:
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
def opciones_consulta():
    """Consultar por código o Todos"""
    inicio = True
    cont = 0
    while inicio:
        try:
            print("Ingresa el número de la acción a realizar:")
            print(1, "Código Dispensador")
            print(2, "Todos los Dispensadores")
            nro_accion = int(input(""))
            if nro_accion == 2 or nro_accion == 1:
                return nro_accion
            else:
                cont += 1
                inicio = validacion.mensaje_validacion(cont)
                continue
        except (ValueError, TypeError):
            cont +=1
            inicio = validacion.mensaje_validacion(cont)

# endregion
