import Model.Cliente as cliente

cliente_clase = cliente.Cliente()
cliente_clase.set_codigo("000001")

clientes = []

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
    print()
    cantidad = 0
    if len(clientes) ==0:
        print("No hay clientes para mostrar")
    cantidad += 1
    print("LISTADO DE LOS CLIENTES")
    print(f"Cliente nro {cantidad}")
    for idx, dato in clientes.items():
        print(str(idx).upper()+ ": ",dato)
