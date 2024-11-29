# Historias de usuario

* * *

## Historia de Usuario 1: Selección de Fechas

### Descripción

**Como** usuario de la aplicación  
**Requiero** poder seleccionar fechas de manera fácil usando un calendario en la interfaz gráfica  
**Para que** pueda registrar eventos o tareas de forma precisa y sin errores.  

### Criterios de aceptación

- Debe haber un widget de calendario disponible en la interfaz gráfica.
- Al seleccionar una fecha en el calendario, el sistema debe registrar correctamente la fecha seleccionada.
- El calendario debe ser visualmente claro y fácil de usar.

* * *
* * *

## Historia de Usuario 2: Consulta de Datos

### Descripción

**Como** usuario  
**Quiero** poder consultar datos almacenados (como información de usuarios y registros)  
**Para que** pueda visualizar la información relevante de manera rápida y ordenada.

### Criterios de aceptación

- La interfaz debe permitir realizar consultas de forma rápida y ordenada.
- Los resultados de la consulta deben mostrarse en una tabla o lista organizada.
- El usuario debe poder visualizar a los detalles completos de un registro al hacer clic en él.

* * *
* * *

## Historia de Usuario 3: Acceso a la Aplicación

### Descripción

**Como** usuario  
**Quiero** poder iniciar la aplicación de manera sencilla y rápida desde la terminal  
**Para que** pueda comenzar a gestionar mis datos sin complicaciones.

### Criterios de aceptación

- El usuario debe poder iniciar el servicio ejecutando el comando python app.py desde la terminal.
- El sistema debe iniciar correctamente sin errores y mostrar la ventana principal de la interfaz gráfica.
- En caso de faltar dependencias, el sistema debe indicar qué paquetes instalar.

* * *
* * *

## Historia de Usuario 4: Garantizar datos completos en reserva

### Descripción

**Como** usuario  
**Quiero** poder garantizar que las reservas que se realizan tengan toda la información necesaria  
**Para que** pueda mantener la información completa y poder garantizar la integridad de la reserva.

### Criterios de aceptación

- El sistema debe asegurar que todos los campos obligatorios (como nombre, cancha, fecha y hora de la reserva) se completen antes de permitir que el usuario finalice la reserva.
- Si algún campo obligatorio está vacío o incompleto, el sistema debe mostrar un mensaje claro indicando cuál es el campo faltante.

* * *
* * *

## Historia de Usuario 5: Formato de hora de reserva

### Descripción

**Como** usuario  
**Quiero** poder seleccionar la hora de una reserva en un formato de 24 horas  
**Para que** pueda registrar la hora de manera precisa.

### Criterios de aceptación

- El sistema debe permitir al usuario seleccionar la hora de una reserva en un formato de 24 horas.
- La interfaz gráfica debe mostrar claramente el formato de la hora (por ejemplo, 13:00 en lugar de 1:00 PM).
- Al registrar la reserva, el sistema debe almacenar la hora en formato de 24 horas en la base de datos.
