"""Vista del menú de operaciones"""
# region Importaciones
from colorama import Fore, Style
from Common import mensaje
import Controller.ClienteController as clientecontroller
import Controller.MenuController as menucontroller
import View.administrador_view as administradorview
import View.operacion_cliente_view as operacionclienteview
# endregion

msj = mensaje.Mensaje()

# region Funciones de Opciones
def selecciona_operacion(nromenu:int, nombre_seleccion:str):
    """Opción para escoger el formulario"""
    while True:
        print(Style.BRIGHT + Fore.BLUE)
        print(msj.mensaje_menu(nombre_seleccion))
        print(Fore.WHITE + Style.NORMAL)
        print("Ingresa el número de operación a realizar:")
        lista_menu =[]
        nueva_lista={}
        if len(lista_menu)==0:
            lista_menu = menucontroller.listar_menu(nromenu)
        for resultado in lista_menu:
            print(resultado[0], resultado[1])
            nueva_lista[resultado[0]]=resultado[2]
        nro_operacion = input("")
        if nro_operacion.isdigit() and int(nro_operacion)\
            in list(range(len(lista_menu)+1)):
            return int(nro_operacion), nueva_lista
        print(Style.BRIGHT + Fore.RED)
        print("===============================")
        print(msj.mensaje_opcion_ingresada_incorrecta())
        print("===============================")

# endregion

#region Selección de Opciones
def seleccionar_operaciones(opc_menu, nombre_seleccion):
    """Selección de las opciones de Operaciones"""
    iniciar_operacion = True
    while iniciar_operacion:
        opc_operacion, lista= selecciona_operacion(opc_menu, nombre_seleccion)
        if opc_operacion == len(lista):
            iniciar_operacion = False
        elif opc_menu == 3 :
            administradorview.seleccion_formulario(lista.get(int(opc_operacion)))
        else:
            contar =0
            if opc_operacion == 3:
                clientes = clientecontroller.listado_cliente()
                for cliente in clientes:
                    if cliente[5] == 1:
                        contar+=1
                if contar <=1:
                    print(msj.mensaje_mantenimiento("Operación de Transferencia"))
                else:
                    operacionclienteview.seleccion_formulario_operacion_cliente(opc_operacion)
            else:
                operacionclienteview.seleccion_formulario_operacion_cliente(opc_operacion)
#endregion
