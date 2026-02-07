# P3 - Contador de Palabras
## `wordCount.py`

**Programa:** Análisis de frecuencia de palabras en archivos de texto  
**Autor:** Carlos Isaac Sagrero Campos - A01796826  
**Curso:** TC4017 - Pruebas de software y aseguramiento de la calidad

---

## 📋 Descripción

Programa Python que analiza archivos de texto para contar la frecuencia de aparición de cada palabra distinta. Implementa el procesamiento de texto manualmente sin usar expresiones regulares ni funciones avanzadas de strings, con soporte completo para caracteres del español.

---

## ✨ Funcionalidades Principales

### Análisis de Texto
- **Conteo de palabras distintas:** Identifica todas las palabras únicas
- **Frecuencia de aparición:** Cuenta cuántas veces aparece cada palabra
- **Normalización a minúsculas:** Considera "Palabra" y "palabra" como iguales
- **Soporte de español:** Maneja correctamente ñ, á, é, í, ó, ú

### Características Especiales
- ✅ Implementación manual sin regex ni `split()`
- ✅ Procesamiento carácter por carácter
- ✅ Detección de caracteres inválidos con ubicación exacta
- ✅ Conversión manual a minúsculas para español
- ✅ Manejo robusto de errores sin detener ejecución
- ✅ Medición y reporte de tiempo de ejecución
- ✅ Resultados en pantalla y archivo `WordCountResults.txt`

---

## 🚀 Uso del Programa

### Formato de Invocación

```bash
python3 wordCount.py fileWithData.txt
```

### Ejemplo de Ejecución

```bash
cd source
python3 wordCount.py fileWithData.txt
```

### Salida Esperada

```
Word Count Results
------------------
para 3
software 1
seguro 1
es 2
necesario 1
análisis 1
...
------------------
Tiempo_transcurrido_segundos 0.0005010840250179172
```

---

## 📁 Estructura de Archivos

```
P3/
├── README.md                    # Este archivo
├── source/
│   ├── wordCount.py             # Programa principal
│   ├── fileWithData.txt         # Archivo de texto de entrada
│   └── pruebas_pylint.sh        # Script de pruebas con pylint
├── results/
│   └── WordCountResults.txt     # Resultados generados
└── tests/
    └── pylint_historial.txt     # Historial de validaciones pylint
```

---

## 🔧 Requisitos Técnicos Implementados

| Requisito | Descripción | Estado |
|-----------|-------------|--------|
| **Req 1** | Lectura de archivo recibido como parámetro | ✅ Completo |
| **Req 2** | Cálculo de palabras distintas y frecuencias | ✅ Completo |
| **Req 3** | Manejo de errores sin detener ejecución | ✅ Completo |
| **Req 4** | Ejecución desde línea de comandos | ✅ Completo |
| **Req 5** | Validación del formato de invocación | ✅ Completo |
| **Req 6** | Procesamiento eficiente línea por línea | ✅ Completo |
| **Req 7** | Medición y reporte de tiempo de ejecución | ✅ Completo |
| **Req 8** | Conformidad con PEP8 y pylint | ✅ Completo |

---

## 🧮 Algoritmos Implementados

### 1. Detección de Separadores

```python
def es_separador(caracter):
    # Espacios, tabuladores, saltos de línea, puntuación
    return caracter in ' \t\n\r.,;:!?¡¿()[]{}"\'-/'
```

**Separadores reconocidos:**
- Espacios y tabuladores
- Signos de puntuación: `.`, `,`, `;`, `:`, `!`, `?`
- Símbolos de agrupación: `()`, `[]`, `{}`
- Comillas y guiones

### 2. Validación de Caracteres Españoles

```python
def es_letra_espanola(caracter):
    if 'a' <= caracter <= 'z':
        return True
    if 'A' <= caracter <= 'Z':
        return True
    # Vocales acentuadas y ñ
    if caracter in 'áéíóúÁÉÍÓÚñÑüÜ':
        return True
    return False
```

**Caracteres soportados:**
- Letras minúsculas: `a-z`
- Letras mayúsculas: `A-Z`
- Vocales acentuadas: `áéíóúÁÉÍÓÚ`
- Eñes: `ñÑ`
- Diéresis: `üÜ`

### 3. Conversión a Minúsculas (Español)

