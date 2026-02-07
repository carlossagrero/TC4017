""" Tarea: computeStatistics.py
Se bsuca cumplir los reuqisito sy no tener los errores al ejecurar esa cosa de pylint. 
Creí que iba a ser más facil, pero no :-(

P2 - TC4017 - Pruebas de software y aseguramiento de la calidad
Carlos Isaac Sagrero Campos - A01796826

"""
# pylint: disable=invalid-name
import sys
import time
import math


# Req 2: Archivo de salida con nombre fijo StatisticsResults.txt
NOMBRE_ARCHIVO_SALIDA = "../results/StatisticsResults.txt"


def separar_tokens(linea_limpia):
    """Separa tokens por comas o espacios sin usar split ni regex."""
    valores = []
    actual = ""

    for caracter in linea_limpia:
        if caracter == "," or caracter.isspace():
            if actual:
                valores.append(actual)
                actual = ""
        else:
            actual += caracter

    if actual:
        valores.append(actual)

    return valores


def convertir_a_float_seguro(valor_str):
    """Convierte a float y rechaza NaN e Inf."""
    valor = float(valor_str)

    # NaN check (NaN != NaN siempre es True)
    #Como me diste lata con el pylint
    if math.isnan(valor):
        raise ValueError("NaN no permitido")

    if math.isinf(valor):
        raise ValueError("Inf no permitido")

    return valor


def leer_numeros_desde_archivo(ruta_archivo):
    """
    Req 1: Lee el archivo recibido como parametro.
    Req 3: Detecta tokens invalidos, reporta errores y continua.
    Req 6: Lee muchos elementos de forma secuencial (streaming por lineas).
    """
    numeros = []
    errores = []
    total_valores = 0

    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            for numero_linea, linea in enumerate(archivo, start=1):
                linea_limpia = linea.strip()
                if not linea_limpia:
                    continue

                tokens = separar_tokens(linea_limpia)

                for valor_str in tokens:
                    total_valores += 1
                    try:
                        numeros.append(convertir_a_float_seguro(valor_str))
                    except ValueError as exc:
                        errores.append(
                            f"Error en linea {numero_linea}: valor "
                            f"'{valor_str}' invalido ({exc})"
                        )

    except FileNotFoundError:
        errores.append(f"No se encontro el archivo: {ruta_archivo}")
    except PermissionError:
        errores.append(f"Sin permisos para leer el archivo: {ruta_archivo}")
    except OSError as exc:
        errores.append(f"Error al leer el archivo '{ruta_archivo}': {exc}")

    return numeros, errores, total_valores


def ordenar_lista(numeros):
    """
    Req 2: Ordenamiento necesario para mediana (algoritmo basico).
    Req 6: Merge sort O(n log n) adecuado para cientos/miles de elementos.
    """
    n = len(numeros)
    if n <= 1:
        return numeros[:]

    mitad = n // 2
    izquierda = ordenar_lista(numeros[:mitad])
    derecha = ordenar_lista(numeros[mitad:])

    return fusionar_listas(izquierda, derecha)


def fusionar_listas(izquierda, derecha):
    """
    Req 2: Parte del algoritmo basico merge sort (sin librerias).
    Req 6: Fusion lineal O(n) para mantener eficiencia.
    """
    resultado = []
    i = 0
    j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    while i < len(izquierda):
        resultado.append(izquierda[i])
        i += 1

    while j < len(derecha):
        resultado.append(derecha[j])
        j += 1

    return resultado


def calcular_media(numeros):
    """
    Req 2: Calcula la media con algoritmo basico (suma / n), sin librerias.
    Req 6: O(n) para soportar muchos elementos.
    """
    num = len(numeros)
    if num == 0:
        return None

    suma = 0.0
    for valor in numeros:
        suma += valor
    return suma / num


def calcular_mediana(numeros_ordenados):
    """
    Req 2: Calcula la mediana usando el listado ordenado (algoritmo basico).
    Req 6: Acceso O(1) al/los elementos centrales tras ordenar.
    """
    num = len(numeros_ordenados)
    if num == 0:
        return None

    mitad = num // 2
    if num % 2 == 1:
        return numeros_ordenados[mitad]

    return (numeros_ordenados[mitad - 1] + numeros_ordenados[mitad]) / 2.0


def calcular_moda(numeros):
    """
    Req 2: Calcula moda con conteo manual (diccionario) sin librerias.
    Req 6: Conteo O(n) para cientos/miles de elementos.
    Req 3: No falla si la lista esta vacia; devuelve lista vacia.
    """
    num = len(numeros)
    if num == 0:
        return []

    conteos = {}
    for valor in numeros:
        if valor in conteos:
            conteos[valor] += 1
        else:
            conteos[valor] = 1

    max_frecuencia = 0
    for _, frecuencia in conteos.items():
        if frecuencia > max_frecuencia:
            max_frecuencia = frecuencia

    if max_frecuencia <= 1:
        return []

    modas = []
    for valor, frecuencia in conteos.items():
        if frecuencia == max_frecuencia:
            modas.append(valor)

    # Req 2: Salida consistente; se ordena con el mismo algoritmo basico.
    return ordenar_lista(modas)


def calcular_varianza(numeros, media):
    """
    Req 2: Calcula varianza con algoritmo basico:
        sum((xi - media)^2) / n
    (Varianza poblacional; el requisito no especifica muestral.)
    Req 6: O(n) para soportar muchos elementos.
    """
    n = len(numeros)
    if n == 0:
        return None

    suma_cuadrados = 0.0
    for valor in numeros:
        diferencia = valor - media
        suma_cuadrados += diferencia * diferencia

    return suma_cuadrados / n


