"""Dispensador ViewModel"""
# region Importación
from Data.conexion import conexion
#endregion

class DispensadorViewModel:
    """Clase Dispensador ViewModel"""
    def __init__(self) -> None:
        pass
    def lista_dispensadores(self):
        """Lista de Dispensadores"""
        lista_dispensador = []
        try:
            connection= conexion()
            cursor = connection.cursor()
            cursor.execute("exec sp_Lista_Dispensador")
            resultset= cursor.fetchall()
            lista_dispensador = self.formaterar_datos(resultset)
            connection.close()
        except ImportError as ex:
            print(ex)
        return  lista_dispensador

    def registrar_dispensador(self, disp:dict[str,any]):
        """Registro Dispensador"""
        try:
            connection= conexion()
            cursor = connection.cursor()
            params = [disp.get("codigo"), disp.get("lugar")]
            for valor in disp.get("billete"):
                for _, vbillete in valor.items():
                    params.append(vbillete)
            store_proc = "exec sp_Registrar_Dispensador @strCodigo = ?,\
                @strLugar = ?, @intDoscientos = ?, @intCien= ?, @intCincuenta=?,\
                @intVeinte =?, @intDiez=?"
            cursor.execute(store_proc, params)
            cursor.commit()
            cursor.close()
        except ImportError as ex:
            print(ex)

    def modificar_dispensador(self, dicts:dict[str,any]):
        """Modificar Dispensador"""
        try:
            connection= conexion()
            cursor = connection.cursor()
            params = [dicts.get("codigo"), dicts.get("lugar"), dicts.get("estado")]
            for valor in dicts.get("billete"):
                for _, vbillete in valor.items():
                    params.append(vbillete)
            store_proc = "exec sp_Modificar_Dispensador @strCodigo = ?,\
                @strLugar = ?, @bitEstado =?, @intDoscientos = ?, @intCien= ?,\
                @intCincuenta=?, @intVeinte =?, @intDiez=?"
            cursor.execute(store_proc, params)
            cursor.commit()
            cursor.close()
            return True
        except ImportError as ex:
            print(ex)
            return False

    def buscar_dispensador_codigo(self, codigo):
        """Buscar Dispensador por Código"""
        try:
            connection= conexion()
            cursor = connection.cursor()
            store_proc = "exec sp_ListarDispensador_Codigo_Estado @strCodigo=?"
            params = codigo
            cursor.execute(store_proc, params)
            resultset= cursor.fetchall()
            connection.close()
            return self.formaterar_datos(resultset)
        except ImportError as ex:
            print(ex)
            return  []

    def lista_dispensador_estado(self, estado):
        """Listar los Dispensadores por su estado"""
        try:
            connection= conexion()
            cursor = connection.cursor()
            store_proc = "exec sp_ListarDispensador_Codigo_Estado @bitEstado=?"
            params = estado
            cursor.execute(store_proc, params)
            resultset= cursor.fetchall()
            connection.close()
            return self.formaterar_datos(resultset)
        except ImportError as ex:
            print(ex)
            return  []

    def verificar_monto_dispensador(self, codigo_dispensador:int, monto:float):
        """Verificar el Monto del Dispensador"""
        cantidad:float = 0
        lista_dispensador = self.lista_dispensadores()
        for dato in lista_dispensador:
            if dato.get("codigo") == codigo_dispensador:
                for valor in dato.get("billete"):
                    for nro_billete, vbillete in valor.items():
                        cantidad = cantidad +(nro_billete * vbillete)
        if cantidad >= monto:
            return True
        return False

    def agregar_billete_dispensador(self, cod_dispensador:int, lugar_dispensador:str,
                        estado_dispensador:str, billete:list):
        """Agregar billetes al dispensador"""
        nueva_lista=[]
        # Lista guardada del Dispensador
        respt_dispensador = self.buscar_dispensador_codigo(cod_dispensador)
        for result in respt_dispensador:
            for valor in result.get("billete"):
                for nro_billete, vbillete in valor.items():
                    # Lista de los nuevos valores de billetes para el Dispensdaor
                    for val_billete in billete:
                        for nro_billete2, vbillete2 in val_billete.items():
                            # Comparación de las claves de las listas para sumar sus valores
                            if nro_billete == nro_billete2:
                                nueva_lista.append({nro_billete: vbillete+vbillete2})
                                break
        disp={"codigo":cod_dispensador,"lugar":lugar_dispensador,
              "estado":estado_dispensador, "billete": nueva_lista}
        return self.modificar_dispensador(disp)

    def formaterar_datos(self, datos):
        """Formatear los datos  que llegan del SP"""
        lista_dispensador =[]
        for resultado in datos:
            billetes =[]
            billetes.append({200:int(resultado[4]), 100:int(resultado[5]),
                             50:int(resultado[6]), 20:int(resultado[7]),
                             10:int(resultado[8])})
            lista_dispensador.append({"codigo":int(resultado[1]),"lugar":resultado[2],
                                      "billete": billetes,"estado": resultado[3]})
        return lista_dispensador
        