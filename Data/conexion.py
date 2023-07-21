"""Conectar con SQL"""

import pyodbc
from Data.credencial import database, password, server, username

def conexion():
    """Conexión a SQL"""
    try:

        return pyodbc.connect('DRIVER={SQL Server};SERVER='+server+
                            ';DATABASE='+database+
                            ';UID='+username+
                            ';PWD='+ password)
    except ImportError:
        print("ERROR A LA CONEXIÓN")
        return None
