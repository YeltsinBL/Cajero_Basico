"""Vista para las Operaciones por Cliente Transferir"""
# region importaciones
import Common.Validacion as validacion
import Common.mensaje as mensaje
import Controller.ClienteController as clientecontroller
import Controller.transferencia_controller as transferenciacontroller
import Controller.dispensador_controller as dispensadorcontroller
# endregion

msj = mensaje.Mensaje()

# region Formulario Transferir
def frm_cliente_transferencia():
    """Consulta de Transferencia"""
    print("================================")
    print(msj.mensaje_frm_registro("transferencia"))
    print("================================")
    vali_codigo_cliente = True
    vali_clave_cliente = True
    vali_codigo_dispensador= True
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
    while vali_codigo_dispensador:
        codigo_dispensador = input("CÓDIGO DISPENSADOR: ")
        vali_codigo_dispensador = not validacion.\
                                    valores_ingresados("código dispensador",codigo_dispensador,1)
        if vali_codigo_dispensador is False:
            existe_dispensador = dispensadorcontroller\
                                .verifica_dispensador_codigo(int(codigo_dispensador))
            if existe_dispensador is False:
                print("===============================")
                print(msj.mensaje_no_existe("código del dispensador"))
                print("===============================")
                print("")
    vali_codigo_cliente_transferencia = True
    vali_codigo_dispensador_transferir = True
    while vali_codigo_cliente_transferencia:
        codigo_cliente_trans = input("CÓDIGO CLIENTE A TRANSFERIR: ")
        vali_codigo_cliente_transferencia = not validacion.\
                                valores_ingresados("código del cliente a transferir",
                                                   codigo_cliente_trans,4)
        if vali_codigo_cliente_transferencia is False:
            existe_clientes = clientecontroller.verifica_cliente_codigo(codigo_cliente_trans)
            if existe_clientes is False:
                print("===============================")
                print(msj.mensaje_no_existe("código del cliente a transferir"))
                print("===============================")
                print("")
    while vali_codigo_dispensador_transferir:
        codigo_dispensador_transferir = input("CÓDIGO DISPENSADOR A TRANSFERIR: ")
        vali_codigo_dispensador_transferir = not validacion.\
                                    valores_ingresados("código dispensador a transferir",
                                                       codigo_dispensador_transferir,1)
        if vali_codigo_dispensador_transferir is False:
            existe_dispensador = dispensadorcontroller\
                                .verifica_dispensador_codigo(int(codigo_dispensador_transferir))
            if existe_dispensador is False:
                print("===============================")
                print(msj.mensaje_no_existe("código del dispensador a transferir"))
                print("===============================")
                print("")
    vali_monto = True
    while vali_monto:
        monto = input("MONTO: ")
        vali_monto = not validacion.valores_ingresados("MONTO",monto,2)
        if vali_monto is False:
            print("====================================================")
            print(msj.mensaje_verificar_monto())
            print("====================================================")
            veri_monto = dispensadorcontroller.verificar_monto_dispensador(
                                        int(codigo_dispensador), float(monto))
            if veri_monto is False:
                print("===============================")
                print(msj.mensaje_monto_excedido())
                print("===============================")
                print("")
                vali_codigo_dispensador = True
                vali_monto = True
    datos = {"codigo_cliente":codigo_cliente, "codigo_dispensador":int(codigo_dispensador),
            "codigo_cliente_transferir":codigo_cliente_trans, 
            "codigo_dispensador_transferir":int(codigo_dispensador_transferir),
            "monto":float(monto)}
    print("===============================")
    print(msj.mensaje_realizando_accion("transferencia"))
    print("===============================")
    resp = transferenciacontroller.registro_transferencia(datos)
    if resp:
        print("======================")
        print(msj.mensaje_registrado("transferencia"))
        print("======================")
        print("")
    else:
        print("======================")
        print(msj.mensaje_error_registrar("transferencia"))
        print("======================")
        print("")
# endregion
