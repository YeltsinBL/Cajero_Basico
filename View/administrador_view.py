"""Vista para las Operaciones por Administrador"""
# region importaciones
import Common.Validacion as validacion
import Common.mensaje as mensaje
import Controller.ClienteController as clientecontroller
import Controller.dispensador_controller as dispensadorcontroller
import Controller.OperacionController as operacioncontroller
# endregion

msj = mensaje.Mensaje()

# region Función para SELECCIONAR FORMULARIO

def seleccionar_acciones_formulario_operacion():
    """Opción para Mostrar las acciones de los formularios"""
    inicio = True
    cont = 0
    while inicio:
        try:
            print("Ingresa el número de la acción a realizar:")
            operacioncontroller.listado_opciones_formulario()
            cant_opc_form = operacioncontroller.cantidad_opciones_formulario()
            nro_accion = int(input(""))
            if cant_opc_form < nro_accion or nro_accion < 1:
                cont += 1
                inicio = validacion.mensaje_validacion(cont)
                continue
            return nro_accion
        except (ValueError, TypeError):
            cont +=1
            inicio = validacion.mensaje_validacion(cont)

def seleccionar_acciones_formulario_operacion_inicial():
    """Opción para Mostrar las acciones de los formularios"""
    inicio = True
    cont = 0
    while inicio:
        try:
            print("Ingresa el número de la acción a realizar:")
            print(1, "Agregar")
            print(6, "Salir")
            nro_accion = int(input(""))
            if nro_accion == 6 or nro_accion == 1:
                return nro_accion
            else:
                cont += 1
                inicio = validacion.mensaje_validacion(cont)
                continue
        except (ValueError, TypeError):
            cont +=1
            inicio = validacion.mensaje_validacion(cont)

# endregion

# region Formulario Cliente
def frm_registrar_cliente():
    """Registro de Clientes"""
    print("======================")
    print(msj.mensaje_frm_registro("CLIENTE"))
    print("======================")
    vali_cod = True
    vali_nom= True
    vali_nrocta= True
    while vali_cod:
        codigo = input("CÓDIGO: ")
        vali_cod = not validacion.valores_ingresados("código",codigo,4)
    while vali_nom:
        nombre = input("NOMBRE: ")
        vali_nom = not validacion.valores_ingresados("nombre",nombre,3)
    while vali_nrocta:
        nrocuentasoles = input("NRO CUENTA SOLES: ")
        vali_nrocta = not validacion.valores_ingresados("nro cuenta soles",nrocuentasoles,1)
    clave = input("CLAVE: ")
    clientecontroller.registro_cliente({"codigo":codigo, "nombre": nombre,
                                        "nrocuentasoles": int(nrocuentasoles),
                                        "clave":clave, "estado": "Activo"})
    print("======================")
    print(msj.mensaje_registrado("CLIENTE"))
    print("======================")
    print("")

def frm_modificar_cliente():
    """Modificar Cliente"""
    vali_cod = True
    datos_cliente:dict[str,any]
    while vali_cod:
        print("====================")
        print(msj.mensaje_frm_modifica("CLIENTE"))
        print("====================")
        codigo_cliente = input("CÓDIGO: ")
        vali_cod = not validacion.valores_ingresados("código",codigo_cliente,4)
        existe_clientes = clientecontroller.verifica_cliente_codigo(codigo_cliente)
        if existe_clientes:
            vali_nom=True
            vali_nrocta = True
            vali_estado = True
            while vali_nom:
                nombre = input("NOMBRE: ")
                vali_nom = not validacion.valores_ingresados("nombre",nombre,3)
            while vali_nrocta:
                nrocuentasoles = input("NRO CUENTA SOLES: ")
                vali_nrocta = not validacion.valores_ingresados("nro cuenta soles",\
                                                                    nrocuentasoles,1)
            while vali_estado:
                estado = input("ESTADO: ")
                vali_estado = not validacion.valores_ingresados("estado",estado,5)
            datos_cliente = {"codigo":codigo_cliente, "nombre": nombre,
                     "nrocuentasoles": int(nrocuentasoles), "estado": estado.capitalize()}
            vali_cod = False
        else:
            vali_cod = True
            print("===============================")
            print(msj.mensaje_no_existe("CÓDIGO"))
            print("===============================")
            print("")
            frm_listado_cliente()
    respt= clientecontroller.modificar_cliente(datos_cliente)
    print("=====================")
    if respt:
        print(msj.mensaje_modificar("CLIENTE"))
    else:
        print(msj.mensaje_error_modificar("CLIENTE"))
    print("=====================")
    print("")

