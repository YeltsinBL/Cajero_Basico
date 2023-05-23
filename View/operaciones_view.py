"""Vista del menú de operaciones"""
# region Importaciones
import Controller.OperacionController as operacioncontroller
import Common.Validacion as validacion
import View.administrador_view as administradorview
#import View.MenuView as menuview
# endregion

# region Funciones de Opciones
def selecciona_operacion(nromenu):
    """Opción para escoger el formulario"""
    inicio = True
    cont = 0
    while inicio:
        try:
            print("Ingresa el número de operación a realizar:")
            operacioncontroller.listado_opciones_por_menu(nromenu)
            nro_operacion = int(input(""))
            cant = operacioncontroller.cantidad_opciones_por_menu(nromenu)
            if cant < nro_operacion or nro_operacion < 1:
                cont += 1
                inicio = validacion.mensaje_validacion(cont)
                continue
            return nro_operacion
        except (ValueError, TypeError):
            cont +=1
            inicio = validacion.mensaje_validacion(cont)

# def seleccionar_acciones_formulario_operacion():
#     """Opción para Mostrar las acciones de los formularios"""
#     inicio = True
#     cont = 0
#     while inicio:
#         try:
#             print("Ingresa el número de la acción a realizar:")
#             operacioncontroller.listado_opciones_formulario()
#             cant_opc_form = operacioncontroller.cantidad_opciones_formulario()
#             nro_accion = int(input(""))
#             if cant_opc_form < nro_accion or nro_accion < 1:
#                 cont += 1
#                 inicio = validacion.mensaje_validacion(cont)
#                 continue
#             return nro_accion
#         except (ValueError, TypeError):
#             cont +=1
#             inicio = validacion.mensaje_validacion(cont)

# def seleccionar_acciones_formulario_operacion_inicial():
#     """Opción para Mostrar las acciones de los formularios"""
#     inicio = True
#     cont = 0
#     while inicio:
#         try:
#             print("Ingresa el número de la acción a realizar:")
#             print(1, "Agregar")
#             print(6, "Salir")
#             nro_accion = int(input(""))
#             if nro_accion == 6 or nro_accion == 1:
#                 return nro_accion
#             else:
#                 cont += 1
#                 inicio = validacion.mensaje_validacion(cont)
#                 continue
#         except (ValueError, TypeError):
#             cont +=1
#             inicio = validacion.mensaje_validacion(cont)

def mostrar_seleccionados(nromenu, nrooperacion, nroaccion):
    """Muestra los menu seleccionado"""
    nombre_seleccionado = operacioncontroller.opcion_seleccionada_por_menu(nromenu,nrooperacion)
    nombre_seleccionado += "-> " + operacioncontroller.opcion_seleccionado_formulario(nroaccion)
    print("Usted ha seleccionado estas opciones:" , nombre_seleccionado)
    print()

# endregion

#region Selección de Opciones
def seleccionar_operaciones(opc_menu):
    """Selección de las opciones de Operaciones"""
    iniciar_operacion = True
    while iniciar_operacion:
        opc_operacion= selecciona_operacion(opc_menu)
        if opc_operacion == operacioncontroller.cantidad_opciones_por_menu(opc_menu):
            iniciar_operacion = False
            break
        elif opc_menu == 2 :

            # iniciar_accion = True
            # while iniciar_accion:
            #     opc_accion : int|None
            #     if (opc_operacion == 1 and len(menuview.clientes) == 0) or \
            #         (opc_operacion == 2 and len(menuview.dispensadores) == 0):
            #         opc_accion = seleccionar_acciones_formulario_operacion_inicial()
            #     else:
            #         opc_accion = seleccionar_acciones_formulario_operacion()
            #     if opc_accion == 6:
            #         iniciar_accion = False
            #         break
            administradorview.seleccion_formulario(opc_operacion)
        else:
            print("Seleccionó Tipo Cliente")
#endregion