```python
def a_minusculas_espanol(texto):
    MAYUSCULAS = "ABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓÚÑÜ"
    MINUSCULAS = "abcdefghijklmnopqrstuvwxyzáéíóúñü"
    
    resultado = ""
    for caracter in texto:
        pos = -1
        i = 0
        while i < len(MAYUSCULAS):
            if MAYUSCULAS[i] == caracter:
                pos = i
                break
            i += 1
        
        if pos >= 0:
            resultado += MINUSCULAS[pos]
        else:
            resultado += caracter
    
    return resultado
```

**Algoritmo:**
1. Busca cada carácter en tabla de mayúsculas
2. Si se encuentra, reemplaza por su equivalente minúscula
3. Maneja correctamente acentos y ñ
4. **Complejidad:** O(n × m), donde n es longitud del texto y m es tamaño del alfabeto

### 4. Conteo de Frecuencias

```python
def agregar_frecuencia(palabras, frecuencias, palabra):
    # Buscar si la palabra ya existe
    indice = -1
    i = 0
    while i < len(palabras):
        if palabras[i] == palabra:
            indice = i
            break
        i += 1
    
    if indice >= 0:
        # Palabra existe, incrementar frecuencia
        frecuencias[indice] += 1
    else:
        # Palabra nueva, agregar
        palabras.append(palabra)
        frecuencias.append(1)
```

**Algoritmo:**
1. Busca la palabra en la lista de palabras únicas
2. Si existe, incrementa su frecuencia
3. Si no existe, la agrega con frecuencia 1
4. **Complejidad:** O(n) por palabra

### 5. Procesamiento Principal

```python
def procesar_archivo(ruta_archivo):
    palabras = []
    frecuencias = []
    
    with open(ruta_archivo, 'r', encoding='utf-8', errors='replace') as archivo:
        linea_num = 0
        for linea in archivo:
            linea_num += 1
            palabra_actual = []
            pos = 0
            
            while pos < len(linea):
                ch = linea[pos]
                
                if es_separador(ch):
                    if palabra_actual:
                        palabra = ''.join(palabra_actual)
                        palabra = a_minusculas_espanol(palabra)
                        agregar_frecuencia(palabras, frecuencias, palabra)
                        palabra_actual = []
                else:
                    if es_caracter_valido_en_palabra(ch):
                        palabra_actual.append(ch)
                    else:
                        # Reportar error y continuar
                        print(f"Error: caracter invalido en linea {linea_num} ...")
                
                pos += 1
    
    return palabras, frecuencias
```

**Algoritmo:**
1. Procesa archivo línea por línea
2. Examina cada carácter individualmente
3. Construye palabras carácter por carácter
4. Valida cada carácter y reporta inválidos
5. **Complejidad:** O(n), donde n es el número total de caracteres

---

## 📊 Formato de Datos de Entrada

El archivo de entrada puede contener:
- Texto en español con acentos y ñ
- Múltiples líneas y párrafos
- Signos de puntuación comunes
- Mayúsculas y minúsculas mezcladas

### Ejemplo de `fileWithData.txt`

```
Para construir software seguro, es necesario comenzar desde la 
etapa de análisis y definición de requisitos. Debe incluir 
objetivos claros relacionados con la protección de información, 
el control de accesos y la resistencia ante ataques.

Un error común es enfocarse únicamente en las funcionalidades 
visibles para el usuario y dejar la seguridad para después.
```

### Caracteres Inválidos Detectados
- Símbolos especiales no esperados: `@`, `#`, `$`, `%`
- Caracteres de control ASCII
- Bytes inválidos en UTF-8 (manejados con `errors='replace'`)

---

## 🛠️ Análisis Estático con Pylint

### Ejecutar Validación

```bash
cd source
bash pruebas_pylint.sh
```

### O ejecutar pylint directamente

```bash
pylint wordCount.py
```

### Resultados Esperados
- **Puntuación:** > 9.0/10.0
- **Conformidad PEP8:** 100%
- **Sin errores críticos**

---

## 📝 Archivo de Salida

### Ubicación
```
results/WordCountResults.txt
```

### Formato
```
Word Count Results
------------------
para 3
software 1
seguro 1
es 2
...
------------------
Tiempo_transcurrido_segundos 0.0005010840250179172
```

### Contenido
- Encabezado del reporte
- Una línea por palabra distinta con su frecuencia
- Separador visual
- Tiempo de ejecución en segundos

---

## 🔍 Manejo de Errores

### Errores Manejados
1. **Archivo no encontrado:** Mensaje claro, retorna listas vacías
2. **Permisos insuficientes:** Detección y reporte
3. **Caracteres inválidos:** Reporte con línea y posición exacta
4. **Errores de encoding:** Modo `errors='replace'` para UTF-8
5. **Error al escribir resultados:** Captura de excepciones OSError

