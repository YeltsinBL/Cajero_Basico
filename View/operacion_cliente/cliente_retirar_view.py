"""Vista para las Operaciones por Cliente Retirar"""
# region importaciones
import Common.Validacion as validacion
import Common.mensaje as mensaje
import Controller.ClienteController as clientecontroller
import Controller.dispensador_controller as dispensadorcontroller
import Controller.retirar_controller as retirocontroller
import Controller.cuenta_cliente_controller as cuentaclientecontroller
# endregion

msj = mensaje.Mensaje()

# region Formulario Retirar
def frm_registrar_retiro():
    """Registrar Retiro"""
    print("======================")
    print(msj.mensaje_frm_registro("retiro"))
    print("======================")
    vali_codigo_cliente = True
    vali_clave_cliente = True
    vali_codigo_dispensador= True
    vali_monto = True
    while vali_codigo_cliente:
        vali_codigo_dispensador= True
        codigo_cliente = input("CÓDIGO CLIENTE: ")
        vali_codigo_cliente = not validacion.\
                                valores_ingresados("código del cliente",codigo_cliente,4)
        if vali_codigo_cliente is False:
            vali_codigo_cliente = not clientecontroller.verifica_cliente_codigo(codigo_cliente)
            if vali_codigo_cliente:
                print("===============================")
                print(msj.mensaje_no_existe("código del cliente"))
                print("===============================")
                print("")
                vali_codigo_dispensador = False
            else:
                cont = 0
                while vali_clave_cliente:
                    vali_codigo_dispensador= True
                    clave = input("CLAVE CLIENTE: ")
                    vali_clave_cliente = not clientecontroller.\
                        verifica_cliente_codigo_clave(codigo_cliente, clave)
                    if vali_clave_cliente:
                        print("===============================")
                        print(msj.mensaje_clave_incorrecta("clave"))
                        print("===============================")
                        print("")
                        cont +=1
                        if cont == 3:
                            return
                        intent = lambda cont : "intento" if(3-cont == 1) else "intentos"
                        print(f"LE QUEDA {3 - cont}", intent(cont).upper())
                        vali_codigo_dispensador = False
    while vali_codigo_dispensador:
        codigo_dispensador = input("CÓDIGO DISPENSADOR: ")
        vali_codigo_dispensador = not validacion.\
                                    valores_ingresados("código dispensador",codigo_dispensador,1)
        if vali_codigo_dispensador is False:
            vali_codigo_dispensador = not dispensadorcontroller\
                                .verifica_dispensador_codigo(int(codigo_dispensador))
            if vali_codigo_dispensador:
                print("===============================")
                print(msj.mensaje_no_existe("código del dispensador"))
                print("===============================")
                print("")
    while vali_monto:
        monto = input("MONTO: ")
        vali_monto = not validacion.valores_ingresados("MONTO",monto,2)
        if vali_monto is False:
            print("====================================================")
            print(msj.mensaje_verificar_tipo("saldo","el dispensador"))
            print("====================================================")
            vali_monto = not dispensadorcontroller.verificar_monto_dispensador(
                                        int(codigo_dispensador), float(monto))
            if vali_monto:
                print("===============================")
                print(msj.mensaje_monto_excedido("al dispensador"))
                print("===============================")
                print("")
            else:
                print("====================================================")
                print(msj.mensaje_verificar_tipo("saldo","la cuenta del cliente"))
                print("====================================================")
                vali_monto = not cuentaclientecontroller.verificar_cuenta_cliente(
                                codigo_cliente, int(codigo_dispensador), float(monto))
                if vali_monto:
                    print("====================================================")
                    print(msj.mensaje_monto_excedido("el saldo del cliente"))
                    print("====================================================")
                    print("")
                    return
    respt_cliente = clientecontroller.buscar_cliente_codigo(codigo_cliente)
    respt_dispensador = dispensadorcontroller.\
                        buscar_dispensador_codigo(int(codigo_dispensador))
    datos = {"codigo_cliente":codigo_cliente, "nombre_cliente":respt_cliente.nombre,
            "codigo_dispensador":int(codigo_dispensador),
            "lugar_dispensador":respt_dispensador.lugar, 
            "estado_dispensador":respt_dispensador.estado, 
            "monto":float(monto)}
    print("============================================")
    print(msj.mensaje_verificar_tipo("billetes","el dispensador"))
    print("============================================")
    resp = retirocontroller.registro_retiro(datos)
    if isinstance(resp, list) and len(resp)>0:
        detalle_retiro(datos.get("codigo_cliente"), datos.get("nombre_cliente"),
                       datos.get("codigo_dispensador"), datos.get("lugar_dispensador"),
                       datos.get("monto"), resp)
        print("======================")
        print(msj.mensaje_registrado("retiro"))
        print("======================")
        print("")
    elif isinstance(resp, str):
        print("============================================")
        print(msj.mensaje_error_al("registrar","el dispensador"))
        print(msj.mensaje_no_tiene("dispensador",f"suficientes billetes de {resp[:-3]}"))
        print("============================================")
        print("")
    else:
        print("======================")
        print(msj.mensaje_error_al("registrar","retiro"))
        print("======================")
        print("")

def detalle_retiro(codigo_cliente,nombre_cliente, codigo_dispensador,
                   lugar_dispensador, monto, datos_retiro:list):
    """Verificar el monto del Dispensador"""
    print("CÓDIGO CLIENTE:", codigo_cliente)
    print("NOMBRE CLIENTE:", nombre_cliente)
    print("CÓDIGO DISPENSADOR:", codigo_dispensador,"-", lugar_dispensador)
    print("MONTO:", monto)
    print("BILLETES:")
    for dato in datos_retiro:
        for nro_billete, vbillete in dato.items():
            print(str(nro_billete)+ ": ",vbillete)
# endregion
