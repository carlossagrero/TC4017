# 🏨 Sistema de Gestión de Hoteles

Sistema completo de gestión de hoteles, clientes y reservaciones. Incluye validación de datos, persistencia en JSON y suite completa de pruebas unitarias e integración.

## 🎯 Características Principales

### ✅ Gestión de Clientes
- Crear, buscar, modificar y eliminar clientes
- Validación de email en tiempo real
- Búsqueda por ID
- Borrado lógico (marca como inactivo)

### ✅ Gestión de Hoteles
- Crear, buscar, modificar y eliminar hoteles
- Registro de ciudad y número de habitaciones
- Búsqueda por ID
- Validación de números positivos

### ✅ Gestión de Reservaciones
- Crear reservaciones vinculando cliente + hotel
- Validación de existencia de cliente y hotel
- Búsqueda y cancelación de reservaciones
- Persistencia automática de datos

### ✅ Persistencia
- Almacenamiento en JSON (`data/bd.json`)
- Carga y guardado automático
- Manejo robusto de errores de I/O

---

## 🏗️ Arquitectura

### Capas del Sistema

```
┌─────────────────────────────────────────────────────┐
│       Interfaz de Usuario (GUI - Tkinter)           │
│          HotelManagementApp (app_desktop.py)        │
└─────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────┐
│          Capa de Servicios (Business Logic)         │
├──────────────────┬──────────────────┬───────────────┤
│ CustomerService │ HotelService      │ ReservationSv │
└──────────────────┴──────────────────┴───────────────┘
                        ↓
┌─────────────────────────────────────────────────────┐
│            Capa de Modelos (Entidades)              │
├──────────────────┬──────────────────┬───────────────┤
│    Customer      │      Hotel       │   Reservation │
└──────────────────┴──────────────────┴───────────────┘
                        ↓
┌─────────────────────────────────────────────────────┐
│         Capa de Persistencia (JSON Storage)         │
│          AlmacenJson (almacen_json.py)             │
└─────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────┐
│          data/bd.json (Archivo de Datos)            │
└─────────────────────────────────────────────────────┘
```

---

## 📊 Calidad de Código

### Métricas de Calidad (2026-02-20)

| Herramienta | Métrica | Estado |
|-------------|---------|--------|
| **pylint** | Puntuación | 9.64/10 ✅ |
| **pylint** | Too many instance attributes | ✅ Corregido |
| **pylint** | Catching too general exception | ✅ Corregido |
| **pylint** | Too few public methods | ✅ Corregido |
| **flake8** | Line too long (E501) | ✅ 0 violations |
| **pytest** | Tests pasados | 88/88 ✅ |
| **coverage** | Cobertura total | 84%+ ✅ |

### Mejoras Implementadas

1. **Widget Registry Pattern** (`app_desktop.py`)
   - Consolidación de referencias de widgets en diccionario anidado
   - Reduce from 11+ instance attributes a 3 top-level dicts
   - Mejora legibilidad y mantenibilidad

2. **Manejo Específico de Excepciones**
   - Reemplazados `except Exception` con tuplas específicas
   - `except (ValueError, KeyError, TypeError)`
   - Mejor discriminación de errores

3. **Cumplimiento de Flake8**
   - Todas las líneas ≤79 caracteres
   - Wrapped method signatures y string literals
   - 65 violaciones → 0 violaciones

4. **API Pública**
   - Agregadas métodos `run()` y `close()` a `HotelManagementApp`
   - Permite uso como librería y testing directo

### Pruebas Unitarias e Integración

```
Total Pruebas: 88 ✅
├── test_customer.py              [12 tests] ✅
├── test_customer_service.py      [13 tests] ✅
├── test_hotel.py                 [12 tests] ✅
├── test_hotel_service.py         [14 tests] ✅
├── test_reservation.py           [12 tests] ✅
├── test_reservation_service.py   [13 tests] ✅
└── test_integracion.py           [12 tests] ✅

Cobertura:
├── almacen_json.py               96.08% ✅
├── customer_service.py           78.38% ✅
├── hotel_service.py              80.88% ✅
├── reservation_service.py        100.0% ✅
├── Modelos                       ~91%  ✅
└── TOTAL                         84.36% ✅
```

---

## 🚀 Instalación y Uso

### Requisitos Previos
- Python 3.8+
- pip (gestor de paquetes)
- Poetry (opcional, para dependencias)

### Instalación

```bash
# Clonar o descargar el repositorio
cd ruta/del/proyecto

# Instalar dependencias
poetry install
# O con pip:
pip install -r requirements.txt  # si existe
```

### Ejecutar la Aplicación

```bash
# Opción 1: Script ejecutable (Recomendado)
src/ejecutar_app.sh

# Opción 2: Comando Python
python -m src.app_desktop

# Opción 3: Importar y ejecutar
python -c "from src.app_desktop import main; main()"
```

### Ejecutar Pruebas

```bash
# Todas las pruebas con cobertura
./src/ejecutar_pruebas.sh

# O con pytest directo:
pytest tests/ -v --cov=src --cov-report=term-missing

# Pruebas de módulo específico:
pytest tests/test_customer.py -v
pytest tests/test_hotel.py -v
pytest tests/test_reservation.py -v
```

### Validar Calidad del Código

```bash
# Análisis con pylint
./src/ejecuta_calidad.sh

# O ejecutar herramientas por separado:
pylint src/
flake8 src/
```

---

## 📁 Estructura del Proyecto

