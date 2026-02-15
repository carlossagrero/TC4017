# Sistema de Cálculo de Ventas

Sistema de procesamiento de ventas que calcula el costo total de transacciones a partir de un catálogo de precios y registros de ventas en formato JSON.

## 📋 Descripción del Proyecto

Este proyecto es parte de la asignatura **TC4017 - Pruebas de software y aseguramiento de la calidad** y consiste en un sistema que:

- Lee archivos JSON con catálogos de precios y registros de ventas
- Calcula el costo total de todas las ventas
- Genera reportes legibles para humanos
- Maneja datos inválidos de forma robusta
- Escala a cientos de miles de registros
- Mide y reporta el tiempo de ejecución
- Cumple con estándares PEP8

## 📁 Estructura del Proyecto

```
5.2/
├── data/                           # Archivos de datos
│   ├── priceCatalogue.json        # Catálogo de precios de productos
│   ├── salesRecord.json           # Registro de ventas (pequeño)
│   ├── salesRecord_100k.json      # Registro de ventas (100,000 renglones)
│   ├── TC2.Sales.json             # Casos de prueba 2
│   └── TC3.Sales.json             # Casos de prueba 3
├── source/                         # Código fuente
│   ├── computeSales.py            # Programa principal
│   ├── generar_ventas.py          # Generador de datos de prueba
│   └── ejecuta_programa.sh        # Script de ejecución y validación
├── results/                        # Resultados generados
│   ├── SalesResults.txt           # Reporte por defecto (sin parámetro)
│   ├── TC2.Sales_results.txt      # Resultados de TC2.Sales.json
│   ├── TC3.Sales_results.txt      # Resultados de TC3.Sales.json
│   ├── salesRecord_results.txt    # Resultados de salesRecord.json
│   └── salesRecord_100k_results.txt # Resultados de salesRecord_100k.json
├── general_results/                # Reportes generales
│   └── A01796826_A5.2.pdf         # Reporte consolidado en formato PDF
├── tests/                          # Archivos de pruebas y logs
│   ├── bitacora_ejecucion.txt     # Historial de ejecuciones
│   ├── pylint_historial.txt       # Historial de análisis Pylint
│   └── flake8_historial.txt       # Historial de análisis Flake8
└── README.md                       # Este archivo
```

## 🚀 Requisitos

- Python 3.7 o superior
- Bibliotecas estándar de Python (json, sys, time, decimal, pathlib)
- (Opcional) pylint y flake8 para análisis de código

## 📖 Uso

### Ejecución del Programa Principal

```bash
cd source
python computeSales.py <archivo_catalogo> <archivo_ventas> [archivo_salida]
```

**Ejemplo básico (usa archivo de salida por defecto):**
```bash
python computeSales.py ../data/priceCatalogue.json ../data/salesRecord.json
# Genera: ../results/SalesResults.txt
```

**Ejemplo con archivo de salida personalizado:**
```bash
python computeSales.py ../data/priceCatalogue.json ../data/TC2.Sales.json ../results/TC2.Sales_results.txt
```

**Ejemplo con dataset grande:**
```bash
python computeSales.py ../data/priceCatalogue.json ../data/salesRecord_100k.json ../results/salesRecord_100k_results.txt
```

### Generar Datos de Prueba

```bash
cd source
python generar_ventas.py
```

Este script genera un archivo `salesRecord_100k.json` con 100,000 renglones de ventas aleatorias basadas en el catálogo de precios.

### Ejecución con Script Automatizado

El script `ejecuta_programa.sh` procesa **automáticamente todos los archivos `*.json`** de la carpeta `data/` y realiza análisis de calidad de código:

```bash
cd source
./ejecuta_programa.sh
```

Este script:
1. **Itera sobre todos los archivos `*.json` en `data/`** (excepto `priceCatalogue.json`)
2. Para cada archivo de ventas, ejecuta el programa y crea un archivo de resultados con el patrón: `{nombre_archivo}_results.txt`
3. Registra la salida en la bitácora de ejecución
4. Ejecuta Pylint para análisis estático del código
5. Ejecuta Flake8 para verificación de estilo PEP8

**Archivos procesados automáticamente:**
- ✅ `salesRecord.json` → `salesRecord_results.txt`
- ✅ `salesRecord_100k.json` → `salesRecord_100k_results.txt`
- ✅ `TC2.Sales.json` → `TC2.Sales_results.txt`
- ✅ `TC3.Sales.json` → `TC3.Sales_results.txt`

## 📄 Formato de Archivos

### Catálogo de Precios (priceCatalogue.json)
```json
[
  {
    "title": "Nombre del Producto",
    "price": 99.99
  }
]
```

### Registro de Ventas (salesRecord.json)
```json
[
  {
    "SALE_ID": 1,
    "Product": "Nombre del Producto",
    "Quantity": 5
  }
]
```

## 📊 Salida del Programa

El programa genera archivos de resultados en el directorio `results/` con:

- Resumen de ventas procesadas
- Total de ventas, renglones e items
- Monto total calculado
- Estadísticas de errores encontrados
- Detalles de errores (si existen)
- Tiempo de ejecución

Ejemplo de salida:
```
========================================
      REPORTE DE VENTAS PROCESADAS
========================================
Fecha y Hora: 2026-02-14 10:30:45

RESUMEN:
  Total de ventas:    1,250
  Total de renglones: 3,456
  Total de items:     8,920

MONTO TOTAL: $125,450.75 USD

Tiempo de ejecución: 0.234 segundos
```

## ✨ Características

### Requisitos Cumplidos

- ✅ Lee 2 archivos JSON desde línea de comandos
- ✅ Calcula el costo total usando el catálogo de precios
- ✅ Imprime resultados en pantalla y los guarda en archivo
- ✅ Maneja datos inválidos: reporta errores y continúa procesando
- ✅ Escala a cientos/miles de ítems
- ✅ Mide e incluye tiempo transcurrido
- ✅ Cumple con PEP8
- ✅ Usa nombres de variables en español

### Manejo de Errores

El sistema maneja robustamente:
- Archivos inexistentes o inaccesibles
- JSON malformado
- Productos sin precio en el catálogo
- Cantidades inválidas (negativas, no numéricas)
- Campos faltantes en los registros
- Tipos de datos incorrectos

## 🛠️ Herramientas de Calidad

### Análisis Estático con Pylint

```bash
pylint computeSales.py
```

### Verificación de Estilo con Flake8

```bash
flake8 computeSales.py
```

Los historiales de estos análisis se guardan automáticamente en el directorio `tests/`.

## 👨‍💻 Autor

Carlos Isaac Sagrero Campos

## 📚 Asignatura

**TC4017 - Pruebas de software y aseguramiento de la calidad**  
4to Trimestre - Maestría  
Semana 5 - Tarea 5.2

## 📅 Fecha

Febrero 2026

## 📝 Licencia

Proyecto académico - Todos los derechos reservados