def frm_buscar_cliente():
    """Función para Buscar un cliente por su código"""
    print("===========================")
    print(msj.mensaje_frm_buscar("CLIENTE"))
    print("===========================")
    vali_cod = True
    while vali_cod:
        codigo_cliente = input("CÓDIGO: ")
        vali_cod = not validacion.valores_ingresados("código",codigo_cliente,4)
    respt = clientecontroller.buscar_cliente_codigo(codigo_cliente)
    if not isinstance(respt,list):
        print("NOMBRE:",respt.nombre)
        print("NRO. CUENTA SOLES:",respt.nrocuentasoles)
        print("SALDO:",respt.saldo)
        print("ESTADO:",respt.estado)
        print("====================")
        print(msj.mensaje_existe("CLIENTE"))
        print("====================")
    else:
        print("====================================")
        print(msj.mensaje_error_buscar("CLIENTE"))
        print("====================================")
        existe_clientes = clientecontroller.verifica_cliente_codigo(codigo_cliente)
        if not existe_clientes:
            print(msj.mensaje_no_existe("CÓDIGO"))
            print("================================")
            print("")
            frm_listado_cliente()
    print("")

def frm_listado_cliente():
    """Listado de los Clientes"""
    clientes = clientecontroller.listado_cliente()
    cantidad = 0
    print("=======================")
    print(msj.mensaje_frm_lista("CLIENTES"))
    print("=======================")
    for dato in clientes:
        cantidad += 1
        print(f"CLIENTE NRO. {cantidad}")
        print("CÓDIGO:",dato.codigo)
        print("NOMBRE:",dato.nombre)
        print("NRO. CUENTA SOLES:",dato.nrocuentasoles)
        print("SALDO:",dato.saldo)
        print("ESTADO:",dato.estado)
        print("=======================")
    print(msj.mensaje_listado("CLIENTES"))
    print("=======================")
    print("")

def selecciona_estado_cliente():
    """Selecciona el tipo a listar de los Clientes por estado"""
    inicio = True
    cont = 0
    while inicio:
        try:
            print()
            print("Ingresa el número del estado")
            operacioncontroller.listado_estados_clientes()
            nro_menu = int(input(""))
            if 3 < nro_menu or nro_menu < 1:
                cont += 1
                inicio = validacion.mensaje_validacion(cont)
                continue
            return nro_menu
        except (ValueError, TypeError):
            cont += 1
            validacion.mensaje_validacion(cont)

def frm_estado_cliente():
    """Lista de los Clientes por estado"""
    nro_estado = selecciona_estado_cliente()
    if nro_estado == 3:
        return
    estado = "activo" if nro_estado == 1 else "desactivo"
    respt = clientecontroller.listado_cliente_estado(estado)
    if len(respt)>0:
        cantidad = 0
        print("=================================")
        print(msj.mensaje_frm_listar_estado("CLIENTE", estado.upper()+"S"))
        print("=================================")
        for dato in respt:
            cantidad += 1
            print(f"CLIENTE NRO. {cantidad}")
            print("CÓDIGO:",dato.codigo)
            print("NOMBRE:",dato.nombre)
            print("NRO. CUENTA SOLES:",dato.nrocuentasoles)
            print("SALDO:",dato.saldo)
            print("ESTADO:",dato.estado)
            print("===============================")
        print(msj.mensaje_encontro_por_estado("CLIENTES", estado.upper()+"S"))
        print("===============================")
        print("")
    else:
        print("============================")
        print(msj.mensaje_no_encontro_por_estado("CLIENTES", estado.upper()+"S"))
        print("============================")
        print("")