```
a01796826_a6_2/
│
├── src/
│   ├── app_desktop.py              (835 líneas) - GUI principal
│   ├── __main__.py                 (5 líneas)   - Entry point
│   ├── customer.py                 (72 líneas)  - Modelo Cliente
│   ├── customer_service.py         (166 líneas) - Servicio Cliente
│   ├── hotel.py                    (75 líneas)  - Modelo Hotel
│   ├── hotel_service.py            (260 líneas) - Servicio Hotel
│   ├── reservation.py              (70 líneas)  - Modelo Reservación
│   ├── reservation_service.py      (145 líneas) - Servicio Reservación
│   ├── almacen_json.py             (136 líneas) - Persistencia JSON
│   ├── ejecutar_app.sh             - Ejecutar aplicación
│   ├── ejecutar_pruebas.sh         - Ejecutar pruebas
│   └── ejecuta_calidad.sh          - Validar calidad
│
├── data/
│   └── bd.json                     - Base de datos JSON
│
├── tests/
│   ├── test_customer.py            - Pruebas unitarias Cliente
│   ├── test_customer_service.py    - Pruebas unitarias CustomerService
│   ├── test_hotel.py               - Pruebas unitarias Hotel
│   ├── test_hotel_service.py       - Pruebas unitarias HotelService
│   ├── test_reservation.py         - Pruebas unitarias Reservación
│   ├── test_reservation_service.py - Pruebas unitarias ReservationService
│   ├── test_integracion.py         - Pruebas integración
│   └── conftest.py                 - Configuración pytest
│
├── test_reports/
│   └── test_report_log.txt         - Reporte de pruebas
│
├── docs/
│   └── (documentación adicional)
│
├── README.md                       - Este archivo
├── ARQUITECTURA.md                 - Diseño del sistema
├── CAMBIOS.md                      - Registro de cambios
├── CHANGELOG.md                    - Versiones del proyecto
├── DESKTOP_APP_README.md           - Guía de la aplicación
├── GUIA_RAPIDA.md                  - Tutorial de inicio rápido
├── IMPLEMENTACION.md               - Resumen técnico
├── LEEME.md                        - Resumen ejecutivo
│
├── pyproject.toml                  - Configuración Poetry
├── poetry.lock                     - Lock de dependencias
├── .coveragerc                     - Configuración de cobertura
└── .gitignore                      - Archivos ignorados por Git
```

---

## 🔧 Detalles Técnicos

### Patrón de Diseño: Widget Registry

En `app_desktop.py`, los widgets de la interfaz se organizan en un diccionario anidado:

```python
self.widgets = {
    "customers": {},   # widgets de clientes
    "hotels": {},      # widgets de hoteles
    "reservations": {} # widgets de reservaciones
}
```

**Ventajas:**
- Reduce instance attributes de 11+ a 3
- Mejor organización lógica
- Facilita acceso y actualización
- Cumple límites de pylint

### Manejo de Excepciones

Se utilizan tuplas de excepciones específicas:

```python
try:
    # operación que puede fallar
except (ValueError, KeyError, TypeError) as e:
    # manejar error específico
    messagebox.showerror("Error", str(e))
```

**Beneficios:**
- Excepciones específicas y predecibles
- Mejor debugging y logging
- Código más seguro y mantenible

### Cumplimiento de PEP8 (flake8)

Todas las líneas respetan el límite de 79 caracteres:

```python
# Mal (>79 caracteres)
self.label = tk.Label(self.frame, text="Texto muy largo que excede el límite de 79 caracteres permitido")

# Bien (wrapped)
self.label = tk.Label(
    self.frame,
    text="Texto muy largo que se divide "
         "en múltiples líneas para cumplir"
)
```

---

## 📚 Documentación

- **[ARQUITECTURA.md](ARQUITECTURA.md)** - Diagrama de capas y flujo de datos
- **[IMPLEMENTACION.md](IMPLEMENTACION.md)** - Detalles de implementación
- **[DESKTOP_APP_README.md](DESKTOP_APP_README.md)** - Guía de uso de la GUI
- **[GUIA_RAPIDA.md](GUIA_RAPIDA.md)** - Tutorial paso a paso
- **[CAMBIOS.md](CAMBIOS.md)** - Registro de cambios realizados
- **[LEEME.md](LEEME.md)** - Resumen ejecutivo

---

## 🐛 Troubleshooting

### La aplicación no inicia
```bash
# Verificar versión de Python
python --version  # Debe ser 3.8+

# Verificar Tkinter disponible
python -m tkinter

# Si falta Tkinter:
# macOS: brew install python-tk@3.9
# Linux: sudo apt-get install python3-tk
# Windows: Reinstalar Python con tcl/tk
```

### Los datos no se guardan
```bash
# Verificar que data/ existe
ls -la data/

# Si no existe, crear
mkdir data
python -m src.app_desktop
```

### Errores en pruebas
```bash
# Reinstalar dependencias
poetry install --no-cache

# Limpiar caché de pytest
rm -rf .pytest_cache/
rm -rf __pycache__/

# Ejecutar pruebas de nuevo
./src/ejecutar_pruebas.sh
```

---

## 👨‍💻 Desarrollo

### Agregar Nuevo Modelo

1. Crear clase en `src/nuevo_modelo.py`
2. Crear servicio en `src/nuevo_modelo_service.py`
3. Agregar tests en `tests/test_nuevo_modelo.py`
4. Integrar en `app_desktop.py`

### Ejecutar Análisis de Calidad

```bash
# Ejecutar herramientas de calidad
./src/ejecuta_calidad.sh

# O individual:
pylint src/ --disable=all --enable=too-many-instance-attributes,too-few-public-methods,catching-too-general-exception
flake8 src/ --select=E501
```

---

## 📝 Licencia

Proyecto académico para TC4017 - Pruebas de software y aseguramiento de la calidad.

---

## 📧 Contacto

Para preguntas o sugerencias sobre el proyecto, contactar al desarrollador.

**Última actualización:** 2026-02-20  
**Versión:** 0.4.0  
**Estado:** ✅ Completo y probado
