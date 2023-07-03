"""Módulo de la Vista del Menú"""
# region Importaciones
from colorama import Fore, Style
import Common.mensaje as mensaje
import Common.Validacion as validacion
import Controller.MenuController as menucontroller
import View.operaciones_view as operacionview
import Controller.ClienteController as clientecontroller
import Controller.dispensador_controller as dispensadorcontroller
# endregion
msj = mensaje.Mensaje()
# region Funciones para seleccionar
def selecciona_menu():
    """Función para seleccionar opción del menú principal"""
    inicio = True
    cont = 0
    while inicio:
        try:
            print(Fore.BLUE)
            print(msj.mensaje_menu("Principal"))
            print(Fore.WHITE + Style.NORMAL)
            print("Ingresa el número de tu tipo de usuario:")
            menucontroller.listado_menu()
            nro_menu = int(input(""))
            if 3 < nro_menu or nro_menu < 1:
                cont += 1
                inicio = validacion.mensaje_validacion(cont)
                continue
            return nro_menu
        except (ValueError, TypeError):
            cont +=1
            validacion.mensaje_validacion(cont)
# endregion
def iniciar_sistema():
    """Inicia el Sistema"""
    # print("")
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
        elif opc_menu == 1:
            if len(clientecontroller.listado_cliente())==0:
                print(Style.BRIGHT + Fore.RED)
                print("===============================")
                print(msj.mensaje_mantenimiento("sistema"))
                print("===============================")
                continue
            elif len(dispensadorcontroller.listado_dispensador())==0:
                print(Style.BRIGHT + Fore.RED)
                print("===============================")
                print(msj.mensaje_mantenimiento("dispensadores"))
                print("===============================")
                continue
        operacionview.seleccionar_operaciones(opc_menu=opc_menu)
