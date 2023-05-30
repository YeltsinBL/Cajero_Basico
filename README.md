# Cajero Automático Básico
Proyecto final para la universidad

## Arquitectura
- MVC: Lo primero que se realicé es la creación de las carpetas para tener ordenado, por el momento esta arquitectura se acopla mejor, con forme los avances quizás se cambie a otra arquitectura.
- MVVM: Cambié la arquitectura de MVC a MVVM haciendo la pruebas y cambios para Clientes.

### Carpetas

### Api
Simular que hay un servicio que devuelve los datos.
- Lista del Dispensador
- Lista de Clientes

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

#### ViewModel
- Cliente_ViewModel: clase con funciones para el cliente
  - Listar Cliente
  - Registrar Cliente
  - Verificar Cliente por Código
  - Modificar Cliente
  - Buscar Cliente por Código
  - Listar Cliente por Estado

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
- dispensador_controller
  - Registrar Cliente
  - Listar Cliente
  - Modificar Cliente
  - Consultar por código
  - Listado por estado

#### View
- MenuView
  - Seleccionar Menú Principal

- operaciones_view
  - Seleccionar Formulario para Administrador (Cliente 100% - Dispensador 100%)
  - Seleccionar Formulario para Cliente 0%

- administrador_view:
  - Seleccionar Acciones del Formulario de Clientes: 100%
  - Seleccionar Acciones para Dispensador: 100%

- operacion_cliente_view: 0%

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
