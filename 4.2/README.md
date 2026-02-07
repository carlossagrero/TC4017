# TC4017 - Pruebas de Software y Aseguramiento de la Calidad
## Tarea 4.2 - Ejercicio de programación 1

**Autor:** Carlos Isaac Sagrero Campos - A01796826  
**Fecha:** 7 de febrero de 2026

---

## Descripción General

Este repositorio contiene tres programas Python desarrollados como parte de la Tarea 4.2 del curso TC4017. Cada programa implementa funcionalidades específicas de procesamiento de datos, cumpliendo con estrictos requisitos de calidad de código validados mediante análisis estático con **pylint**.

Los tres programas comparten características comunes:
- ✅ Implementación sin uso de librerías externas para algoritmos core
- ✅ Manejo robusto de errores sin detener la ejecución
- ✅ Medición y reporte de tiempo de ejecución
- ✅ Procesamiento eficiente para manejar grandes volúmenes de datos
- ✅ Conformidad con PEP8 y validación con pylint
- ✅ Generación de archivos de resultados

---

## Estructura del Proyecto

```
4.2/
├── README.md                    # Este archivo
├── P1/                          # Programa 1: Estadísticas Descriptivas
│   ├── README.md
│   ├── source/
│   │   ├── computeStatistics.py
│   │   ├── fileWithData.txt
│   │   └── pruebas_pylint.sh
│   ├── results/
│   │   └── StatisticsResults.txt
│   └── tests/
│       └── pylint_historial.txt
├── P2/                          # Programa 2: Conversión de Números
│   ├── README.md
│   ├── source/
│   │   ├── convertNumbers.py
│   │   ├── fileWithData.txt
│   │   └── pruebas_pylint.sh
│   ├── results/
│   │   └── ConvertionResults.txt
│   └── tests/
│       └── pylint_historial.txt
└── P3/                          # Programa 3: Contador de Palabras
    ├── README.md
    ├── source/
    │   ├── wordCount.py
    │   ├── fileWithData.txt
    │   └── pruebas_pylint.sh
    ├── results/
    │   └── WordCountResults.txt
    └── tests/
        └── pylint_historial.txt
```

---

## Programas Incluidos

### 📊 P1: Estadísticas Descriptivas (`computeStatistics.py`)
Calcula estadísticas descriptivas de un conjunto de números:
- Media, mediana, moda
- Varianza y desviación estándar
- Algoritmos implementados manualmente (sin numpy/scipy)

[Ver documentación completa →](P1/README.md)

### 🔢 P2: Conversión de Números (`convertNumbers.py`)
Convierte números enteros a representaciones binaria y hexadecimal:
- Conversión manual sin funciones integradas de Python
- Procesamiento línea por línea para eficiencia
- Manejo de valores inválidos

[Ver documentación completa →](P2/README.md)

### 📝 P3: Contador de Palabras (`wordCount.py`)
Analiza frecuencia de palabras en archivos de texto:
- Soporte para caracteres en español (á, é, í, ó, ú, ñ)
- Procesamiento sin regex ni funciones de string avanzadas
- Detección de caracteres inválidos

[Ver documentación completa →](P3/README.md)

---

## Requisitos Generales

### Software Necesario
- Python 3.8 o superior
- pylint (para análisis estático)

### Instalación de Dependencias

```bash
# Instalar pylint
pip install pylint

# Verificar instalación
python3 --version
pylint --version
```

---

## Ejecución de Programas

Cada programa se ejecuta de forma independiente desde su directorio `source/`:

```bash
# P1: Estadísticas Descriptivas
cd P1/source
python3 computeStatistics.py fileWithData.txt

# P2: Conversión de Números
cd P2/source
python3 convertNumbers.py fileWithData.txt

# P3: Contador de Palabras
cd P3/source
python3 wordCount.py fileWithData.txt
```

---

## Análisis Estático con Pylint

Cada programa incluye un script `pruebas_pylint.sh` que:
1. Ejecuta el programa Python
2. Realiza análisis estático con pylint
3. Registra resultados en `../tests/pylint_historial.txt`

### Ejecutar Pruebas

```bash
# Ejemplo para P1
cd P1/source
bash pruebas_pylint.sh

# O ejecutar pylint directamente
pylint computeStatistics.py
```

---

## Características Técnicas Destacadas

### ✨ Implementación sin Librerías Externas
- Algoritmos implementados manualmente para fines educativos
- Mayor comprensión de los conceptos matemáticos y de procesamiento
- Cumplimiento estricto de requisitos de la tarea

### 🛡️ Manejo Robusto de Errores
- Los programas reportan errores y continúan la ejecución
- Validación exhaustiva de datos de entrada
- Mensajes de error descriptivos con ubicación exacta

### ⚡ Optimización para Grandes Volúmenes
- Procesamiento streaming (línea por línea)
- Complejidad algorítmica eficiente (O(n) o O(n log n))
- Medición y reporte de tiempo de ejecución

### 📋 Calidad de Código
- Conformidad total con PEP8
- Validación con pylint (puntajes > 9.0/10.0)
- Documentación exhaustiva con docstrings
- Código legible y mantenible

---

## Resultados y Salidas

Cada programa genera:
1. **Salida en consola:** Resultados formateados para visualización
2. **Archivo de resultados:** Guardado en `results/`
3. **Registro de tiempo:** Medición precisa del tiempo de ejecución
4. **Reporte de errores:** Listado de valores inválidos detectados

---

## Notas de Desarrollo

- Los programas evitan el uso de `split()`, `regex` y funciones avanzadas según requisitos
- Implementación de algoritmos básicos para conversión de casos, ordenamiento, etc.
- Soporte para caracteres especiales del español (ñ, acentos)
- Validación de NaN e Infinity en datos numéricos

---

## Autor

**Carlos Isaac Sagrero Campos**  
Matrícula: A01796826  
Curso: TC4017 - Pruebas de software y aseguramiento de la calidad  
