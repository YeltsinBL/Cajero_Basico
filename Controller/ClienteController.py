import Model.Cliente as cliente

cliente_clase = cliente.Cliente()
cliente_clase.set_codigo("000001")

def registrar_cliente():
    """Función de Registro de Clientes"""
    print("REGISTRO DEL CLIENTE")
    print("Ingrese la información")
    codigo = input("CÓDIGO: ")
    nombre = input("NOMBRE:")
    nrocuentasoles = input("NRO CUENTA SOLES: ")
    saldo = float(input("SALDO:"))
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
            print(str(idx).upper()+ ": ",valor)
