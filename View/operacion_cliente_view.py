"""Vista para las Operaciones por Cliente"""
# region importaciones
import View.operacion_cliente.cliente_depositar_view as clientedepositar
# endregion

# region Función de Seleccionar Formulario
def seleccion_formulario_operacion_cliente(opc_operacion):
    """Selección del Formulario"""
    match opc_operacion:
        case 1: clientedepositar.frm_registrar_deposito()
        case 2: pass
        case 3: pass
        case 4: pass
        case 5: pass
        case 6: pass
# endregion
