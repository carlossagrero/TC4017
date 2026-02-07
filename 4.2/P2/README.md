# P2 - Conversión de Números
## `convertNumbers.py`

**Programa:** Conversión de números decimales a binario y hexadecimal  
**Autor:** Carlos Isaac Sagrero Campos - A01796826  
**Curso:** TC4017 - Pruebas de software y aseguramiento de la calidad

---

## 📋 Descripción

Programa Python que convierte números enteros del sistema decimal a sus representaciones en binario y hexadecimal. Implementa los algoritmos de conversión manualmente sin usar las funciones integradas de Python (`bin()`, `hex()`).

---

## ✨ Funcionalidades Principales

### Conversiones Realizadas
- **Decimal → Binario:** Representación en base 2
- **Decimal → Hexadecimal:** Representación en base 16 (0-9, A-F)

### Características Especiales
- ✅ Implementación manual de algoritmos de conversión
- ✅ Procesamiento línea por línea para eficiencia
- ✅ Manejo de errores sin detener la ejecución
- ✅ Soporte para números negativos
- ✅ Detección de valores inválidos (no enteros, texto)
- ✅ Medición y reporte de tiempo de ejecución
- ✅ Resultados en pantalla y archivo `ConvertionResults.txt`

---

## 🚀 Uso del Programa

### Formato de Invocación

```bash
python3 convertNumbers.py fileWithData.txt
```

### Ejemplo de Ejecución

```bash
cd source
python3 convertNumbers.py fileWithData.txt
```

### Salida Esperada

```
Numero	Binario	Hexadecimal
15	1111	F
255	11111111	FF
256	100000000	100
-10	-1010	-A
42	101010	2A

Tiempo transcurrido (segundos): 0.000123
```

---

## 📁 Estructura de Archivos

```
P2/
├── README.md                    # Este archivo
├── source/
│   ├── convertNumbers.py        # Programa principal
│   ├── fileWithData.txt         # Archivo de datos de entrada
│   ├── ConvertionResults.txt    # Resultados (duplicado en source)
│   └── pruebas_pylint.sh        # Script de pruebas con pylint
├── results/
│   └── ConvertionResults.txt    # Resultados generados
└── tests/
    └── pylint_historial.txt     # Historial de validaciones pylint
```

---

## 🔧 Requisitos Técnicos Implementados

| Requisito | Descripción | Estado |
|-----------|-------------|--------|
| **Req 1** | Lectura de archivo recibido como parámetro | ✅ Completo |
| **Req 2** | Conversión con algoritmos básicos | ✅ Completo |
| **Req 3** | Manejo de errores sin detener ejecución | ✅ Completo |
| **Req 4** | Ejecución desde línea de comandos | ✅ Completo |
| **Req 5** | Validación del formato de invocación | ✅ Completo |
| **Req 6** | Procesamiento eficiente línea por línea | ✅ Completo |
| **Req 7** | Medición y reporte de tiempo de ejecución | ✅ Completo |
| **Req 8** | Conformidad con PEP8 y pylint | ✅ Completo |

---

## 🧮 Algoritmos Implementados

### 1. Conversión a Binario

```python
def convertir_a_binario(numero):
    if numero == 0:
        return "0"
    
    negativo = numero < 0
    numero = abs(numero)
    
    resultado = ""
    while numero > 0:
        digito = numero % 2
        resultado = str(digito) + resultado
        numero = numero // 2
    
    if negativo:
        resultado = "-" + resultado
    
    return resultado
```

**Algoritmo:**
1. Divide el número entre 2 repetidamente
2. El residuo de cada división es un dígito binario
3. Construye el resultado de derecha a izquierda
4. **Complejidad:** O(log₂ n)

### 2. Conversión a Hexadecimal

```python
def convertir_a_hexadecimal(numero):
    if numero == 0:
        return "0"
    
    DIGITOS_HEX = "0123456789ABCDEF"
    negativo = numero < 0
    numero = abs(numero)
    
    resultado = ""
    while numero > 0:
        residuo = numero % 16
        resultado = DIGITOS_HEX[residuo] + resultado
        numero = numero // 16
    
    if negativo:
        resultado = "-" + resultado
    
    return resultado
```

**Algoritmo:**
1. Divide el número entre 16 repetidamente
2. El residuo se mapea al dígito hexadecimal (0-F)
3. Construye el resultado de derecha a izquierda
4. **Complejidad:** O(log₁₆ n)

### 3. Interpretación de Enteros

```python
def interpretar_entero(texto):
    texto = texto.strip()
    if not texto:
        return (False, 0)
    
    # Validación manual del formato de entero
    negativo = False
    pos = 0
    
    if texto[0] == '-':
        negativo = True
        pos = 1
    elif texto[0] == '+':
        pos = 1
    
    # Construir número dígito por dígito
    numero = 0
    while pos < len(texto):
        ch = texto[pos]
        if not ('0' <= ch <= '9'):
            return (False, 0)
        numero = numero * 10 + (ord(ch) - ord('0'))
        pos += 1
    
    if negativo:
        numero = -numero
    
    return (True, numero)
```

