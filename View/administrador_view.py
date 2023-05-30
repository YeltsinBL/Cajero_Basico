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
    print(msj.mensaje_frm_registro("CLIENTE"))
    print("Ingrese la información")
    vali_cod = True
    vali_nom= True
    vali_nrocta= True
    vali_saldo = True
    while vali_cod:
        codigo = input("CÓDIGO: ")
        vali_cod = not validacion.valores_ingresados("código",codigo,4)
    while vali_nom:
        nombre = input("NOMBRE: ")
        vali_nom = not validacion.valores_ingresados("nombre",nombre,3)
    while vali_nrocta:
        nrocuentasoles = input("NRO CUENTA SOLES: ")
        vali_nrocta = not validacion.valores_ingresados("nro cuenta soles",nrocuentasoles,1)
    while vali_saldo:
        saldo = input("SALDO: ")
        vali_saldo = not validacion.valores_ingresados("saldo",saldo,2)
    clave = input("CLAVE: ")
    clientecontroller.registro_cliente({"codigo":codigo, "nombre": nombre,
                                        "nrocuentasoles": int(nrocuentasoles),
                                        "saldo": float(saldo), "clave":clave, "estado": "Activo"})
    print("============================")
    print(msj.mensaje_registrado("CLIENTE"))
    print("============================")
    print("")

def frm_modificar_cliente():
    """Modificar Cliente"""
    vali_cod = True
    datos_cliente:dict[str,any]
    while vali_cod:
        print(msj.mensaje_frm_modifica("CLIENTE"))
        codigo_cliente = input("CÓDIGO: ")
        vali_cod = not validacion.valores_ingresados("código",codigo_cliente,4)
        existe_clientes = clientecontroller.verifica_cliente_codigo(codigo_cliente)
        if existe_clientes:
            vali_nom=True
            vali_nrocta = True
            vali_estado = True
            while vali_nom:
                nombre = input("NUEVO NOMBRE: ")
                vali_nom = not validacion.valores_ingresados("nombre",nombre,3)
            while vali_nrocta:
                nrocuentasoles = input("NUEVO NRO CUENTA SOLES: ")
                vali_nrocta = not validacion.valores_ingresados("nro cuenta soles",\
                                                                    nrocuentasoles,1)
            while vali_estado:
                estado = input("NUEVO ESTADO: ")
                vali_estado = not validacion.valores_ingresados("estado",estado,5)
            datos_cliente = {"codigo":codigo_cliente, "nombre": nombre,
                     "nrocuentasoles": int(nrocuentasoles), "estado": estado.capitalize()}
            vali_cod = False
        else:
            vali_cod = True
            print(msj.mensaje_no_existe("CÓDIGO"))
            print("=======================================")
            print("")
            frm_listado_cliente()
            print("=======================================")
    respt= clientecontroller.modificar_cliente(datos_cliente)
    print("============================")
    if respt:
        print(msj.mensaje_modificar("CLIENTE"))
    else:
        print(msj.mensaje_error_modificar("CLIENTE"))
    print("============================")
    print("")

def frm_buscar_cliente():
    """Función para Buscar un cliente por su código"""
    print(msj.mensaje_frm_buscar("CLIENTE"))
    vali_cod = True
    while vali_cod:
        codigo_cliente = input("CÓDIGO: ")
        vali_cod = not validacion.valores_ingresados("código",codigo_cliente,4)
    #return codigo_cliente
    respt = clientecontroller.buscar_cliente_codigo(codigo_cliente)
    if not isinstance(respt,list):
        print("NOMBRE:",respt.nombre)
        print("NRO. CUENTA SOLES:",respt.nrocuentasoles)
        print("SALDO:",respt.saldo)
        print("ESTADO:",respt.estado)
        print("============================")
        print(msj.mensaje_existe("CLIENTE"))
    else:
        print(msj.mensaje_error_buscar("CLIENTE"))
        existe_clientes = clientecontroller.verifica_cliente_codigo(codigo_cliente)
        if not existe_clientes:
            print(msj.mensaje_no_existe("CÓDIGO"))
            print("=======================================")
            print("")
            frm_listado_cliente()
    print("=======================================")
    print("")

