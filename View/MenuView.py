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
        lista_menu =[]
        nueva_lista={}
        nombre_lista={}
        if len(lista_menu)==0:
            lista_menu = menucontroller.listar_menu(1)
        for resultado in lista_menu:
            print(resultado[0], resultado[1])
            nueva_lista[resultado[0]]=resultado[2]
            nombre_lista[resultado[0]]=resultado[1]
        nro_menu = input("")
        if nro_menu.isdigit() and int(nro_menu) \
            in list(range(len(lista_menu)+1)):
            return nueva_lista.get(int(nro_menu)), nombre_lista.get(int(nro_menu))
        print(list(range(len(lista_menu)+1)))
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
        opc_menu, nombre = selecciona_menu()
        if opc_menu == 0:
            msj.mensaje_despedida()
            iniciar_principal = False
            break
        if opc_menu == 2:
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
        operacionview.seleccionar_operaciones(opc_menu=opc_menu, nombre_seleccion=nombre)