**Algoritmo:**
1. Valida manualmente el formato de entero
2. Construye el número dígito por dígito sin usar `int()`
3. Maneja signo positivo/negativo
4. **Complejidad:** O(m), donde m es la longitud del texto

---

## 📊 Formato de Datos de Entrada

El archivo de entrada debe contener un número entero por línea.

### Ejemplo de `fileWithData.txt`

```
15
255
256
-10
42
100
1024
0
-128
```

### Valores Inválidos Detectados
- Números decimales: `3.14`, `2.5`
- Texto no numérico: `"abc"`, `"xyz"`
- Líneas vacías (se ignoran)
- Valores con caracteres extraños: `"12a"`, `"--5"`

---

## 🛠️ Análisis Estático con Pylint

### Ejecutar Validación

```bash
cd source
bash pruebas_pylint.sh
```

### O ejecutar pylint directamente

```bash
pylint convertNumbers.py
```

### Resultados Esperados
- **Puntuación:** > 9.0/10.0
- **Conformidad PEP8:** 100%
- **Sin errores críticos**

---

## 📝 Archivo de Salida

### Ubicación
```
source/ConvertionResults.txt
results/ConvertionResults.txt
```

### Formato
```
Numero	Binario	Hexadecimal
15	1111	F
255	11111111	FF
...
Tiempo transcurrido (segundos): 0.000123
```

### Contenido
- Encabezado con nombres de columnas
- Una línea por número convertido
- Tiempo de ejecución al final
- Errores reportados durante el proceso

---

## 🔍 Manejo de Errores

### Errores Manejados
1. **Archivo no encontrado:** Mensaje claro y salida con código 1
2. **Permisos insuficientes:** Detección y salida controlada
3. **Valores no enteros:** Reporte con número de línea
4. **Formato inválido:** Mensaje descriptivo del error
5. **Error al escribir resultados:** Captura de excepciones OSError

### Ejemplo de Reporte de Errores

```
Error en linea 5: valor invalido '3.14' (no es un numero entero)
Error en linea 8: valor invalido 'abc' (no es un numero entero)
```

---

## 📋 Tabla de Conversiones de Ejemplo

| Decimal | Binario | Hexadecimal |
|---------|---------|-------------|
| 0 | 0 | 0 |
| 1 | 1 | 1 |
| 15 | 1111 | F |
| 16 | 10000 | 10 |
| 255 | 11111111 | FF |
| 256 | 100000000 | 100 |
| 1024 | 10000000000 | 400 |
| -10 | -1010 | -A |
| -255 | -11111111 | -FF |

---

## ⚡ Optimizaciones de Rendimiento

- **Procesamiento streaming:** Lee y procesa línea por línea
- **Sin carga completa en memoria:** Ideal para archivos grandes
- **Escritura simultánea:** Escribe resultados mientras procesa
- **Algoritmos eficientes:** O(log n) para conversiones

---

## 📚 Funciones Principales

| Función | Descripción |
|---------|-------------|
| `convertir_a_binario()` | Convierte entero a representación binaria |
| `convertir_a_hexadecimal()` | Convierte entero a representación hexadecimal |
| `interpretar_entero()` | Valida y convierte texto a entero |
| `procesar_archivo()` | Procesa archivo línea por línea |
| `main()` | Punto de entrada del programa |

---

## 🎯 Casos de Uso

1. **Educación:** Aprendizaje de sistemas numéricos
2. **Debugging:** Conversión rápida de valores para análisis
3. **Programación de bajo nivel:** Conversión de direcciones de memoria
4. **Criptografía:** Manipulación de valores en diferentes bases

---

## 🐛 Solución de Problemas

### Error: "Uso: python convertNumbers.py fileWithData.txt"
**Causa:** Falta el argumento del archivo de entrada  
**Solución:** Proporcionar la ruta del archivo como argumento

### Error: "archivo no encontrado"
**Causa:** Ruta de archivo incorrecta  
**Solución:** Verificar que el archivo existe en la ubicación especificada

### Advertencia: "valor invalido"
**Causa:** Archivo contiene valores no enteros  
**Solución:** El programa reporta y continúa; revisar valores en el archivo

---

## 💡 Limitaciones y Consideraciones

- Solo procesa **números enteros** (no decimales)
- Soporte para números negativos (con prefijo `-`)
- Sin límite teórico de tamaño (limitado por memoria de Python)
- Resultados en formato tabular con separación por tabulador

---

## 📄 Licencia y Uso Académico

Este programa fue desarrollado con fines educativos para el curso TC4017. El código implementa algoritmos de conversión de base manualmente para demostrar comprensión de los conceptos fundamentales de sistemas numéricos.

---

## 👤 Autor

**Carlos Isaac Sagrero Campos**  
Matrícula: A01796826  
TC4017 - Pruebas de software y aseguramiento de la calidad
