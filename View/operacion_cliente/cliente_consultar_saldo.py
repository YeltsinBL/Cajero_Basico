"""Vista para las Operaciones por Cliente Consultar Saldo"""
# region importaciones
import Common.Validacion as validacion
import Common.mensaje as mensaje
import Controller.ClienteController as clientecontroller
import Controller.dispensador_controller as dispensadorcontroller
import Controller.depositar_controller as depositarcontroller
# endregion

msj = mensaje.Mensaje()

# region Formulario Saldo
def frm_consulta_saldo():
    """Consulta de Saldo"""
    print("================================")
    print(msj.mensaje_frm_consultar("saldo"))
    print("================================")
    opc_accion = opciones_consulta()
    vali_cod_cliente = True
    codigo_dispensador =0
    while vali_cod_cliente:
        codigo_cliente = input("CÓDIGO CLIENTE: ")
        vali_cod_cliente = not validacion.valores_ingresados("código",codigo_cliente,4)
    if opc_accion == 1:
        vali_cod_dispensador = True
        while vali_cod_dispensador:
            codigo_dispensador = input("CÓDIGO DISPENSADOR: ")
            vali_cod_dispensador = not validacion.valores_ingresados("código",codigo_dispensador,1)
    respt = depositarcontroller.buscar_deposito_codigo(codigo_cliente, int(codigo_dispensador))
    #total = 0
    # Realizar la verificacion por códigos separados
    if len(respt)>0:
        print("============================")
        for deposito in respt:
            respt_cliente = clientecontroller.buscar_cliente_codigo(deposito.codigo_cliente)
            respt_dispensador = dispensadorcontroller.\
                        buscar_dispensador_codigo(int(deposito.codigo_dispensador))
            print("CLIENTE:",deposito.codigo_cliente, "-", respt_cliente.nombre)
            print("DISPENSADOR:",deposito.codigo_dispensador, "-", respt_dispensador.lugar)
            # print("CANTIDAD DE BILLETES:")
            # for valor in deposito.billete:
            #     for nro_billete, vbillete in valor.items():
            #         print(str(nro_billete)+ ": ",vbillete)
            #         total = total + (int(nro_billete)* vbillete)
            print("TOTAL:", deposito.monto)
            print("============================")
        print(msj.mensaje_existe("saldo"))
        print("============================")
    else:
        print("===========================================")
        print(msj.mensaje_error_consultar("saldo"))
        print("===========================================")
        existe_dispensador = depositarcontroller\
                            .buscar_deposito_codigo(codigo_cliente, int(codigo_dispensador))
        if not existe_dispensador:
            print(msj.mensaje_no_existe("código del cliente"))
            print("===============================")
            print("")
    print("")
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
