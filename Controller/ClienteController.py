"""Funciones que interactúan con los datos del Cliente"""
import Model.Cliente as cliente
import Common.Validacion as validacion

cliente_clase = cliente.Cliente()
cliente_clase.set_codigo("000001")

def registrar_cliente():
    """Función de Registro de Clientes"""
    print("REGISTRO DEL CLIENTE")
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
    return {"codigo":codigo, "nombre": nombre,
                     "nroCuentaSoles": nrocuentasoles,
                     "saldo": saldo, "clave":clave, "estado": "Activo"}

def listado_clientes(clientes):
    """Muestra las clientes registrados"""
    cantidad = 0
    print("LISTADO DE LOS CLIENTES")
    for dato in clientes:
        cantidad += 1
        print(f"CLIENTE NRO. {cantidad}")
        for idx, valor in dato.items():
            if not idx.lower() == "clave":
                print(str(idx).upper()+ ": ",valor)
        print("=======================================")

def modificar_cliente(clientes:list):
    """Función para Modificar Cliente"""
    vali_cod = True
    while vali_cod:
        print("MODIFICAR CLIENTE")
        codigo_cliente = input("CÓDIGO: ")
        vali_cod = not validacion.valores_ingresados("código",codigo_cliente,4)
        for dato in clientes:
            if dato["codigo"]==codigo_cliente:
                vali_nom=True
                vali_nrocta = True
                vali_saldo = True
                vali_estado = True
                print("NOMBRE ACTUAL:", dato["nombre"])
                while vali_nom:
                    nombre = input("NUEVO NOMBRE: ")
                    vali_nom = not validacion.valores_ingresados("nombre",nombre,3)
                print("NRO CUENTA SOLES ACTUAL:", dato["nroCuentaSoles"])
                while vali_nrocta:
                    nrocuentasoles = input("NUEVO NRO CUENTA SOLES: ")
                    vali_nrocta = not validacion.valores_ingresados("nro cuenta soles",nrocuentasoles,1)
                print("SALDO ACTUAL:", dato["saldo"])
                while vali_saldo:
                    saldo = input("NUEVO SALDO: ")
                    vali_saldo = not validacion.valores_ingresados("saldo",saldo,2)
                print("ESTADO ACTUAL:", dato["estado"])
                while vali_estado:
                    estado = input("NUEVO ESTADO: ")
                    vali_estado = not validacion.valores_ingresados("estado",estado,5)
                dato["nombre"] = nombre
                dato["nroCuentaSoles"] = nrocuentasoles
                dato["saldo"] = saldo
                dato["estado"] = estado.capitalize()
                return clientes
            else:
                vali_cod = True
                print("El CÓDIGO ingresado no existe")
                print("=======================================")
                print("")
                listado_clientes(clientes)
                print("=======================================")

def consultar_cliente(clientes:list):
    """Función para Buscar un cliente por su código"""
    print("CONSULTAR CLIENTE")
    vali_cod = True
    while vali_cod:
        codigo_cliente = input("CÓDIGO: ")
        vali_cod = not validacion.valores_ingresados("código",codigo_cliente,4)
    nueva = (x for x in clientes if x["codigo"]==codigo_cliente)
    for dato in nueva:
        for idx, valor in dato.items():
            if not idx.lower() == "clave":
                print(str(idx).upper()+ ": ",valor)
        print("=======================================")

def activo_cliente(clientes:list, nro_estado):
    """Función para Buscar los clientes activos"""
    cantidad = 0
    estado="activo" if nro_estado ==1 else "desactivo"
    print("CLIENTES", estado.upper()+"S")
    nueva = (x for x in clientes if x["estado"].lower()== estado)
    for dato in nueva:
        cantidad += 1
        print(f"CLIENTE NRO. {cantidad}")
        for idx, valor in dato.items():
            if not idx.lower() == "clave":
                print(str(idx).upper()+ ": ",valor)
        print("=======================================")
