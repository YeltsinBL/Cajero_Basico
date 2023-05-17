import sys

import Controller.MenuController as menucontroller

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
