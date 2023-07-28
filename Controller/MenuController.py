"""Función que interactúa con la opción del Menú"""
# region Imports
import ViewModel.menu_viewmodel as menuviewmodel
#endregion

menu_vm = menuviewmodel.MenuViewModel()

def listar_menu(codigo):
    """Listado de los Menús"""
    return menu_vm.listar_menu(codigo)
