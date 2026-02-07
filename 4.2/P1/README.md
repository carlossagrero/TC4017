# P1 - Estadísticas Descriptivas
## `computeStatistics.py`

**Programa:** Cálculo de estadísticas descriptivas  
**Autor:** Carlos Isaac Sagrero Campos - A01796826  
**Curso:** TC4017 - Pruebas de software y aseguramiento de la calidad

---

## 📋 Descripción

Programa Python que calcula estadísticas descriptivas básicas (media, mediana, moda, varianza y desviación estándar) a partir de un archivo de datos numéricos. Implementa todos los algoritmos estadísticos manualmente sin usar librerías como NumPy o SciPy.

---

## ✨ Funcionalidades Principales

### Estadísticas Calculadas
- **Media (Mean):** Promedio aritmético de los valores
- **Mediana (Median):** Valor central en el conjunto ordenado
- **Moda (Mode):** Valor(es) más frecuente(s)
- **Varianza (Variance):** Medida de dispersión de los datos
- **Desviación Estándar (Standard Deviation):** Raíz cuadrada de la varianza

### Características Especiales
- ✅ Implementación manual de todos los algoritmos (sin NumPy/SciPy)
- ✅ Manejo de errores sin detener la ejecución
- ✅ Detección y reporte de valores inválidos (NaN, Infinity, texto)
- ✅ Procesamiento eficiente para grandes volúmenes de datos
- ✅ Medición y reporte de tiempo de ejecución
- ✅ Resultados en pantalla y archivo `StatisticsResults.txt`

---

## 🚀 Uso del Programa

### Formato de Invocación

```bash
python3 computeStatistics.py fileWithData.txt
```

### Ejemplo de Ejecución

```bash
cd source
python3 computeStatistics.py fileWithData.txt
```

### Salida Esperada

```
=== Statistics Results ===
Archivo de entrada: fileWithData.txt
Valores leidos totales(validos + invalidos): 111
Numeros validos: 106
Valores invalidos: 5

=== Descriptive Statistics ===
Mean (media): 49.792453
Median (mediana): 47.500000
Mode (moda): 38
Variance (varianza): 794.428622
Standard deviation (desviacion estandar): 28.185610

Tiempo transcurrido (segundos): 0.000368

=== Errores detectados (se continuo la ejecucion) ===
Error en linea 100: valor '--' invalido (could not convert string to float: '--')
Error en linea 100: valor 'pa'' invalido (could not convert string to float: "pa'")
...
```

---

## 📁 Estructura de Archivos

```
P1/
├── README.md                    # Este archivo
├── source/
│   ├── computeStatistics.py     # Programa principal
│   ├── fileWithData.txt         # Archivo de datos de entrada
│   └── pruebas_pylint.sh        # Script de pruebas con pylint
├── results/
│   └── StatisticsResults.txt    # Resultados generados
└── tests/
    └── pylint_historial.txt     # Historial de validaciones pylint
```

---

## 🔧 Requisitos Técnicos Implementados

| Requisito | Descripción | Estado |
|-----------|-------------|--------|
| **Req 1** | Lectura de archivo recibido como parámetro | ✅ Completo |
| **Req 2** | Cálculo de estadísticas con algoritmos básicos | ✅ Completo |
| **Req 3** | Manejo de errores sin detener ejecución | ✅ Completo |
| **Req 4** | Ejecución desde línea de comandos | ✅ Completo |
| **Req 5** | Validación del formato de invocación | ✅ Completo |
| **Req 6** | Soporte para miles de elementos (O(n)/O(n log n)) | ✅ Completo |
| **Req 7** | Medición y reporte de tiempo de ejecución | ✅ Completo |
| **Req 8** | Conformidad con PEP8 y pylint | ✅ Completo |

---

## 🧮 Algoritmos Implementados

### 1. Media
```python
def calcular_media(numeros):
    suma = 0.0
    for valor in numeros:
        suma += valor
    return suma / len(numeros)
```
- **Complejidad:** O(n)

### 2. Mediana
```python
def calcular_mediana(numeros_ordenados):
    n = len(numeros_ordenados)
    if n % 2 == 0:
        return (numeros_ordenados[n//2 - 1] + numeros_ordenados[n//2]) / 2.0
    else:
        return numeros_ordenados[n // 2]
```
- **Complejidad:** O(n log n) - incluye ordenamiento con merge sort

### 3. Moda
```python
def calcular_moda(numeros):
    # Conteo manual con diccionario
    conteos = {}
    for valor in numeros:
        conteos[valor] = conteos.get(valor, 0) + 1
    # Encuentra frecuencia máxima y valores con esa frecuencia
```
- **Complejidad:** O(n)

