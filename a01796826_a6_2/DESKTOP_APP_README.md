# Aplicación de Escritorio - Sistema de Gestión de Hoteles

**Versión:** 0.5.0  
**Estado:** ✅ Completa, Probada y Optimizada

## Descripción

Aplicación de escritorio que integra todas las funcionalidades del sistema de gestión de hoteles, clientes y reservaciones. Construida con Tkinter, optimizada según estándares de calidad de código (pylint 9.64/10, flake8 0 violations).

## Requisitos

- Python 3.8 o superior
- Tkinter (incluido en la mayoría de instalaciones de Python)

## Instalación

Si no tiene Tkinter instalado, puede instalarlo con:

**En macOS:**
```bash
brew install python-tk@3.9  # O reemplazar 3.9 con su versión de Python
```

**En Linux (Ubuntu/Debian):**
```bash
sudo apt-get install python3-tk
```

**En Windows:**
Tkinter viene incluido con Python. Si no lo tiene, reinstale Python seleccionando "tcl/tk and IDLE" en la instalación.

## Uso

### Opción 1: Script ejecutable (Recomendado)
```bash
src/ejecutar_app.sh
```

### Opción 2: Comando Python directo
```bash
python -m src.app_desktop
```

### Opción 3: Desde Python
```python
from src.app_desktop import main
main()
```

## Características

### Gestión de Clientes

- **Crear Cliente**: Ingrese nombre y email, haga clic en "Crear Cliente"
- **Buscar Cliente**: Ingrese el ID y haga clic en "Buscar Cliente"
- **Modificar Cliente**: Ingrese el ID, nombre y/o email nuevo, haga clic en "Modificar Cliente"
- **Eliminar Cliente**: Ingrese el ID y haga clic en "Eliminar Cliente" (borrado lógico)
- **Limpiar**: Limpia todos los campos

### Gestión de Hoteles

- **Crear Hotel**: Ingrese nombre, ciudad y total de habitaciones
- **Buscar Hotel**: Ingrese el ID del hotel
- **Modificar Hotel**: Ingrese el ID y los campos a actualizar
- **Eliminar Hotel**: Ingrese el ID para eliminarlo
- **Limpiar**: Limpia todos los campos

### Gestión de Reservaciones

- **Crear Reservación**: Ingrese ID de cliente e ID de hotel
- **Ver Reservación**: Busque por ID de reservación
- **Cancelar Reservación**: Ingrese ID de reservación para cancelarla
- **Limpiar**: Limpia todos los campos

## Validaciones

La aplicación realiza validaciones automáticas:

- **Email**: Debe contener "@" y "."
- **Habitaciones**: Debe ser un número entero positivo
- **IDs requeridos**: Los IDs de cliente y hotel deben existir para crear reservaciones
- **Campos obligatorios**: Se valida que los datos requeridos estén completos

## Persistencia de Datos

Los datos se almacenan automáticamente en `data/bd.json` en formato JSON. La aplicación carga y guarda datos automáticamente en cada operación.

## Estructura de Datos

### Cliente (Customer)
```json
{
  "id_customer": "uuid",
  "nombre": "string",
  "email": "string",
  "activo": boolean
}
```

### Hotel
```json
{
  "id_hotel": "uuid",
  "nombre": "string",
  "ciudad": "string",
  "total_habitaciones": integer,
  "activo": boolean
}
```

### Reservación
```json
{
  "id_reservation": "uuid",
  "id_customer": "uuid",
  "id_hotel": "uuid",
  "activo": boolean
}
```

## Notas Importantes

- Los IDs se generan automáticamente usando UUID4
- Los eliminar operaciones son "borrado lógico" (activo = false)
- La aplicación es multiplataforma (Windows, macOS, Linux)
- Los cambios se guardan inmediatamente en el archivo JSON

## Troubleshooting

Si la aplicación no inicia:

1. Verifique que Python 3.8+ está instalado: `python --version`
2. Verifique que Tkinter está disponible: `python -m tkinter`
3. Verifique que la carpeta `data/` existe
4. Si no existe la carpeta, créela: `mkdir data` y reinicie la aplicación
