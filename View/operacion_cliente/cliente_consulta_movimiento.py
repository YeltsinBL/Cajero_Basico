"""Vista para las Operaciones por Cliente Consultar Movimiento"""
# region importaciones
import Common.Validacion as validacion
import Common.mensaje as mensaje
import Controller.ClienteController as clientecontroller
import Controller.depositar_controller as depositocontroller
import Controller.retirar_controller as retirocontroller
import Controller.dispensador_controller as dispensadorcontroller
# endregion

msj = mensaje.Mensaje()

# region Formulario Consulta
def frm_consulta_movimiento():
    """Consulta de Movimiento"""
    print("================================")
    print(msj.mensaje_frm_consultar("movimiento"))
    print("================================")
    vali_codigo_cliente = True
    vali_clave_cliente = True
    while vali_codigo_cliente:
        codigo_cliente = input("CÓDIGO CLIENTE: ")
        vali_codigo_cliente = not validacion.\
                                valores_ingresados("código del cliente",codigo_cliente,4)
        if vali_codigo_cliente is False:
            existe_clientes = clientecontroller.verifica_cliente_codigo(codigo_cliente)
            if existe_clientes is False:
                print("===============================")
                print(msj.mensaje_no_existe("código del cliente"))
                print("===============================")
                print("")
            else:
                cont = 0
                while vali_clave_cliente:
                    clave = input("CLAVE CLIENTE: ")
                    existe_clave_cliente = clientecontroller.\
                        verifica_cliente_codigo_clave(codigo_cliente, clave)
                    vali_clave_cliente = False
                    if existe_clave_cliente is False:
                        print("===============================")
                        print(msj.mensaje_clave_incorrecta("clave"))
                        print("===============================")
                        print("")
                        cont +=1
                        if cont == 3:
                            vali_clave_cliente = False
                            return
                        intent = lambda cont : "intento" if(3-cont == 1) else "intentos"
                        print(f"LE QUEDA {3 - cont}", intent(cont).upper())
                        vali_clave_cliente = True
    resp_deposito = depositocontroller.buscar_deposito_codigo(codigo_cliente,0)
    if len(resp_deposito)>0:
        total = 0
        print("============================")
        print(msj.mensaje_listado("depósitos"))
        print("============================")
        for deposito in resp_deposito:
            respt_cliente = clientecontroller.buscar_cliente_codigo(deposito.codigo_cliente)
            respt_dispensador = dispensadorcontroller.\
                        buscar_dispensador_codigo(int(deposito.codigo_dispensador))
            print("CLIENTE:",deposito.codigo_cliente, "-", respt_cliente.nombre)
            print("DISPENSADOR:",deposito.codigo_dispensador, "-", respt_dispensador.lugar)
            print("CANTIDAD DE BILLETES:")
            for valor in deposito.billete:
                for nro_billete, vbillete in valor.items():
                    print(str(nro_billete)+ ": ",vbillete)
                    total = total + (int(nro_billete)* vbillete)
            print("TOTAL:", total)
            print("============================")
    else:
        print("===========================================")
        print(msj.mensaje_no_existe_lista("depósito"))
        print("===========================================")
    resp_retiro = retirocontroller.buscar_retiro(codigo_cliente)
    if len(resp_retiro)>0:
        print(msj.mensaje_listado("retiros"))
        print("============================")
        for retiro in resp_retiro:
            respt_cliente = clientecontroller.buscar_cliente_codigo(retiro.codigo_cliente)
            respt_dispensador = dispensadorcontroller.\
                        buscar_dispensador_codigo(int(retiro.codigo_dispensador))
            print("CLIENTE:",retiro.codigo_cliente, "-", respt_cliente.nombre)
            print("DISPENSADOR:",retiro.codigo_dispensador, "-", respt_dispensador.lugar)
            print("MONTO:", retiro.monto)
            print("============================")
    else:
        print("===========================================")
        print(msj.mensaje_no_existe_lista("retiro"))
        print("===========================================")
    print("")

# endregion
