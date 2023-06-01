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
- Retirar_ViewModel: clase con función para el retiro
  - Registro Retiro
  - Actualizar Billetes al Dispensador

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
- retirar_controller
  - Registro Retiro

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
