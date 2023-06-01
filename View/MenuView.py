"""Módulo de la Vista del Menú"""
# region Importaciones
import Common.mensaje as mensaje
import Common.Validacion as validacion
import Controller.MenuController as menucontroller
import View.operaciones_view as operacionview
# endregion
msj = mensaje.Mensaje()
# region Funciones para seleccionar
def selecciona_menu():
    """Función para seleccionar opción del menú principal"""
    inicio = True
    cont = 0
    while inicio:
        try:
            print()
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
    """Incia el Sistema"""
    print("")
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
        operacionview.seleccionar_operaciones(opc_menu=opc_menu)
