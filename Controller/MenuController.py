import Model.Menu as menu

def listado_menu():
    """Muestra las opciones del menú principal"""
    for idk, valor in menu.opcion_fuera.items():
        print(idk,valor)
