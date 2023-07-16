class Operacion:
    """Clase para las operaciones 
    de acuerdo a la opcion del menú principal"""
    opcion = {1:[{1:"Depositar", 2:"Retirar", 3:"Transferir",
                  4:"Pagar Servicio", 5:"Consultar Saldo",
                  6:"Consultar Movimiento", 7:"Salir"}],
              2:[{1:"Gestionar Clientes",
                  2:"Gestionar Dispensador", 3:"Salir"}]}

opcion_fuera = {1:[{1:"Depositar", 2:"Retirar", 3:"Transferir",
                  4:"Pagar Servicio", 5:"Consultar Saldo",
                  6:"Consultar Movimiento", 7:"Regresar al Menú Principal"}],
              2:[{1:"Gestionar Clientes",
                  2:"Gestionar Dispensador", 3:"Regresar al Menú Principal"}]}

opcion_estado_cliente = {1:"Activo", 2:"Inactivo", 3:"Salir"}
