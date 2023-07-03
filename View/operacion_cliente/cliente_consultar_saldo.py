"""Vista para las Operaciones por Cliente Consultar Saldo"""
# region importaciones
from time import sleep
from colorama import Fore, Style
import Common.Validacion as validacion
import Common.mensaje as mensaje
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
    vali_cod_cliente = True
    codigo_dispensador =0
    while vali_cod_cliente:
        codigo_cliente = input("CÓDIGO CLIENTE: ")
        vali_cod_cliente = not validacion.valores_ingresados("código",codigo_cliente,4)
        if vali_cod_cliente is False:
            cliente = clientecontroller.buscar_cliente_codigo(codigo_cliente)
            if isinstance(cliente,list):
                print(Style.BRIGHT + Fore.RED)
                print("============================")
                print(msj.mensaje_no_existe("código del cliente"))
                print("============================")
                vali_cod_cliente = True
                break
    if  vali_cod_cliente is False:
        if opc_accion == 1:
            vali_cod_dispensador = True
            while vali_cod_dispensador:
                codigo_dispensador = input("CÓDIGO DISPENSADOR: ")
                vali_cod_dispensador = not validacion.valores_ingresados("código",
                                                                         codigo_dispensador,1)
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
                existe_dis = True
                for valor in existe_cliente:
                   # existe_dis = valor.codigo_dispensador != int(codigo_dispensador)
                    if valor.codigo_dispensador != int(codigo_dispensador):
                        existe_dis = True
                    else: existe_dis = False
                if existe_dis:
                    print(msj.mensaje_no_tiene("cliente", "cuenta en este dispensador"))
                    print("===========================================")
                else: pass
            else:
                print(msj.mensaje_cuenta_no_activa())
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
