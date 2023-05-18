# Cajero Automático Básico
Proyecto final para la universidad

## Arquitectura
- MVC: Lo primero que se realicé es la creación de las carpetas para tener ordenado, por el momento esta arquitectura se acopla mejor, con forme los avances quizás se cambie a otra arquitectura.

### Carpetas

#### Common
Funciones globales que se repetiran constantemente.
- Validacion
  - Mensaje validación por dato ingresado

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

#### View
- MenuView: aún no está separado las acciones e ingreso de datos.
  - Seleccionar Menú Principal
  - Seleccionar Operación
  - Seleccionar Acción de Formulario

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
