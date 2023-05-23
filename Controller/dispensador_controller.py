"""Funciones que interactúan con los datos del Dispensador """

# region Importación
import Common.Validacion as validacion
import Api.service as service
#endregion

# region Funciones
def registrar_dispensador():
    """Función de Registro de Dispensadores"""
    print("REGISTRO DEL DISPENSADOR")
    print("Ingrese la información")
    vali_lugar = True
    vali_billetes= True
    vali_bill_200=True
    vali_bill_100=True
    vali_bill_50=True
    vali_bill_20=True
    vali_bill_10=True
    cant_disp= len(service.dispensadores)
    billetes=[]
    while vali_lugar:
        lugar = input("LUGAR: ")
        vali_lugar = not validacion.valores_ingresados("lugar",lugar,3)
    while vali_billetes:
        print("Cantidad de Billetes")
        while vali_bill_200:
            billete_200 = input("Billetes de 200: ")
            vali_bill_200 = not validacion.valores_ingresados("billetes de 200",billete_200,1)
        while vali_bill_100:
            billete_100 = input("Billetes de 100: ")
            vali_bill_100 = not validacion.valores_ingresados("billetes de 100",billete_100,1)
        while vali_bill_50:
            billete_50 = input("Billetes de 50: ")
            vali_bill_50 = not validacion.valores_ingresados("billetes de 50",billete_50,1)
        while vali_bill_20:
            billete_20 = input("Billetes de 20: ")
            vali_bill_20 = not validacion.valores_ingresados("billetes de 20",billete_20,1)
        while vali_bill_10:
            billete_10 = input("Billetes de 10: ")
            vali_bill_10 = not validacion.valores_ingresados("billetes de 10",billete_10,1)
        billetes.append({200:billete_200, 100:billete_100, 50:billete_50, 20:billete_20,\
                         10:billete_10})
        vali_billetes = False
    service.dispensadores.append({"codigo":cant_disp+1,"lugar":lugar, "billetes": billetes,\
                                  "estado": "Activo"})
    #return True

def listado_dispensadores():
    """Muestra las dispensadores registrados"""
    cantidad = 0
    print("LISTADO DE LOS DISPENSADORES")
    for dato in service.dispensadores:
        cantidad += 1
        print(f"DISPENSADOR NRO. {cantidad}")
        for idx, valor in dato.items():
            if idx == "billetes":
                print("BILLETES:")
                for billete in valor:
                    for nro_billete, vbillete in billete.items():
                        print(str(nro_billete).upper()+ ": ",vbillete)
            else: print(str(idx).upper()+ ": ",valor)

def modificar_dispensador():
    """Función para Modificar dispensador"""
    vali_cod = True
    while vali_cod:
        print("MODIFICAR dispensador")
        codigo_dispensador = input("CÓDIGO: ")
        vali_cod = not validacion.valores_ingresados("código",codigo_dispensador,1)
        for dato in service.dispensadores:
            if dato["codigo"]==int(codigo_dispensador):
                vali_lugar = True
                vali_billetes= True
                vali_bill_200=True
                vali_bill_100=True
                vali_bill_50=True
                vali_bill_20=True
                vali_bill_10=True
                vali_estado = True
                print("LUGAR ACTUAL:", dato["lugar"])
                while vali_lugar:
                    lugar = input("NUEVO LUGAR: ")
                    vali_lugar = not validacion.valores_ingresados("lugar",lugar,3)
                print("Cantidad de Billetes")
                while vali_billetes:
                    for dato_billete in dato["billetes"]:
                        print("BILLETES DE 200 ACTUAL:", dato_billete[200])
                        while vali_bill_200:
                            billete_200 = input("Billetes de 200: ")
                            vali_bill_200 = not validacion.valores_ingresados("billetes de 200",\
                                                                            billete_200,1)
                        print("BILLETES DE 100 ACTUAL:", dato_billete[100])
                        while vali_bill_100:
                            billete_100 = input("Billetes de 100: ")
                            vali_bill_100 = not validacion.valores_ingresados("billetes de 100",\
                                                                            billete_100,1)
                        print("BILLETES DE 50 ACTUAL:", dato_billete[50])
                        while vali_bill_50:
                            billete_50 = input("Billetes de 50: ")
                            vali_bill_50 = not validacion.valores_ingresados("billetes de 50",\
                                                                            billete_50,1)
                        print("BILLETES DE 20 ACTUAL:", dato_billete[20])
                        while vali_bill_20:
                            billete_20 = input("Billetes de 20: ")
                            vali_bill_20 = not validacion.valores_ingresados("billetes de 20",\
                                                                            billete_20,1)
                        print("BILLETES DE 10 ACTUAL:", dato_billete[10])
                        while vali_bill_10:
                            billete_10 = input("Billetes de 10: ")
                            vali_bill_10 = not validacion.valores_ingresados("billetes de 10",\
                                                                            billete_10,1)
                        dato_billete[200]=billete_200
                        dato_billete[100]=billete_100
                        dato_billete[50]=billete_50
                        dato_billete[20]=billete_20
                        dato_billete[10]=billete_10
                    vali_billetes = False
                print("ESTADO ACTUAL:", dato["estado"])
                while vali_estado:
                    estado = input("NUEVO ESTADO: ")
                    vali_estado = not validacion.valores_ingresados("estado",estado,5)
                dato["lugar"] = lugar
                dato["estado"] = estado.capitalize()
                return True
            else:
                vali_cod = True
                print("El CÓDIGO ingresado no existe")
                print("=======================================")
                print("")
                listado_dispensadores()
                print("=======================================")

def consultar_dispensador():
    """Función para Buscar un dispensador por su código"""
    print("CONSULTAR DISPENSADOR")
    vali_cod = True
    while vali_cod:
        codigo_dispensador = input("CÓDIGO: ")
        vali_cod = not validacion.valores_ingresados("código",codigo_dispensador,1)
    nueva = (x for x in service.dispensadores if x["codigo"]==int(codigo_dispensador))
    for dato in nueva:
        for idx, valor in dato.items():
            if idx == "billetes":
                print("BILLETES:")
                for billete in valor:
                    for nro_billete, vbillete in billete.items():
                        print(str(nro_billete).upper()+ ": ",vbillete)
            else: print(str(idx).upper()+ ": ",valor)

def activo_dispensador(nro_estado):
    """Función para Buscar los Dispensadores por estado"""
    cantidad = 0
    estado="activo" if nro_estado ==1 else "desactivo"
    print("DISPENSADORES", estado.upper()+"S")
    nueva = (x for x in service.dispensadores if x["estado"].lower()== estado)
    for dato in nueva:
        cantidad += 1
        print(f"DISPENSADOR NRO. {cantidad}")
        for idx, valor in dato.items():
            if idx == "billetes":
                print("BILLETES:")
                for billete in valor:
                    for nro_billete, vbillete in billete.items():
                        print(str(nro_billete).upper()+ ": ",vbillete)
            else: print(str(idx).upper()+ ": ",valor)

def lista_dispensadores():
    """Devuelve la lista de los dispensadores"""
    return service.dispensadores
# endregion
