"""Vista para las Operaciones por Cliente Depositar"""
# region importaciones
import Common.Validacion as validacion
import Common.mensaje as mensaje
import Controller.ClienteController as clientecontroller
import Controller.dispensador_controller as dispensadorcontroller
import Controller.depositar_controller as depositarcontroller
# endregion

msj = mensaje.Mensaje()

# region Formulario Depositar
def frm_registrar_deposito():
    """Registrar Depósito"""
    print("======================")
    print(msj.mensaje_frm_registro("depósito"))
    print("======================")
    vali_codigo_cliente = True
    vali_codigo_dispensador= True
    vali_billetes = True
    vali_bill_200=True
    vali_bill_100=True
    vali_bill_50=True
    vali_bill_20=True
    vali_bill_10=True
    billetes=[]
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
                vali_codigo_dispensador = False
                vali_billetes = False
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
                vali_billetes = False
    while vali_billetes:
        print("Cantidad de Billetes")
        while vali_bill_200:
            billete_200 = input("Billetes de 200: ")
            vali_bill_200 = not validacion.valores_ingresados("billetes de 200",billete_200,1)
        while vali_bill_100:
            billete_100 = input("Billetes de 100: ")
            vali_bill_100 = not validacion.valores_ingresados("billetes de 100",billete_100,1)
        while vali_bill_50:
            billete_50 = input("Billetes de 50: ")
            vali_bill_50 = not validacion.valores_ingresados("billetes de 50",billete_50,1)
        while vali_bill_20:
            billete_20 = input("Billetes de 20: ")
            vali_bill_20 = not validacion.valores_ingresados("billetes de 20",billete_20,1)
        while vali_bill_10:
            billete_10 = input("Billetes de 10: ")
            vali_bill_10 = not validacion.valores_ingresados("billetes de 10",billete_10,1)
        billetes.append({200:int(billete_200), 100:int(billete_100), 50:int(billete_50),
                         20:int(billete_20), 10:int(billete_10)})
        vali_billetes = False
    respt_cliente = clientecontroller.buscar_cliente_codigo(codigo_cliente)
    respt_dispensador = dispensadorcontroller.\
                        buscar_dispensador_codigo(int(codigo_dispensador))
    dato_dispensador = {"codigo_cliente":codigo_cliente,
                        "nombre_cliente":respt_cliente.nombre,
                        "codigo_dispensador": int(codigo_dispensador),
                        "lugar_dispensador":respt_dispensador.lugar,
                        "estado_dispensador":respt_dispensador.estado,
                        "billete":billetes}
    respt= vista_previa_registro(dato_dispensador)
    if respt:
        dato_dispensador["monto"] = float(respt)
        respt2 = depositarcontroller.registro_deposito(dato_dispensador)
        if respt2:
            print("======================")
            print(msj.mensaje_registrado("depósito"))
            print("======================")
            print("")
        else:
            print("======================")
            print(msj.mensaje_error_registrar("depósito"))
            print("======================")
            print("")
    else:
        print("======================")
        print(msj.mensaje_cancelar_confirmacion("depósito"))
        print("======================")
        print("")

def vista_previa_registro(datos_depositar:dict[str,any]):
    """Vista previa al registrar"""
    total=0
    print(datos_depositar)
    print("===========================")
    print(msj.mensaje_frm_vista_previa("depósito"))
    print("===========================")
    print("CLIENTE:",datos_depositar.get("nombre_cliente"))
    print("DISPENSADOR:",datos_depositar.get("codigo_dispensador"),"-",
          datos_depositar.get("lugar_dispensador"))
    print("CANTIDAD DE BILLETES:")
    for valor in datos_depositar.get("billete"):
        for nro_billete, vbillete in valor.items():
            print(str(nro_billete)+ ": ",vbillete)
            total = total + (int(nro_billete)* vbillete)
    print("TOTAL:", total)
    print("===========================")
    while True:
        print("¿CONFIRMAR DEPÓSITO? 1 [SI]  o 0 [NO] ")
        confirmar = input("INGRESE OPCIÓN: ")
        if confirmar== "1":
            return int(total)
        elif confirmar == "0":
            return 0
        msj.mensaje_opcion_ingresada_incorrecta()

# endregion