# endregion

# region Formulario DISPENSADOR
def frm_agregar_dispensador():
    """Registrar Dispensador"""
    print("============================")
    print(msj.mensaje_frm_registro("DISPENSADOR"))
    print("============================")
    vali_lugar = True
    vali_billetes= True
    vali_bill_200=True
    vali_bill_100=True
    vali_bill_50=True
    vali_bill_20=True
    vali_bill_10=True
    cant_disp= len(dispensadorcontroller.listado_dispensador())
    billetes=[]
    while vali_lugar:
        lugar = input("LUGAR: ")
        vali_lugar = not validacion.valores_ingresados("lugar",lugar,3)
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
    dispensadorcontroller.registro_dispensador({"codigo":cant_disp+1,"lugar":lugar,
                                                       "billete": billetes,"estado": "Activo"})
    print("============================")
    print(msj.mensaje_registrado("DISPENSADOR"))
    print("============================")
    print("")

def frm_listado_dispensadores():
    """Listar los Dispensadores"""
    dispensa = dispensadorcontroller.listado_dispensador()
    cantidad = 0
    print("============================")
    print(msj.mensaje_frm_lista("DISPENSADORES"))
    print("============================")
    for dato in dispensa:
        cantidad += 1
        print(f"DISPENSADOR NRO. {cantidad}")
        print("CODIGO:", dato.codigo)
        print("LUGAR:", dato.lugar)
        print("BILLETES:")
        for valor in dato.billete:
            for nro_billete, vbillete in valor.items():
                print(str(nro_billete).upper()+ ": ",vbillete)
        print("ESTADO:", dato.estado)
        print("============================")
    print(msj.mensaje_listado("DISPENSADORES"))
    print("============================")
    print("")

def frm_modificar_dispensador():
    """Modififcar Dispensdaor"""
    vali_cod = True
    datos_dispensador:dict[str,any]
    billetes=[]
    while vali_cod:
        print("============================")
        print(msj.mensaje_frm_modifica("DISPENSADOR"))
        print("============================")
        codigo_dispensador = input("CÓDIGO: ")
        vali_cod = not validacion.valores_ingresados("código",codigo_dispensador,1)
        existe_dispensador = dispensadorcontroller\
                                .verifica_dispensador_codigo(int(codigo_dispensador))
        if existe_dispensador:
            vali_lugar = True
            vali_bill_200=True
            vali_bill_100=True
            vali_bill_50=True
            vali_bill_20=True
            vali_bill_10=True
            vali_estado = True
            while vali_lugar:
                lugar = input("NUEVO LUGAR: ")
                vali_lugar = not validacion.valores_ingresados("lugar",lugar,3)
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
            while vali_estado:
                estado = input("NUEVO ESTADO: ")
                vali_estado = not validacion.valores_ingresados("estado",estado,5)
            billetes.append({200:int(billete_200), 100:int(billete_100),
                             50:int(billete_50), 20:int(billete_20),
                             10:int(billete_10)})
            datos_dispensador={"codigo":int(codigo_dispensador),"lugar":lugar,
                               "billete": billetes,"estado": estado.capitalize()}
            vali_cod = False
        else:
            vali_cod = True
            print(msj.mensaje_no_existe("CÓDIGO"))
            print("=======================================")
            print("")
            frm_listado_dispensadores()
            print("=======================================")
    respt = dispensadorcontroller.modificar_dispensador(datos_dispensador)
    print("============================")
    if respt:
        print(msj.mensaje_modificar("DISPENSADOR"))
    else:
        print(msj.mensaje_error_modificar("DISPENSADOR"))
    print("============================")
    print("")