### Ejemplo de Reporte de Errores

```
Error: caracter invalido en linea 5 posicion 23: '@'
Error: caracter invalido en linea 8 posicion 15: '#'
```

---

## 📋 Ejemplo de Resultados

### Entrada
```
La calidad es fundamental. La calidad importa.
```

### Salida
```
Word Count Results
------------------
la 2
calidad 2
es 1
fundamental 1
importa 1
------------------
Tiempo_transcurrido_segundos 0.000123
```

**Observaciones:**
- "La" y "la" se cuentan como la misma palabra
- "calidad" aparece 2 veces
- La puntuación se ignora correctamente

---

## ⚡ Optimizaciones de Rendimiento

- **Procesamiento streaming:** Lee línea por línea, no carga archivo completo
- **Búsqueda lineal optimizada:** Adecuada para vocabularios pequeños/medianos
- **Sin regex:** Evita overhead de compilación de patrones
- **Encoding tolerante:** `errors='replace'` previene crashes por encoding

### Mejoras Posibles (no implementadas por requisitos)
- Usar diccionarios en lugar de listas paralelas para O(1) en búsqueda
- Implementar ordenamiento de resultados por frecuencia
- Agregar filtrado de palabras vacías (stop words)

---

## 📚 Funciones Principales

| Función | Descripción |
|---------|-------------|
| `es_separador()` | Detecta caracteres separadores de palabras |
| `es_letra_espanola()` | Valida letras del alfabeto español |
| `es_caracter_valido_en_palabra()` | Valida caracteres permitidos |
| `a_minusculas_espanol()` | Convierte a minúsculas con soporte de acentos |
| `agregar_frecuencia()` | Actualiza conteo de palabras |
| `procesar_archivo()` | Procesa archivo y extrae palabras |
| `construir_lineas_resultado()` | Formatea resultados para salida |
| `escribir_archivo_resultados()` | Guarda resultados en archivo |

---

## 🎯 Casos de Uso

1. **Análisis de contenido:** Identificar palabras más frecuentes en documentos
2. **Procesamiento de NLP básico:** Base para análisis de lenguaje natural
3. **Control de vocabulario:** Verificar uso de términos específicos
4. **Educación:** Demostración de algoritmos de procesamiento de texto

---

## 🐛 Solución de Problemas

### Error: "Uso: python wordCount.py fileWithData.txt"
**Causa:** Falta el argumento del archivo de entrada  
**Solución:** Proporcionar la ruta del archivo como argumento

### Error: "no se encontro el archivo"
**Causa:** Ruta de archivo incorrecta  
**Solución:** Verificar que el archivo existe en la ubicación especificada

### Advertencia: "caracter invalido"
**Causa:** Archivo contiene caracteres no esperados  
**Solución:** El programa reporta y continúa; revisar archivo de entrada

### Problema: Palabras acentuadas no se reconocen
**Causa:** Encoding incorrecto del archivo  
**Solución:** Asegurar que el archivo esté codificado en UTF-8

---

## 💡 Limitaciones y Consideraciones

- **Sin ordenamiento:** Palabras aparecen en el orden que se encuentran
- **Sensibilidad a acentos:** "casa" y "casá" son palabras diferentes
- **Guiones:** Palabras con guión se separan (ej: "bien-estar" → "bien", "estar")
- **Números:** Dígitos se consideran caracteres inválidos
- **Complejidad de búsqueda:** O(n) por palabra; puede ser lento con vocabularios muy grandes

---

## 🌐 Soporte de Idiomas

### Español (Completo)
- ✅ Vocales acentuadas (á, é, í, ó, ú)
- ✅ Eñe (ñ, Ñ)
- ✅ Diéresis (ü, Ü)
- ✅ Signos de interrogación y exclamación invertidos (¿, ¡)

### Otros Idiomas
- ⚠️ Inglés: Soportado completamente (subset del español)
- ⚠️ Francés/Portugués: Soporte parcial (algunos acentos)
- ❌ Alemán/Nórdicos: No soporta ß, ø, å, æ

---

## 📄 Licencia y Uso Académico

Este programa fue desarrollado con fines educativos para el curso TC4017. El código implementa algoritmos de procesamiento de texto manualmente para demostrar comprensión de los conceptos fundamentales de análisis léxico y manejo de caracteres.

---

## 👤 Autor

**Carlos Isaac Sagrero Campos**  
Matrícula: A01796826
TC4017 - Pruebas de software y aseguramiento de la calidad
