
"""
convertNumbers.py

P2 - TC4017 - Pruebas de software y aseguramiento de la calidad
Carlos Isaac Sagrero Campos - A01796826

A ver que tal..
"""
# pylint: disable=invalid-name
import sys
import time


NOMBRE_ARCHIVO_SALIDA = "ConvertionResults.txt"
DIGITOS_HEX = "0123456789ABCDEF"


def convertir_a_binario(numero):
    """
    Req 2: Conversion a binario con algoritmo basico (division repetida).
    Req 8: PEP8.
    """
    if numero == 0:
        return "0"

    es_negativo = numero < 0
    valor = -numero if es_negativo else numero

    digitos = []
    while valor > 0:
        residuo = valor % 2
        digitos.append("1" if residuo == 1 else "0")
        valor //= 2

    digitos.reverse()
    resultado = "".join(digitos)
    return f"-{resultado}" if es_negativo else resultado


def convertir_a_hexadecimal(numero):
    """
    Req 2: Conversion a hexadecimal con algoritmo basico (division repetida).
    Req 8: PEP8.
    """
    if numero == 0:
        return "0"

    es_negativo = numero < 0
    valor = -numero if es_negativo else numero

    digitos = []
    while valor > 0:
        residuo = valor % 16
        digitos.append(DIGITOS_HEX[residuo])
        valor //= 16

    digitos.reverse()
    resultado = "".join(digitos)
    return f"-{resultado}" if es_negativo else resultado


def interpretar_entero(texto):
    """
    Req 3: Detecta datos invalidos para no detener la ejecucion.
    Req 8: PEP8.
    """
    limpio = texto.strip()
    if not limpio:
        return False, 0

    try:
        return True, int(limpio, 10)
    except ValueError:
        return False, 0


def procesar_archivo(ruta_entrada):
    """
    Req 1: Lee el archivo recibido como parametro.
    Req 2: Imprime resultados y escribe en ConvertionResults.txt.
    Req 3: Reporta errores y continua con el resto de datos.
    Req 6: Procesa linea por linea para soportar miles de elementos.
    Req 7: Calcula el tiempo transcurrido al final.
    Req 8: PEP8.
    """
    tiempo_inicio = time.perf_counter()

    with open(NOMBRE_ARCHIVO_SALIDA, "w", encoding="utf-8") as archivo_salida:
        encabezado = "Numero\tBinario\tHexadecimal"
        print(encabezado)
        archivo_salida.write(f"{encabezado}\n")

        with open(ruta_entrada, "r", encoding="utf-8") as archivo_entrada:
            for numero_linea, linea in enumerate(archivo_entrada, start=1):
                valido, numero = interpretar_entero(linea)
                if not valido:
                    print(
                        f"Error (linea {numero_linea}): dato invalido -> "
                        f"{linea.strip()}"
                    )
                    continue

                binario = convertir_a_binario(numero)
                hexadecimal = convertir_a_hexadecimal(numero)

                fila = f"{numero}\t{binario}\t{hexadecimal}"
                print(fila)
                archivo_salida.write(f"{fila}\n")

        tiempo_total = time.perf_counter() - tiempo_inicio
        mensaje_tiempo = f"Tiempo transcurrido (s): {tiempo_total:.6f}"
        print(mensaje_tiempo)
        archivo_salida.write(f"{mensaje_tiempo}\n")


def main():
    """
    Req 1: Permite ejecucion desde linea de comandos.
    Req 5: Valida el formato minimo de invocacion.
    Req 8: PEP8.
    """
    if len(sys.argv) != 2:
        print("Uso: python convertNumbers.py fileWithData.txt")
        sys.exit(1)

    ruta_entrada = sys.argv[1]
    try:
        procesar_archivo(ruta_entrada)
    except FileNotFoundError:
        print(f"Error: archivo no encontrado -> {ruta_entrada}")
        sys.exit(1)
    except OSError as error:
        print(f"Error: no se pudo leer el archivo -> {ruta_entrada} ({error})")
        sys.exit(1)


if __name__ == "__main__":
    main()
