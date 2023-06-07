# Cajero Automático Básico
Proyecto final para la universidad

[![Board Status](https://yeltsinbaltodano.visualstudio.com/599a5088-ab0a-43ee-ae27-de71707765cf/7a27677b-3c75-437a-aae7-234aaf5d16e2/_apis/work/boardbadge/cde23116-46d8-464a-bc43-37135218ab19?columnOptions=1)](https://yeltsinbaltodano.visualstudio.com/599a5088-ab0a-43ee-ae27-de71707765cf/_boards/board/t/7a27677b-3c75-437a-aae7-234aaf5d16e2/Stories/)

## Arquitectura
- MVC: Lo primero que se realicé es la creación de las carpetas para tener ordenado, por el momento esta arquitectura se acopla mejor, con forme los avances quizás se cambie a otra arquitectura.
- MVVM: Cambié la arquitectura de MVC a MVVM haciendo la pruebas y cambios para Clientes.

### Carpetas

### Api
Simular que hay un servicio que devuelve los datos.
- Lista del Dispensador
- Lista de Clientes
- Lista de Depósitos
- Lista de Retiros

#### Common
Funciones globales que se repetiran constantemente.
- Validacion
  - Mensaje validación por selección de menú.
  - Mensaje validación por dato ingresado.
  - Verificar si el valor ingresado solo tiene un punto decimal.
- Mensaje
  - Mensaje de inicio de formulario.
  - Mensaje de éxito.
  - Mensaje de Errores.

#### Model
- Cliente
  - Clase Persona
  - Clase Cliente
- Dispensador
  - Clase Dispensador
- Depositar
  - Clase Depositar
- Retirar
  - Clase Retirar

#### ViewModel
- Cliente_ViewModel: clase con funciones para el cliente
  - Listar Cliente
  - Registrar Cliente
  - Verificar Cliente por Código
  - Modificar Cliente
  - Buscar Cliente por Código
  - Listar Cliente por Estado
  - Verificar Cliente por Código y Clave
- Dispensador_ViewModel: clase con funciones para el dispensador
  - Listar Dispensador
  - Registrar Dispensador
  - Verificar Dispensador por Código
  - Modificar Dispensador
  - Buscar Dispensador por Código
  - Listar Dispensador por Estado
  - Verificar Monto Dispensador
- Depositar_ViewModel: clase con función para el depósito
  - Registro Depósito
  - Agregar Billetes al Dispensador
  - Lista Depósito
  - Modificar Depósito
  - Buscar Depósito
- Retirar_ViewModel: clase con función para el retiro
  - Registro Retiro
  - Modificar Billetes del Dispensador
  - Modificar Billetes del Depósito
  - Buscar Retiro por código Cliente

#### Controller
Funciones que utilizaré en los archivos de View.
- MenuController
  - Listado del Menú Principal.
- OperacionController
  - Listado de las Operaciones de acuerdo a la selección del Menú Principal.
  - Listado de las opciones de los formularios por Operación.
- ClienteController: conexión del Cliente_ViewModel para pasarlo a la vista
  - Registro Cliente
  - Listado Cliente
  - Verificar Cliente por Código
  - Modificar Cliente
  - Buscar Cliente por código
  - Listado Cliente por estado
  - Verificar Cliente por Código y Clave
- dispensador_controller
  - Registrar Dispensador
  - Listado Dispensador
  - Verificar Dispensador por Código
  - Modificar Dispensador
  - Buscar Dispensador por Código
  - Listado Dispensador por estado
  - Verificar Monto Dispensador
- depositar_controller
  - Registro Depósito
  - Buscar Depósito por Código
- retirar_controller
  - Registro Retiro
  - Buscar Retiro

#### View
- MenuView
  - Seleccionar Menú Principal

- operaciones_view
  - Seleccionar Formulario para Administrador (Cliente 100% - Dispensador 100%)
  - Seleccionar Formulario para Cliente 36%

- administrador_view:
  - Seleccionar Acciones del Formulario de Clientes: 100%
  - Seleccionar Acciones del Formulario del Dispensador: 100%

- operacion_cliente_view: 36%
  - Seleccionar formulario para operaciones del cliente

- operacion_cliente:
  - cliente_depositar_view:
    - Registrar Depósito
    - Vista Previa Registro
  - cliente_retirar_view:
    - Registrar Retiro
    - Detalle Retiro
  - cliente_consultar_saldo:
    - Consultar Saldo
    - Opciones Consulta
  - cliente_consulta_movimiento:
    - Consulta movimiento

### Formulario

#### Menú Principal
Las opciones del Menú principal son:
- Cliente
- Administrador
- Salir

#### Operaciones
Las operaciones si dividen en 2 por el tipo de Menú Principal:
- Operaciones por Cliente
  - Depositar
  - Retirar
  - Transferir
  - Pagar Servicio
  - Consultar Saldo
  - Consultar Movimiento
  - Salir
- Operaciones por Administrador
  - Gestionar Clientes
  - Gestionar Dispensador
  - Salir

#### Acciones de los Formularios de Operaciones por Administrador
Las acciones de los formularios de Operaciones por Administrador son los mismos para ambos:
- Agregar
- Modificar
- Consultar
- Estado
- Listar

[//]: # (Enlaces)
