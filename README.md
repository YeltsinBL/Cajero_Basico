# Cajero Automático Básico

Versión final para presentar como proyecto final a la universidad.

[![Board Status](https://yeltsinbaltodano.visualstudio.com/599a5088-ab0a-43ee-ae27-de71707765cf/7a27677b-3c75-437a-aae7-234aaf5d16e2/_apis/work/boardbadge/cde23116-46d8-464a-bc43-37135218ab19?columnOptions=1)](https://yeltsinbaltodano.visualstudio.com/599a5088-ab0a-43ee-ae27-de71707765cf/_boards/board/t/7a27677b-3c75-437a-aae7-234aaf5d16e2/Stories/)

## Arquitectura

- MVC: Lo primero que se realicé es la creación de las carpetas para tener ordenado, por el momento esta arquitectura se acopla mejor, con forme los avances quizás se cambie a otra arquitectura.
- MVVM: Cambié la arquitectura de MVC a MVVM haciendo la pruebas y cambios para Clientes.

## Carpetas

### Data

Simular que hay un servicio que devuelve los datos.

- Lista del Dispensador
- Lista de Clientes
- Lista de Depósitos
- Lista de Retiros
- Lista de Transferencia
- Lista de Cuenta Cliente

### Common

Funciones globales que se repetiran constantemente.

- Validacion
  - Mensaje validación por selección de menú.
  - Mensaje validación por dato ingresado (string, decimal, int).
  - Verificar si el valor ingresado solo tiene un punto decimal.
- Mensaje
  - Mensaje de inicio de formulario.
  - Mensaje de éxito.
  - Mensaje de Errores.
  - Mensaje de Validaciones.
- Elemento
  - Ingresar código cliente
  - Ingresar clave cliente
  - Ingresar código dispensador
  - Ingresar monto
  - Ingresar cantidad billetes
  - Ingresar lugar
  - Ingresar estado

### Model

- Cliente
  - Clase Persona
  - Clase Cliente
- Dispensador
  - Clase Dispensador
- Depositar
  - Clase Depositar
- Retirar
  - Clase Retirar
- Transferencia
  - Clase Transferencia
- Cuenta Cliente
  - Clase Cuenta Cliente

### ViewModel

- Cliente_ViewModel: clase con funciones para el cliente
  - Listar Cliente: utilización del ordenamiento de burbuja
  - Registrar Cliente
  - Verificar Cliente por Código
  - Modificar Cliente
  - Buscar Cliente por Código
  - Listar Cliente por Estado
  - Verificar Cliente por Código y Clave
  - Modificar el saldo del cliente
- Dispensador_ViewModel: clase con funciones para el dispensador
  - Listar Dispensador
  - Registrar Dispensador
  - Verificar Dispensador por Código
  - Modificar Dispensador
  - Buscar Dispensador por Código
  - Listar Dispensador por Estado
  - Verificar Monto Dispensador
  - Agregar Billetes al dispensdor
- Depositar_ViewModel: clase con función para el depósito
  - Registro Depósito
  - Lista Depósito
  - Buscar Depósito
- Retirar_ViewModel: clase con función para el retiro
  - Registro Retiro
  - Calcular los Billetes que se moodificarán en el Dispensador
  - Buscar Retiro por código Cliente
- Transferencia_ViewModel: clase con función para la transferencia
  - Registro Transferencia
  - Lista Transferencia
  - Buscar Transferencia por Código Cliente
- cuenta_cliente_viewmodel: clase con función para la transferencia
  - Registro de la cuenta del cliente
  - Lista de la cuenta del cliente
  - Modificar la cuenta del cliente
  - Modificar el saldo de cuenta del cliente
  - Buscar la cuenta del ciente por código de dispensador y código del cliente
  - Verificar la cuenta del cliente

### Controller

Funciones que utilizaré en los archivos de View.

- MenuController
  - Listado del Menú Principal.
- OperacionController
  - Listado de las Operaciones de acuerdo a la selección del Menú Principal.
  - Listado de las opciones de los formularios por Operación.
  - Listado de las opciones de estado de cliente.
  - Cantidad de operaciones del menú principal y formulario.
  - Muestra las opciones que selecionó del menú principal y formulario.
- ClienteController
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
- transferencia_controller
  - Registro Transferencia
  - Buscar Transferencia
- cuenta_cliente_controller
  - Buscar el saldo de la cuenta del cliente
  - Verificar el monto de la cuenta del cliente

### View

- MenuView

  - Inicio del Sistema
  - Seleccionar Menú Principal

- operaciones_view
  - Mostrar y seleccionar opciones para Administrador o Cliente

- administrador_view:
  - Mostrar opciones de acciones de acuerdo a los datos
  - Seleccionar Acciones de los Formularios de Clientes y Dispensador

- operacion_administrador
  - Gestionar Cliente
    - Muestra los campos que tienen cada formulario para guardar los datos
  - Gestionar Dispensador
    - Muestra los campos que tienen cada formulario para guardar los datos

- operacion_cliente_view
  - Seleccionar formulario para operaciones del cliente

- operacion_cliente:
  - cliente_depositar_view:
    - Registrar Depósito
    - Vista Previa Registro
  - cliente_retirar_view:
    - Registrar Retiro
    - Detalle Retiro
  - cliente_transferir:
    - Registrar Transferencia
  - cliente_consultar_saldo:
    - Consultar Saldo
    - Opciones Consulta
  - cliente_consulta_movimiento:
    - Consulta movimiento

## Funcionalidad

### Menú Principal

Las opciones del Menú principal son:

- Cliente
- Administrador
- Salir

### Operaciones

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

### Acciones de los Formularios de Operaciones por Administrador

Las acciones de los formularios de Operaciones por Administrador son los mismos para ambos:

- Agregar
- Modificar
- Consultar
- Estado
- Listar

> Nota: Existen casos para realizar mejoras, pero esas mejoras se agregarán en las siguientes ramas de este repositorio.

[//]: # (Enlaces)
