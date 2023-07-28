"""Menú View Model"""
#region Import
from Data.conexion import conexion
#endregion

class MenuViewModel:
    """Clase Retirar ViewModel"""
    def __init__(self) -> None:
        pass
    def listar_menu(self, codigo):
        """Listado del Menú"""
        try:
            connection= conexion()
            cursor = connection.cursor()
            store_proc = "exec sp_Menu_Listar @intIdentificador=?"
            parametro = codigo
            cursor.execute(store_proc, parametro)
            resultset= cursor.fetchall()
            connection.close()
            return resultset
        except ImportError as ex:
            print(ex)
            return []