### 4. Varianza
```python
def calcular_varianza(numeros, media):
    suma_cuadrados = 0.0
    for valor in numeros:
        diferencia = valor - media
        suma_cuadrados += diferencia * diferencia
    return suma_cuadrados / len(numeros)
```
- **Complejidad:** O(n)

### 5. Raíz Cuadrada (Newton-Raphson)
```python
def calcular_raiz_cuadrada(valor):
    # Método iterativo Newton-Raphson
    for _ in range(30):
        estimacion = 0.5 * (estimacion + (valor / estimacion))
    return estimacion
```
- **Complejidad:** O(1) - iteraciones fijas

---

## 📊 Formato de Datos de Entrada

El archivo de entrada debe contener números separados por:
- Espacios
- Comas
- Saltos de línea

### Ejemplo de `fileWithData.txt`

```
56, 45, 89, 12, 34
78 23 67 90 11
45.5 67.8 23.4
```

### Valores Inválidos Detectados
- Texto no numérico: `"abc"`, `"--"`, `"que"`
- Valores especiales: `NaN`, `Infinity`, `-Infinity`
- Cadenas vacías o con caracteres inválidos

---

## 🛠️ Análisis Estático con Pylint

### Ejecutar Validación

```bash
cd source
bash pruebas_pylint.sh
```

### O ejecutar pylint directamente

```bash
pylint computeStatistics.py
```

### Resultados Esperados
- **Puntuación:** > 9.0/10.0
- **Conformidad PEP8:** 100%
- **Sin errores críticos**

---

## 📝 Archivo de Salida

### Ubicación
```
results/StatisticsResults.txt
```

### Contenido
- Resumen de valores leídos (válidos e inválidos)
- Estadísticas descriptivas calculadas
- Tiempo de ejecución
- Lista de errores detectados con número de línea

---

## 🔍 Manejo de Errores

### Errores Manejados
1. **Archivo no encontrado:** Mensaje claro y salida controlada
2. **Permisos insuficientes:** Detección y reporte
3. **Valores inválidos:** Reporte con número de línea y valor
4. **NaN/Infinity:** Rechazo automático con mensaje descriptivo
5. **Error al escribir resultados:** Captura de excepciones OSError

### Ejemplo de Reporte de Errores

```
=== Errores detectados (se continuo la ejecucion) ===
Error en linea 100: valor '--' invalido (could not convert string to float: '--')
Error en linea 100: valor 'pa'' invalido (could not convert string to float: "pa'")
Error en linea 100: valor 'que' invalido (could not convert string to float: 'que')
```

---

## ⚡ Optimizaciones de Rendimiento

- **Procesamiento streaming:** Lectura línea por línea para no saturar memoria
- **Algoritmo de ordenamiento eficiente:** Merge sort O(n log n)
- **Cálculo en una sola pasada:** Minimización de iteraciones sobre datos
- **Iteraciones fijas para raíz cuadrada:** Evita convergencia costosa

---

## 📚 Funciones Principales

| Función | Descripción |
|---------|-------------|
| `leer_numeros_desde_archivo()` | Lee y valida números del archivo |
| `calcular_media()` | Calcula promedio aritmético |
| `calcular_mediana()` | Calcula valor central |
| `calcular_moda()` | Encuentra valor(es) más frecuente(s) |
| `calcular_varianza()` | Calcula dispersión de datos |
| `calcular_raiz_cuadrada()` | Implementación Newton-Raphson |
| `construir_reporte()` | Genera texto formateado de resultados |
| `escribir_archivo_salida()` | Guarda resultados en archivo |

---

## 🎯 Casos de Uso

1. **Análisis de datos experimentales:** Procesamiento de mediciones científicas
2. **Control de calidad:** Análisis de métricas de producción
3. **Análisis financiero:** Estadísticas de precios, rendimientos, etc.
4. **Educación:** Demostración de algoritmos estadísticos básicos

---

## 🐛 Solución de Problemas

### Error: "Uso: python computeStatistics.py fileWithData.txt"
**Causa:** Falta el argumento del archivo de entrada  
**Solución:** Proporcionar la ruta del archivo como argumento

### Error: "No se encontro el archivo"
**Causa:** Ruta de archivo incorrecta  
**Solución:** Verificar que el archivo existe en la ubicación especificada

### Advertencia: "NaN no permitido"
**Causa:** Archivo contiene valores NaN explícitos  
**Solución:** El programa reporta y continúa; revisar archivo de entrada

---

## 📄 Licencia y Uso Académico

Este programa fue desarrollado con fines educativos para el curso TC4017. El código implementa algoritmos básicos manualmente para demostrar comprensión de los conceptos fundamentales.

---

## 👤 Autor

**Carlos Isaac Sagrero Campos**  
Matrícula: A01796826  
TC4017 - Pruebas de software y aseguramiento de la calidad
