"""Módulo de la Vista del Menú"""

# region Importaciones
from colorama import Fore, Style
from Common import mensaje
import View.operaciones_view as operacionview
import Controller.MenuController as menucontroller
import Controller.ClienteController as clientecontroller
import Controller.dispensador_controller as dispensadorcontroller
# endregion

msj = mensaje.Mensaje()

# region Funciones para seleccionar
def selecciona_menu():
    """Función para seleccionar opción del menú principal"""
    while True:
        print(Fore.BLUE + Style.BRIGHT)
        print(msj.mensaje_menu("Principal"))
        print(Fore.WHITE + Style.NORMAL)
        print("Ingresa el número de tu tipo de usuario:")
        menucontroller.listado_menu()
        nro_menu = input("")
        if nro_menu.isdigit() and int(nro_menu) in {1, 2, 3}:
            return int(nro_menu)
        print(Style.BRIGHT + Fore.RED)
        print("===============================")
        print(msj.mensaje_opcion_ingresada_incorrecta())
        print("===============================")

# endregion
def iniciar_sistema():
    """Inicia el Sistema"""
    print(Style.BRIGHT)
    print("==============")
    print("¡BIENVENIDO!")
    print("==============")

    iniciar_principal = True
    while iniciar_principal:
        opc_menu = selecciona_menu()
        if opc_menu == 3:
            msj.mensaje_despedida()
            iniciar_principal = False
            break
        if opc_menu == 1:
            if len(clientecontroller.listado_cliente())==0:
                print(Style.BRIGHT + Fore.RED)
                print("===============================")
                print(msj.mensaje_mantenimiento("sistema"))
                print("===============================")
                continue
            if len(dispensadorcontroller.listado_dispensador())==0:
                print(Style.BRIGHT + Fore.RED)
                print("===============================")
                print(msj.mensaje_mantenimiento("dispensadores"))
                print("===============================")
                continue
        operacionview.seleccionar_operaciones(opc_menu=opc_menu)
