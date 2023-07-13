"""Vista para las Operaciones de Pagar Servicio"""
# region importaciones
from colorama import Fore, Style
import Common.mensaje as mensaje
# endregion

msj = mensaje.Mensaje()

# region Formulario Pago Servicio
def frm_registrar_pago_servicio():
    """Rgistro del Pago de Servicio"""
    print(Style.BRIGHT + Fore.YELLOW)
    print("==============================")
    print(msj.mensaje_mantenimiento("Operación Pago de Servicio"))
    print("==============================")
    print(Style.NORMAL + Fore.WHITE)
# endregion