def calcular_raiz_cuadrada(valor):
    """
    Req 2: Calcula raiz cuadrada sin usar math.sqrt (algoritmo basico),
    mediante Newton-Raphson, para obtener desviacion estandar.
    Req 6: Iteraciones fijas (constante) eficiente para muchos datos.
    """
    if valor is None:
        return None
    if valor < 0:
        return None
    if valor == 0:
        return 0.0

    estimacion = valor if valor >= 1.0 else 1.0

    # Req 2: Metodo iterativo basico; sin funciones de libreria.
    for _ in range(30):
        estimacion = 0.5 * (estimacion + (valor / estimacion))

    return estimacion


def formatear_numero(valor):
    """
    Req 2: Presenta resultados en un formato legible en pantalla/archivo.
    Req 3: Si un calculo no aplica (None), muestra N/A en lugar de fallar.
    """
    if valor is None:
        return "N/A"
    if valor == int(valor):
        return str(int(valor))
    return f"{valor:.6f}"


def construir_reporte(
    ruta_entrada,
    numeros_validos,
    total_valores,
    errores,
    stats,
):
    """
    Req 2: Construye texto para imprimir estadisticas en pantalla y archivo.
    Req 3: Incluye lista de errores detectados sin detener ejecucion.
    Req 7: Incluye tiempo transcurrido en el reporte.
    """
    media = stats["media"]
    mediana = stats["mediana"]
    modas = stats["modas"]
    varianza = stats["varianza"]
    desviacion_estandar = stats["desviacion_estandar"]
    tiempo_segundos = stats["tiempo_segundos"]

    lineas = []
    lineas.append("=== Statistics Results ===")
    lineas.append(f"Archivo de entrada: {ruta_entrada}")
    lineas.append(f"Valores leidos totales(validos + invalidos): {total_valores}")
    lineas.append(f"Numeros validos: {len(numeros_validos)}")
    lineas.append(f"Valores invalidos: {len(errores)}")
    lineas.append("")

    lineas.append("=== Descriptive Statistics ===")
    lineas.append(f"Mean (media): {formatear_numero(media)}")
    lineas.append(f"Median (mediana): {formatear_numero(mediana)}")

    if len(modas) == 0:
        lineas.append("Mode (moda): N/A (no hay moda)")
    else:
        modas_texto = ", ".join(formatear_numero(x) for x in modas)
        lineas.append(f"Mode (moda): {modas_texto}")

    lineas.append(f"Variance (varianza): {formatear_numero(varianza)}")
    lineas.append(
        "Standard deviation (desviacion estandar): "
        f"{formatear_numero(desviacion_estandar)}"
    )
    lineas.append("")
    lineas.append(f"Tiempo transcurrido (segundos): {tiempo_segundos:.6f}")

    if len(errores) > 0:
        lineas.append("")
        lineas.append("=== Errores detectados (se continuo la ejecucion) ===")
        for mensaje in errores:
            lineas.append(mensaje)

    lineas.append("")
    return "\n".join(lineas)


def escribir_archivo_salida(nombre_archivo, contenido):
    """
    Req 2: Escribe resultados en un archivo llamado StatisticsResults.txt.
    """
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(contenido)


def imprimir_uso():
    """
    Req 5: Muestra el formato minimo para invocar el programa.
    """
    print("Uso:")
    print("  python computeStatistics.py fileWithData.txt")


def main():
    """
    Req 1: Punto de entrada por linea de comandos.
    Req 5: Valida invocacion minima con parametro de archivo.
    Req 7: Mide y reporta el tiempo transcurrido de ejecucion y calculos.
    Req 2: Orquesta el calculo e impresion/archivo de resultados.
    Req 3: No se detiene por datos invalidos; reporta y continua.
    """
    tiempo_inicio = time.perf_counter()

    if len(sys.argv) < 2:
        imprimir_uso()
        sys.exit(1)

    ruta_entrada = sys.argv[1]

    numeros, errores, total_valores = leer_numeros_desde_archivo(ruta_entrada)

    numeros_ordenados = ordenar_lista(numeros) if len(numeros) > 0 else []

    stats = {}
    stats["media"] = calcular_media(numeros)
    stats["mediana"] = calcular_mediana(numeros_ordenados)
    stats["modas"] = calcular_moda(numeros)

    if stats["media"] is not None:
        stats["varianza"] = calcular_varianza(numeros, stats["media"])
    else:
        stats["varianza"] = None

    stats["desviacion_estandar"] = calcular_raiz_cuadrada(stats["varianza"])

    tiempo_fin = time.perf_counter()
    stats["tiempo_segundos"] = tiempo_fin - tiempo_inicio

    reporte = construir_reporte(
        ruta_entrada=ruta_entrada,
        numeros_validos=numeros,
        total_valores=total_valores,
        errores=errores,
        stats=stats,
    )

    print(reporte)

    try:
        escribir_archivo_salida(NOMBRE_ARCHIVO_SALIDA, reporte)
    except OSError as exc:
        print(
            f"Error al escribir el archivo de salida '{NOMBRE_ARCHIVO_SALIDA}': {exc}"
        )


# Req 1 y Req 4: Ejecucion directa desde CLI del archivo computeStatistics.py.
if __name__ == "__main__":
    main()
