""" Tarea: wordCount.py
Se bsuca cumplir los reuqisito sy no tener los errores al ejecurar esa cosa de pylint. 


P3 - TC4017 - Pruebas de software y aseguramiento de la calidad
Carlos Isaac Sagrero Campos - A01796826



"""
# pylint: disable=invalid-name

import sys
import time

# Req 2: Archivo de salida con nombre fijo WordCountResults.txt
NOMBRE_ARCHIVO_SALIDA = "../results/WordCountResults.txt"


def es_separador(caracter):
    """
    Req 1: El archivo contiene palabras presumiblemente separadas por espacios.
    """
    return caracter in (" ", "\t", "\n", "\r")


def es_letra_espanola(caracter):
    """
    Req 2: Computo con algoritmos basicos, sin librerias externas.
    Regla: Aceptar letras A-Z, a-z y letras con acentos en espanol, mas la enie.
    """
    codigo = ord(caracter)

    # Letras ASCII: A-Z y a-z
    if 65 <= codigo <= 90:
        return True
    if 97 <= codigo <= 122:
        return True

    # Vocales acentuadas y enie en Unicode
    # a e i o u (mayus y minus) con acento, y dieresis y la cosida de la eñe
    if caracter in (
        "á", "é", "í", "ó", "ú",
        "Á", "É", "Í", "Ó", "Ú",
        "ñ", "Ñ",
        "ü", "Ü",
    ):
        return True

    return False


def es_caracter_valido_en_palabra(caracter):
    """
    Req 3: Mecanismo para manejar datos invalidos.
    Modificacion solicitada: solo palabras (letras), incluyendo acentos en espanol.
    """
    return es_letra_espanola(caracter)


def a_minusculas_espanol(texto):
    """
    Req 2: Computo con algoritmos basicos (sin usar lower()).
    Convertimos mayusculas a minusculas para ASCII y letras espanolas comunes.
    """
    resultado = []
    i = 0
    while i < len(texto):
        c = texto[i]
        codigo = ord(c)

        # ASCII A-Z
        if 65 <= codigo <= 90:
            resultado.append(chr(codigo + 32))
        else:
            # Mapeo manual para letras espanolas
            if c == "Á":
                resultado.append("á")
            elif c == "É":
                resultado.append("é")
            elif c == "Í":
                resultado.append("í")
            elif c == "Ó":
                resultado.append("ó")
            elif c == "Ú":
                resultado.append("ú")
            elif c == "Ñ":
                resultado.append("ñ")
            elif c == "Ü":
                resultado.append("ü")
            else:
                resultado.append(c)

        i += 1
    return "".join(resultado)


def agregar_frecuencia(palabras, frecuencias, palabra):
    """
    Req 2: Identificar palabras distintas y frecuencia usando algoritmos basicos,
    sin usar dict/collections.Counter ni funciones equivalentes.
    Implementacion: listas paralelas (palabras, frecuencias) y busqueda lineal.
    Req 6: Manejar cientos a miles de items (aceptable).
    """
    if palabra == "":
        return

    indice = 0
    while indice < len(palabras):
        if palabras[indice] == palabra:
            frecuencias[indice] += 1
            return
        indice += 1

    palabras.append(palabra)
    frecuencias.append(1)


def procesar_archivo(ruta_archivo):
    """
    Req 1: Leer el archivo recibido como parametro.
    Req 2: Calcular palabras distintas y frecuencias.
    Req 3: Manejar datos invalidos (reportar y continuar).
    """
    palabras = []
    frecuencias = []

    try:
        with open(ruta_archivo, "r", encoding="utf-8", errors="replace") as archivo:
            # Req 3: errors="replace" evita que la lectura truene por bytes invalidos.
            linea_num = 0
            for linea in archivo:
                linea_num += 1
                palabra_actual = []
                pos = 0

                while pos < len(linea):
                    ch = linea[pos]

                    if es_separador(ch):
                        if palabra_actual:
                            palabra = "".join(palabra_actual)
                            palabra = a_minusculas_espanol(palabra)
                            agregar_frecuencia(palabras, frecuencias, palabra)
                            palabra_actual = []
                    else:
                        if es_caracter_valido_en_palabra(ch):
                            palabra_actual.append(ch)
                        else:
                            # Req 3: Reportar error y continuar la ejecucion.
                            print(
                                "Error: caracter invalido en linea "
                                + str(linea_num)
                                + " posicion "
                                + str(pos + 1)
                                + ": '"
                                + ch
                                + "'"
                            )

                    pos += 1

                if palabra_actual:
                    palabra = "".join(palabra_actual)
                    palabra = a_minusculas_espanol(palabra)
                    agregar_frecuencia(palabras, frecuencias, palabra)

    except FileNotFoundError:
        print("Error: no se encontro el archivo: " + ruta_archivo)
        return [], []
    except PermissionError:
        print("Error: sin permisos para leer el archivo: " + ruta_archivo)
        return [], []
    except OSError as exc:
        print("Error: no se pudo leer el archivo por OSError: " + str(exc))
        return [], []

    return palabras, frecuencias


def construir_lineas_resultado(palabras, frecuencias, segundos_transcurridos):
    """
    Req 2: Resultados en pantalla y en archivo WordCountResults.txt.
    Req 7: Incluir tiempo transcurrido en pantalla y archivo.
    """
    lineas = ["Word Count Results", "------------------"]
    i = 0
    while i < len(palabras):
        lineas.append(palabras[i] + " " + str(frecuencias[i]))
        i += 1
    lineas.append("------------------")
    lineas.append("Tiempo_transcurrido_segundos " + str(segundos_transcurridos))
    return lineas


def escribir_archivo_resultados(lineas, nombre_salida):
    """
    Req 2: Escribir resultados en archivo WordCountResults.txt.
    Req 3: Manejar errores de escritura y continuar (mostrar en consola).
    """
    try:
        with open(nombre_salida, "w", encoding="utf-8") as salida:
            i = 0
            while i < len(lineas):
                salida.write(lineas[i] + "\n")
                i += 1
    except PermissionError:
        print("Error: sin permisos para escribir el archivo: " + nombre_salida)
    except OSError as exc:
        print("Error: no se pudo escribir el archivo por OSError: " + str(exc))


def main():
    """
    Req 1: Invocacion por linea de comandos.
    Req 5: python wordCount.py fileWithData.txt
    Req 7: Medir tiempo de ejecucion y calculo.
    """
    if len(sys.argv) < 2:
        print("Uso: python wordCount.py fileWithData.txt")
        return 1

    ruta_archivo = sys.argv[1]

    inicio = time.perf_counter()  # Req 7: medir tiempo
    palabras, frecuencias = procesar_archivo(ruta_archivo)
    fin = time.perf_counter()
    segundos_transcurridos = fin - inicio

    lineas = construir_lineas_resultado(palabras, frecuencias, segundos_transcurridos)

    i = 0
    while i < len(lineas):
        print(lineas[i])
        i += 1

    escribir_archivo_resultados(lineas, NOMBRE_ARCHIVO_SALIDA)

    return 0


if __name__ == "__main__":
    sys.exit(main())
