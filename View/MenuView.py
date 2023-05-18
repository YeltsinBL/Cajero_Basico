import sys

import Controller.MenuController as menucontroller
import Controller.OperacionController as operacioncontroller

print("Bienvenido")
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
                if cont == 3:
                    print("Gracias por su visita")
                    inicio = False
                    sys.exit(0)
                intent = lambda cont : "intento" if(3-cont == 1) else "intentos"
                print("Ingresa un número del 1 al 3, por favor")
                print(f"Le queda {3 - cont}", intent(cont))
                continue
            return nro_menu
        except (ValueError, TypeError):
            cont +=1
            if cont < 3:
                intent = lambda cont : "intento" if(3-cont == 1) else "intentos"
                print("Ingresa un número del 1 al 3, por favor")
                print(f"Le queda {3 - cont}", intent(cont))
            else:
                print("Gracias por su visita")
                inicio = False
                sys.exit(0)

opc_menu = selecciona_menu()
def selecciona_operacion(nromenu):
    """Opción para escoger el formulario"""
    inicio = True
    cont = 0
    while inicio:
        try:
            print("Ingresa el número de operación a realizar:")
            operacioncontroller.listado_opciones_por_menu(nromenu)
            nro_operacion = int(input(""))
            if 3 < nro_operacion or nro_operacion < 1:
                cont += 1
                if cont == 3:
                    print("Gracias por su visita")
                    inicio = False
                    sys.exit(0)
                intent = lambda cont : "intento" if(3-cont == 1) else "intentos"
                print("Ingresa un número del 1 al 3, por favor")
                print(f"Le queda {3 - cont}", intent(cont))
                continue
            return nro_operacion
        except (ValueError, TypeError):
            cont +=1
            if cont < 3:
                intent = lambda cont : "intento" if(3-cont == 1) else "intentos"
                print("Ingresa un número del 1 al 3, por favor")
                print(f"Le queda {3 - cont}", intent(cont))
            else:
                print("Gracias por su visita")
                inicio = False
                sys.exit(0)

def seleccionar_acciones_formulario_operacion():
    """Opción para Mostrar las acciones de los formularios"""
    inicio = True
    cont = 0
    while inicio:
        try:
            print("Ingresa el número de la acción a realizar:")
            operacioncontroller.listado_opciones_formulario()
            cant_opc_form = operacioncontroller.cantidad_opciones_formulario()
            nro_accion = int(input(""))
            if cant_opc_form < nro_accion or nro_accion < 1:
                cont += 1
                if cont == 3:
                    print("Gracias por su visita")
                    inicio = False
                    sys.exit(0)
                intent = lambda cont : "intento" if(3-cont == 1) else "intentos"
                print(f"Ingresa un número del 1 al {cant_opc_form}, por favor")
                print(f"Le queda {3 - cont}", intent(cont) )
                continue
            return nro_accion
        except (ValueError, TypeError):
            cont +=1
            if cont < 3:
                intent = lambda cont : "intento" if(3-cont == 1) else "intentos"
                print(f"Ingresa un número del 1 al {cant_opc_form}, por favor")
                print(f"Le queda {3 - cont}", intent(cont) )
            else:
                print("Gracias por su visita")
                inicio = False
                sys.exit(0)

def mostrar_seleccionados(nromenu, nrooperacion, nroaccion):
    """Muestra los menu seleccionado"""
    nombre_seleccionado = operacioncontroller.opcion_seleccionada_por_menu(nromenu,nrooperacion)
    nombre_seleccionado += "-> " + operacioncontroller.opcion_seleccionado_formulario(nroaccion)
    print("Usted ha seleccionado estas opciones:" , nombre_seleccionado)
    print("Gracias por su visita")

opc_menu = selecciona_menu()
opc_operacion= selecciona_operacion(opc_menu)
opc_accion = seleccionar_acciones_formulario_operacion()
mostrar_seleccionados(opc_menu,opc_operacion,opc_accion)