def frm_buscar_dispensador():
    """Buscar Dispensador por Código"""
    print("================================")
    print(msj.mensaje_frm_buscar("DISPENSADOR"))
    print("================================")
    vali_cod = True
    while vali_cod:
        codigo_dispensador = input("CÓDIGO: ")
        vali_cod = not validacion.valores_ingresados("código",codigo_dispensador,1)
    respt = dispensadorcontroller.buscar_dispensador_codigo(int(codigo_dispensador))
    if not isinstance(respt,list):
        print("LUGAR:",respt.lugar)
        print("BILLETES:")
        for valor in respt.billete:
            for nro_billete, vbillete in valor.items():
                print(str(nro_billete).upper()+ ": ",vbillete)
        print("ESTADO:",respt.estado)
        print("============================")
        print(msj.mensaje_existe("DISPENSADOR"))
        print("============================")
    else:
        print("===========================================")
        print(msj.mensaje_error_buscar("DISPENSADOR"))
        print("===========================================")
        existe_dispensador = dispensadorcontroller.\
                                verifica_dispensador_codigo(int(codigo_dispensador))
        if not existe_dispensador:
            print(msj.mensaje_no_existe("CÓDIGO"))
            print("===============================")
            print("")
            frm_listado_dispensadores()
    print("")

def frm_estado_dispensador():
    """Lista de los Dispensadores por estado"""
    nro_estado = selecciona_estado_cliente()
    if nro_estado == 3:
        return
    estado = "activo" if nro_estado == 1 else "desactivo"
    respt = dispensadorcontroller.listado_dispensador_estado(estado)
    if len(respt)>0:
        cantidad = 0
        print("=====================================")
        print(msj.mensaje_frm_listar_estado("DISPENSADOR", estado.upper()+"S"))
        print("=====================================")
        for dato in respt:
            cantidad += 1
            print(f"DISPENSADOR NRO. {cantidad}")
            print("CÓDIGO:",dato.codigo)
            print("LUGAR:",dato.lugar)
            print("BILLETES:")
            for valor in dato.billete:
                for nro_billete, vbillete in valor.items():
                    print(str(nro_billete).upper()+ ": ",vbillete)
            print("ESTADO:",dato.estado)
            print("====================================")
        print(msj.mensaje_encontro_por_estado("DISPENSADORES", estado.upper()+"S"))
        print("====================================")
        print("")
    else:
        print("==================================")
        print(msj.mensaje_no_encontro_por_estado("DISPENSADORES", estado.upper()+"S"))
        print("==================================")
        print("")
#endregion

# region Función de Administrador

def seleccion_accion_formulario(opc_accion, opc_operacion):
    """Acciones de acuerdo al formulario seleccionado"""
    # mostrar_seleccionados(opc_menu,opc_operacion,opc_accion)
    match opc_accion:
        case 1:
            _ = frm_registrar_cliente() if opc_operacion == 1 \
                else frm_agregar_dispensador()
        case 2:
            _ = frm_modificar_cliente() if opc_operacion == 1 \
                else frm_modificar_dispensador()
        case 3:
            _ = frm_buscar_cliente() if opc_operacion == 1 \
                else frm_buscar_dispensador()
        case 4:
            _ = frm_estado_cliente() if opc_operacion == 1 \
                else frm_estado_dispensador()
        case 5:
            _ = frm_listado_cliente() if opc_operacion == 1 \
                else frm_listado_dispensadores()

def seleccion_formulario(opc_operacion):
    """Selección del Formulario"""
    iniciar_accion = True
    while iniciar_accion:
        opc_accion: int | None
        if (opc_operacion == 1 and len(clientecontroller.listado_cliente()) == 0) or \
            (opc_operacion == 2 and len(dispensadorcontroller.listado_dispensador()) == 0):
            opc_accion = seleccionar_acciones_formulario_operacion_inicial()
        else:
            opc_accion = seleccionar_acciones_formulario_operacion()
        if opc_accion == 6:
            iniciar_accion = False
            break
        seleccion_accion_formulario(opc_accion=opc_accion,
                                    opc_operacion=opc_operacion)

# endregion
