# Cajero Automático Básico
Proyecto final para la universidad

## Arquitectura
- MVC: Lo primero que se realicé es la creación de las carpetas para tener ordenado, por el momento esta arquitectura se acopla mejor, con forme los avances quizás se cambie a otra arquitectura.

### Carpetas

#### Common
Funciones globales que se repetiran constantemente.
- Validacion
  - Mensaje validación por selección de menú.
  - Mensaje validación por dato ingresado.
  - Verificar si el valor ingresado solo tiene un punto decimal.

#### Controller
Funciones que utilizaré en los archivos de View.
- MenuController
  - Listado del Menú Principal.
- OperacionController
  - Listado de las Operaciones de acuerdo a la selección del Menú Principal.
  - Listado de las opciones de los formularios por Operación.
- ClienteController
  - Registrar Cliente
  - Listar Cliente
  - Modificar Cliente
  - Consultar por código
  - Listado por estado

#### View
- MenuView
  - Seleccionar Menú Principal

- operaciones_view
  - Seleccionar Formulario para Administrador (Cliente 100% - Dispensador 0%)
  - Seleccionar Formulario para Cliente 0%


- administrador_view: aún está al 50%
  - Seleccionar Acciones para Clientes: 100%
  - Seleccionar Acciones para Dispensador: 0%
  - Funciones de las acciones para Clientes: 100%
  - Funciones de las acciones para Dispensadores: 0%


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
