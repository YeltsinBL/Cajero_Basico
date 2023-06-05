"""Vista para las Operaciones por Cliente"""
# region importaciones
import View.operacion_cliente.cliente_depositar_view as clientedepositar
import View.operacion_cliente.cliente_retirar_view as clienteretirar
import View.operacion_cliente.cliente_consultar_saldo as clientesaldo
import View.operacion_cliente.cliente_consulta_movimiento as clientemovimiento
# endregion

# region Función de Seleccionar Formulario
def seleccion_formulario_operacion_cliente(opc_operacion):
    """Selección del Formulario"""
    match opc_operacion:
        case 1: clientedepositar.frm_registrar_deposito()
        case 2: clienteretirar.frm_registrar_retiro()
        case 3: pass
        case 4: pass
        case 5: clientesaldo.frm_consulta_saldo()
        case 6: clientemovimiento.frm_consulta_movimiento()
# endregion