def frm_listado_cliente():
    """Listado de los Clientes"""
    clientes = clientecontroller.listado_cliente()
    cantidad = 0
    print("============================")
    print(msj.mensaje_frm_lista("CLIENTES"))
    print("============================")
    for dato in clientes:
        cantidad += 1
        print(f"CLIENTE NRO. {cantidad}")
        print("CÓDIGO:",dato.codigo)
        print("NOMBRE:",dato.nombre)
        print("NRO. CUENTA SOLES:",dato.nrocuentasoles)
        print("SALDO:",dato.saldo)
        print("ESTADO:",dato.estado)
        print("=======================================")
    print(msj.mensaje_listado("CLIENTES"))
    print("============================================")
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
        for dato in respt:
            cantidad += 1
            print(msj.mensaje_frm_listar_estado("CLIENTE", estado.upper()+"S"))
            print(f"CLIENTE NRO. {cantidad}")
            print("CÓDIGO:",dato.codigo)
            print("NOMBRE:",dato.nombre)
            print("NRO. CUENTA SOLES:",dato.nrocuentasoles)
            print("SALDO:",dato.saldo)
            print("ESTADO:",dato.estado)
            print("============================================")
        print(msj.mensaje_encontro_por_estado("CLIENTES", estado.upper()+"S"))
        print("============================================")
        print("")
    else:
        print("============================================")
        print(msj.mensaje_no_encontro_por_estado("CLIENTES", estado.upper()+"S"))
        print("============================================")
        print("")

# endregion

# region Funciones para los DISPENSADORES
def agregar_dispensador():
    """Registrar Dispensador"""
    dispensadorcontroller.registrar_dispensador()
    print("============================")
    print("DISPENSADOR REGISTRADO!")
    print("============================")
    print("")
def listado_dispensdores():
    """Listar los Dispensadores"""
    dispensadorcontroller.listado_dispensadores()
    print("============================")
    print("¡LISTA DE DISPENSADORES!")
    print("============================")
    print("")

def modificar_dispensador():
    """Modififcar Dispensdaor"""
    dispensadorcontroller.modificar_dispensador()
    print("============================")
    print("¡DISPENSADOR MODIFICADO!")
    print("============================")
    print("")

def consultar_dispensador():
    """Consultar Dispensador"""
    dispensadorcontroller.consultar_dispensador()
    print("============================")
    print("¡DISPENSADOR POR CÓDIGO!")
    print("============================")
    print("")

def estado_dispensador():
    """Lista de los Dispensadores por estado"""
    nro_estado = selecciona_estado_cliente()
    if nro_estado == 3:
        return
    dispensadorcontroller.activo_dispensador(nro_estado)
    estado = "activo" if nro_estado == 1 else "desactivo"
    print("============================================")
    print("¡TODOS LOS DISPENSADORES", estado.upper()+"S!")
    print("============================================")
    print("")
#endregion

# region Función de Administrador

def seleccion_accion_formulario(opc_accion, opc_operacion):
    """Acciones de acuerdo al formulario seleccionado"""
    # mostrar_seleccionados(opc_menu,opc_operacion,opc_accion)
    match opc_accion:
        case 1:
            _ = frm_registrar_cliente() if opc_operacion == 1 \
                else agregar_dispensador()
        case 2:
            _ = frm_modificar_cliente() if opc_operacion == 1 \
                else modificar_dispensador()
        case 3:
            _ = frm_buscar_cliente() if opc_operacion == 1 \
                else consultar_dispensador()
        case 4:
            _ = frm_estado_cliente() if opc_operacion == 1 \
                else estado_dispensador()
        case 5:
            _ = frm_listado_cliente() if opc_operacion == 1 \
                else listado_dispensdores()

def seleccion_formulario(opc_operacion):
    """Selección del Formulario"""
    iniciar_accion = True
    while iniciar_accion:
        opc_accion: int | None
        if (opc_operacion == 1 and len(clientecontroller.listado_cliente()) == 0) or \
                (opc_operacion == 2 and len(dispensadorcontroller.lista_dispensadores()) == 0):
            opc_accion = seleccionar_acciones_formulario_operacion_inicial()
        else:
            opc_accion = seleccionar_acciones_formulario_operacion()
        if opc_accion == 6:
            iniciar_accion = False
            break
        seleccion_accion_formulario(opc_accion=opc_accion,
                                    opc_operacion=opc_operacion)

# endregion
